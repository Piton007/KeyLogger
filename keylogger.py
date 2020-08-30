from pynput import keyboard
import smtplib


def on_release(key):
    if key == keyboard.Key.esc:
        return False
    print("{0} released".format(key))
with keyboard.Listener(on_release=on_release) as listener:
    listener.join()


