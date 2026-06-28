import keyboard

def print_pressed_keys(e):
    print(e.name)

keyboard.hook(print_pressed_keys)
keyboard.wait()