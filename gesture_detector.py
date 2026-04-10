import math

class GestureDetector:
    def __init__(self):
        self.tips_ids = [4, 8, 12, 16, 20]
        self.wrist_id = 0

    def is_fist(self, hand_landmarks):

        wrist = hand_landmarks.landmark[self.wrist_id]

        total_dist = 0
        for tip_id in self.tips_ids:
            tip = hand_landmarks.landmark[tip_id]

            dist = math.sqrt(
                (tip.x - wrist.x)**2 + 
                (tip.y - wrist.y)**2
            )
            total_dist += dist

        avg_dist = total_dist / len(self.tips_ids)
        return avg_dist < 0.2