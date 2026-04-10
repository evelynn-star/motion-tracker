import mediapipe as mp
import cv2

class FaceTracker:
    def __init__(self):
        self.mp_face_mesh = mp.solutions.face_mesh
        self.face_mesh = self.mp_face_mesh.FaceMesh(
            max_num_faces=1, 
            min_detection_confidence=0.5, 
            min_tracking_confidence=0.5 )
        
        self.draw_utils = mp.solutions.drawing_utils

        self.point_spec = self.draw_utils.DrawingSpec(
            color=(255, 255, 255),
            thickness=1,
            circle_radius=1
        )

        self.contour_spec = self.draw_utils.DrawingSpec(
            color=(250, 100, 0),
            thickness=2,
            circle_radius=0)
        
        self.mesh_spec = self.draw_utils.DrawingSpec(
            color=(235, 201, 52),
            thickness=1,
            circle_radius=0)
        
        self.is_active = False
    
    def toggle(self):

        self.is_active = not self.is_active
        return self.is_active
        
    def draw(self, frame, rgb_frame):
        if not self.is_active:
            return
        
        results = self.face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                self.draw_utils.draw_landmarks(
                    image = frame,
                    landmark_list = face_landmarks,
                    connections = self.mp_face_mesh.FACEMESH_TESSELATION,
                    landmark_drawing_spec = None,
                    connection_drawing_spec = self.mesh_spec
                )

                self.draw_utils.draw_landmarks(
                    image = frame,
                    landmark_list = face_landmarks,
                    connections = self.mp_face_mesh.FACEMESH_CONTOURS,
                    landmark_drawing_spec = None,
                    connection_drawing_spec = self.contour_spec
                )

                self.draw_utils.draw_landmarks(
                    image = frame,
                    landmark_list = face_landmarks,
                    connections = [],
                    landmark_drawing_spec = self.point_spec,
                    connection_drawing_spec = None
                )