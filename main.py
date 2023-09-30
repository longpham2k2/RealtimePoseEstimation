import numpy as np
import cv2
import mediapipe as mp
from pose_collection import poses_conditions, gesture_sequences
from keyboard_controller import perform_keyboard_input, handle_game_control

# Initialize mediapipe pose class.
mp_pose = mp.solutions.pose

# Setup the Pose function for video stream processing.
pose_video = mp_pose.Pose(min_detection_confidence=0.5,
                          min_tracking_confidence=0.5)

# Initialize mediapipe drawing class - to draw the landmarks points.
mp_drawing = mp.solutions.drawing_utils

# Define a function to perform pose detection and keypoints extraction on each frame of the video stream.


def detectPoseAndKeypoints(frame, pose, draw=False, pose_conditions=None):
    # Convert the frame to RGB format (required by Mediapipe)
    image_in_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform pose estimation on the frame
    resultant = pose.process(image_in_RGB)

    if resultant.pose_landmarks and draw:
        # Draw landmarks and connections on the frame
        mp_drawing.draw_landmarks(frame, landmark_list=resultant.pose_landmarks,
                                  connections=mp_pose.POSE_CONNECTIONS,
                                  landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255, 255, 255),
                                                                               thickness=3, circle_radius=3),
                                  connection_drawing_spec=mp_drawing.DrawingSpec(color=(49, 125, 237),
                                                                                 thickness=2, circle_radius=2))

        # Viết thêm phụ đề
        for idx, landmark in enumerate(resultant.pose_landmarks.landmark):
            h, w, c = frame.shape
            cx, cy = int(landmark.x * w), int(landmark.y * h)
            text_position = (cx, cy)
            cv2.putText(frame, str(idx), text_position,
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        #     print(f"Keypoint {idx}: ({cx}, {cy})")

        if pose_conditions is not None:
            recognized_poses = []
            # Nhận dạng các pose
            for pose_name, condition in pose_conditions.items():
                if condition(resultant.pose_landmarks):
                    # Perform action based on the pose condition
                    # break
                    recognized_poses.append(pose_name)

            # Nhận dạng các tổ hợp pose
            matched_sequence = None
            for gesture_name, pose_sequence in gesture_sequences.items():
                if all(pose in recognized_poses for pose in pose_sequence):
                    matched_sequence = gesture_name

            # Viết tên pose lên màn hình
            full_pose_name = ", ".join(recognized_poses)
            cv2.putText(frame, full_pose_name, (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Viết tên sequence lên màn hình nếu có
            if matched_sequence:
                handle_game_control(matched_sequence)
                True # To do nothing if the above line are commented out
                # Perform an action based on the matched sequence (e.g., simulate keyboard input)
                # You can define actions for each matched sequence here
            else:
                handle_game_control(None)
                matched_sequence = "No matched sequence"
            cv2.putText(frame, matched_sequence, (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame

# Open a video capture stream (0 represents the default camera, change it if needed)
cap = cv2.VideoCapture(1)

while cap.isOpened():
    ret, frame = cap.read()  # Read a frame from the camera

    if not ret:
        continue

    # Process the frame for pose detection and keypoints extraction
    processed_frame = detectPoseAndKeypoints(
        frame, pose_video, draw=True, pose_conditions=poses_conditions)

    # Display the processed frame
    cv2.imshow('Pose Detection', processed_frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
