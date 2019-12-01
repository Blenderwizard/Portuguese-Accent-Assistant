#pynput Library input, omitting mouse control
from pynput import keyboard
from pynput.keyboard import Key, Controller

#Time library, to fix shift key bug
import time

#variable Inits
lastkeys = ["", ""] #last 2 keystroke keeper
temp = "" #last key
sendUpper = 0 #test for shift
stop = 0 #test for special character
keyboardC = Controller() #typer
unpressed_time = 1 #increase accuracy
pressed_time = 0 #increase accuracy

#recognize when a key has been pressed, stops tracking when any special key apart from shift is pressed
def on_press(key):
    global sendUpper
    global stop
    try:
        'alphanumeric key {0} pressed'.format(key.char)
    except AttributeError:
        'special key {0} pressed'.format(key)
        if ((key == keyboard.Key.shift_r) or (key == keyboard.Key.shift)):
            sendUpper = 1
        else:
            stop = 1

#detects the end of a keystroke, if last two keys match a code, backspace twice and prints the letter
def on_release(key):
    global sendUpper
    global temp
    global stop
    global keyboardC
    global pressed_time
    global unpressed_time
    try:
        temp = '{0}'.format(key.char)
        unpressed_time = time.time()
        if stop == 0:
            if ((sendUpper == 1) or (unpressed_time - pressed_time <= .1)):
                if '{0}'.format(key.char) == '`':
                    temp = '~'
                elif '{0}'.format(key.char) == '6':
                    temp = '^'
                elif '{0}'.format(key.char) == ',':
                    temp = '<'
                elif '{0}'.format(key.char) == '.':
                    temp = '>'
                else:
                    temp = temp.upper()
            lastkeys[0] = lastkeys[1]
            lastkeys[1] = temp
        stop = 0
        pressed_time = 0
        unpressed_time = 1
        if (lastkeys[0] == ';'):
            if (lastkeys[1] == 'a'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('á')
                keyboardC.release('á')
            if (lastkeys[1] == 'A'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('Á')
                keyboardC.release('Á')
            if (lastkeys[1] == 'c'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('ç')
                keyboardC.release('ç')
            if (lastkeys[1] == 'C'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('Ç')
                keyboardC.release('Ç')
            if (lastkeys[1] == 'e'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('é')
                keyboardC.release('é')
            if (lastkeys[1] == 'E'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('É')
                keyboardC.release('É')
            if (lastkeys[1] == 'i'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('í')
                keyboardC.release('í')
            if (lastkeys[1] == 'I'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('Í')
                keyboardC.release('Í')
            if (lastkeys[1] == 'o'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('ó')
                keyboardC.release('ó')
            if (lastkeys[1] == 'O'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('Ó')
                keyboardC.release('Ó')
            if (lastkeys[1] == 'u'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('ú')
                keyboardC.release('ú')
            if (lastkeys[1] == 'U'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('Ú')
                keyboardC.release('Ú')
            if (lastkeys[1] == '<'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('«')
                keyboardC.release('«')
            if (lastkeys[1] == '>'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('»')
                keyboardC.release('»')
            if (lastkeys[1] == '-'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('—')
                keyboardC.release('—')
        elif (lastkeys[0] == '^'):
            if (lastkeys[1] == 'a'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('â')
                keyboardC.release('â')
            if (lastkeys[1] == 'A'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('Â')
                keyboardC.release('Â')
            if (lastkeys[1] == 'o'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('ô')
                keyboardC.release('ô')
            if (lastkeys[1] == 'O'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('Ô')
                keyboardC.release('Ô')
            if (lastkeys[1] == 'e'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('ê')
                keyboardC.release('ê')
            if (lastkeys[1] == 'E'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('Ê')
                keyboardC.release('Ê')
        elif (lastkeys[0] == '~'):
            if (lastkeys[1] == 'a'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('ã')
                keyboardC.release('ã')
            if (lastkeys[1] == 'A'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('Ã')
                keyboardC.release('Ã')
            if (lastkeys[1] == 'o'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('õ')
                keyboardC.release('õ')
            if (lastkeys[1] == 'O'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('Õ')
                keyboardC.release('Õ')
        elif (lastkeys[0] == '`'):
            if (lastkeys[1] == 'a'):
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press(Key.backspace)
                keyboardC.release(Key.backspace)
                keyboardC.press('à')
                keyboardC.release('à')
    except AttributeError:
        if ((key == keyboard.Key.shift_r) or (key == keyboard.Key.shift)):
            pressed_time = time.time()
            sendUpper = 0
        elif ((key == keyboard.Key.ctrl_r) or (key == keyboard.Key.ctrl_l)):
            stop = 0
        elif ((key == keyboard.Key.alt_r) or (key == keyboard.Key.alt_l)):
            stop = 0
        elif (key == keyboard.Key.backspace):
            stop = 0
            lastkeys[0] = lastkeys[1]
            lastkeys[1] = ''
        elif (key == keyboard.Key.enter):
            stop = 0
            lastkeys[0] = lastkeys[1]
            lastkeys[1] = ''
        elif (key == keyboard.Key.space):
            stop = 0
            lastkeys[0] = lastkeys[1]
            lastkeys[1] = ''
        else:
            stop = 1
            lastkeys[0] = lastkeys[1]
            lastkeys[1] = ''
    
# Collect events FOREVER
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
