import cv2
import mediapipe as mp
import math
import random
from face_tracker import FaceTracker
from gesture_detector import GestureDetector

def setup():

    mp_hands = mp.solutions.hands
    hands_detector = mp_hands.Hands(min_detection_confidence=0.7, 
                                    min_tracking_confidence=0.5)
    draw_utils = mp.solutions.drawing_utils

    white_dots_spec = draw_utils.DrawingSpec(
        color=(255, 255, 255),
        thickness=1,
        circle_radius=2
    )

    yellow_lines_spec = draw_utils.DrawingSpec(
        color=(200, 253, 255), 
        thickness=1, circle_radius=0)

    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("could not open camera")
        exit()

    camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    sword_img = None
    try:
        sword_img = cv2.imread("sword.png", cv2.IMREAD_UNCHANGED)
        if sword_img is not None:
            sword_img = cv2.resize(sword_img, (200, 200))
            print("could not download")
        else:
            print("not found")
    except Exception as e:
        print(f"ERROR {e}")


    return mp_hands, hands_detector, draw_utils, camera, white_dots_spec, yellow_lines_spec, sword_img

def main():

    mp_hands, hands_detector, draw_utils, camera, white_dots_spec, yellow_lines_spec, sword_img = setup()
    active_finger_id = 8
    face_tracker = FaceTracker()
    gesture_detector = GestureDetector()

    finger_names = {
        4: "thumb",
        8: "index",
        12: "middle",
        16: "ring",
        20: "pinky"
    }

    print("Started")

    while True:
        ret, frame = camera.read()
        if not ret or frame is None:
            print("lost connection")
            camera.release()
            camera = cv2.VideoCapture(0)
            continue

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break
        elif key == ord("f"):
            state = face_tracker.toggle()
            print("face on")
        elif key == ord("1"):
            active_finger_id = 4
        elif key == ord("2"):
            active_finger_id = 8
        elif key == ord("3"):
            active_finger_id = 12
        elif key == ord("4"):
            active_finger_id = 16
        elif key == ord("5"):
            active_finger_id = 20

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb_frame.flags.writeable = False 

        has_sword = False

        try:
            results = hands_detector.process(rgb_frame)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    hand_detected = True
                    draw_utils.draw_landmarks(
                        frame, 
                        hand_landmarks, 
                        mp_hands.HAND_CONNECTIONS, 
                        landmark_drawing_spec=white_dots_spec, 
                        connection_drawing_spec=yellow_lines_spec)
                    
                    if gesture_detector.is_fist(hand_landmarks):
                        has_sword = True
                        base_index = hand_landmarks.landmark[5]
                        wx, wy = int(base_index.x * w), int(base_index.y * h)
                        x_off, y_off = wx - 20, wy - 25

                        if sword_img is not None:
                            try:
                                h_s, w_s, _ = sword_img.shape

                                y_off = max(0, min(y_off, h - h_s))
                                x_off = max(0, min(x_off, w - w_s))

                                roi = frame[y_off:y_off + h_s, x_off:x_off + w_s]

                                alpha_s = sword_img[:, :, 3] / 255.0
                                
                                alpha_l = 1.0 - alpha_s
                                for c in range(0, 3):
                                    roi[:, :, c] = (alpha_s * sword_img[:, :, c] + alpha_l * roi[:, :, c])

                            except: pass
                        else:
                            cv2.rectangle(frame, (wx - 20, wy - 60), (wx + 130, wy - 40), (100, 100, 100), -1 )
                            cv2.putText(frame, "SWORD", (wx, wy, -70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    
                    else:
                        tip = hand_landmarks.landmark[active_finger_id]
                        x_pixel = int(tip.x * w)
                        y_pixel = int(tip.y * h)
                        cv2.circle(frame, (x_pixel, y_pixel), 7, (0, 0, 255), -1)

                    tip = hand_landmarks.landmark[active_finger_id]

        except Exception as e:
            print(f"Error {e}")
        finally:
            rgb_frame.flags.writeable = True

        face_tracker.draw(frame, rgb_frame)
        status = ">>SWORD MODE<<" if has_sword else "<<HAND MODE>>"
        cv2.putText(frame, status, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 255), 2)

        current_finger_name = finger_names.get(active_finger_id, "unknown")
        cv2.putText(frame, f"Finger: {current_finger_name} ({active_finger_id})", (20, frame.shape[0] - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)           
        cv2.putText(frame, "press F; Q; 1-5", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

        cv2.imshow("TRACKING GAME", frame)

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()