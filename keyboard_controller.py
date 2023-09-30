import keyboard
from pose_collection import sequence_keybounds, sequence_keycombos

# Tất cả phím đều là nhấn không giữ
def perform_keyboard_input(recognized_sequence):
    if recognized_sequence in sequence_keybounds:
        key = sequence_keybounds[recognized_sequence]
        keyboard.press_and_release(key)

current_gesture_sequence = None
pressed_keys = set()
# Cho phép giữ phím (ví dụ như WASD để chơi game)
def handle_game_control(new_gesture_sequence): 
    global current_gesture_sequence
    global pressed_keys

    if (new_gesture_sequence):
        if new_gesture_sequence in sequence_keycombos:
            new_keys = set(sequence_keycombos[new_gesture_sequence]) # Combo key bound
            keys_to_press = new_keys - pressed_keys
            keys_to_release = pressed_keys - new_keys
            for key_to_r in keys_to_release:
                keyboard.release(key_to_r)
                pressed_keys.remove(key_to_r)
            for key_to_p in keys_to_press:
                if key_to_p in ("a", "d"):
                    # Is movement key
                    keyboard.press(key_to_p)
                    pressed_keys.add(key_to_p)
                else:
                    # Is action key
                    keyboard.press_and_release(key_to_p)

    # Old logic: switch getsure sequence will release keys. This works but is overly complicated
    # if new_gesture_sequence != current_gesture_sequence:
    #     pressed_keys.clear()
    #     if (current_gesture_sequence):
    #         if current_gesture_sequence in sequence_keybounds:
    #             # current_key = sequence_keybounds[current_gesture_sequence] # Single key bound
    #             # keyboard.release(current_key)
    #             current_keys = sequence_keycombos[current_gesture_sequence] # Combo key bound
    #             for cur_key in current_keys:
    #                 keyboard.release(cur_key)

    #     current_gesture_sequence = new_gesture_sequence

    #     if (new_gesture_sequence):
    #         if new_gesture_sequence in sequence_keycombos:
    #             # new_key = sequence_keybounds[new_gesture_sequence] # Single key bound
    #             # if new_key in ("a", "d"):
    #             #     # Is movement key
    #             #     keyboard.press(new_key)
    #             # else:
    #             #     # Is action key
    #             #     keyboard.press_and_release(new_key)
    #             #     current_gesture_sequence = None
    #             new_keys = sequence_keycombos[new_gesture_sequence] # Combo key bound
    #             for n_key in new_keys:
    #                 if n_key in ("a", "d"):
    #                     # Is movement key
    #                     keyboard.press(n_key)
    #                 else:
    #                     # Is action key
    #                     keyboard.press_and_release(n_key)
    #                     # current_gesture_sequence = None
