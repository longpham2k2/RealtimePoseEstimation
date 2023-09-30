from utils import angle_of, do_lines_intersect, almost_collapsed, distance, distance_between_segments

# Collection of poses' conditions
poses_conditions = {
    "Palms Together": lambda landmarks: almost_collapsed((landmarks.landmark[15].x, landmarks.landmark[15].y), (landmarks.landmark[16].x, landmarks.landmark[16].y), 35 / 100 * distance((landmarks.landmark[11].x, landmarks.landmark[11].y), (landmarks.landmark[12].x, landmarks.landmark[12].y))),
    "Fold arms": lambda landmarks: distance_between_segments((landmarks.landmark[13].x, landmarks.landmark[13].y), (landmarks.landmark[15].x, landmarks.landmark[15].y), (landmarks.landmark[14].x, landmarks.landmark[14].y), (landmarks.landmark[16].x, landmarks.landmark[16].y)) < 15 / 100 * distance((landmarks.landmark[11].x, landmarks.landmark[11].y), (landmarks.landmark[12].x, landmarks.landmark[12].y)) and abs(angle_of((landmarks.landmark[13].x, landmarks.landmark[13].y), (landmarks.landmark[15].x, landmarks.landmark[15].y)) - angle_of((landmarks.landmark[14].x, landmarks.landmark[14].y), (landmarks.landmark[16].x, landmarks.landmark[16].y))) <= 15,
    "Cross arms": lambda landmarks: do_lines_intersect((landmarks.landmark[13].x, landmarks.landmark[13].y), (landmarks.landmark[15].x, landmarks.landmark[15].y), (landmarks.landmark[14].x, landmarks.landmark[14].y), (landmarks.landmark[16].x, landmarks.landmark[16].y)),
    "Raise right arm": lambda landmarks: angle_of((landmarks.landmark[12].x, landmarks.landmark[12].y), (landmarks.landmark[16].x, landmarks.landmark[16].y)) > 45 and landmarks.landmark[12].y > landmarks.landmark[16].y,
    "Open right arm": lambda landmarks: angle_of((landmarks.landmark[12].x, landmarks.landmark[12].y), (landmarks.landmark[16].x, landmarks.landmark[16].y)) < 45 and landmarks.landmark[12].x > landmarks.landmark[16].x,
    "Fold right arm": lambda landmarks: angle_of((landmarks.landmark[12].x, landmarks.landmark[12].y), (landmarks.landmark[16].x, landmarks.landmark[16].y)) < 45 and landmarks.landmark[12].x < landmarks.landmark[16].x,
    "Lower right arm": lambda landmarks: angle_of((landmarks.landmark[12].x, landmarks.landmark[12].y), (landmarks.landmark[16].x, landmarks.landmark[16].y)) > 45 and landmarks.landmark[12].y < landmarks.landmark[16].y,
    "Raise left arm": lambda landmarks: angle_of((landmarks.landmark[11].x, landmarks.landmark[11].y), (landmarks.landmark[15].x, landmarks.landmark[15].y)) > 45 and landmarks.landmark[11].y > landmarks.landmark[15].y,
    "Open left arm": lambda landmarks: angle_of((landmarks.landmark[11].x, landmarks.landmark[11].y), (landmarks.landmark[15].x, landmarks.landmark[15].y)) < 45 and landmarks.landmark[11].x < landmarks.landmark[15].x,
    "Fold left arm": lambda landmarks: angle_of((landmarks.landmark[11].x, landmarks.landmark[11].y), (landmarks.landmark[15].x, landmarks.landmark[15].y)) < 45 and landmarks.landmark[11].x > landmarks.landmark[15].x,
    "Lower left arm": lambda landmarks: angle_of((landmarks.landmark[11].x, landmarks.landmark[11].y), (landmarks.landmark[15].x, landmarks.landmark[15].y)) > 45 and landmarks.landmark[11].y < landmarks.landmark[15].y,
    "Lean left": lambda landmarks: landmarks.landmark[12].y < landmarks.landmark[11].y,
    "Lean right": lambda landmarks: landmarks.landmark[12].y > landmarks.landmark[11].y,
}

gesture_sequences = {
    "Fold arms": ["Fold arms"],
    "Raise both arms": ["Raise right arm", "Raise left arm"],
    "Raise right arm": ["Raise right arm", "Lower left arm"],
    "Raise right Open left": ["Raise right arm", "Open left arm"],
    "Open right arm": ["Open right arm", "Lower left arm"],
    "Raise left arm": ["Raise left arm", "Lower right arm"],
    "Raise left Open right": ["Raise left arm", "Open right arm"],
    "Open left arm": ["Open left arm", "Lower right arm"],
    "Lower both arms": ["Lower right arm", "Lower left arm"],
}

sequence_keybounds = {
    "Raise both arms": "w",
    "Open right arm": "d",
    "Open left arm": "a",
    "Lower both arms": "s",
}

sequence_keycombos = {
    "Raise both arms": ["w"],
    "Raise right Open left": ["w", "a"],
    "Raise left Open right": ["w", "d"],
    "Open right arm": ["d"],
    "Open left arm": ["a"],
    "Fold arms": ["s"],
}
