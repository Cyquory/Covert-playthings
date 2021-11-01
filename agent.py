import time
import random
import threading
from pynput import mouse, keyboard
import pydirectinput

def main():
    operator_thread = Operator()
    operator_thread.start()
    trigger = keyboard.KeyCode.from_char('-')
    kill_switch = keyboard.KeyCode.from_char('=')
    
    def on_press(key):
        if key == trigger:
            if operator_thread.running:
                operator_thread.pause()
            else:
                operator_thread.play()
        elif key == kill_switch:
            # Stop listener
            operator_thread.terminate()
            print(f'Program ended')
            return False
        elif key == keyboard.Key.right:
            operator_thread.mode = (operator_thread.mode+1)%operator_thread.get_modecount()
            operator_thread.pause()
            print(f'Program now in mode: {operator_thread.get_description()}')
        elif key == keyboard.Key.left:
            operator_thread.mode = (operator_thread.mode-1)%operator_thread.get_modecount()
            operator_thread.pause()
            print(f'Program now in mode: {operator_thread.get_description()}')
        elif key == keyboard.Key.down:
            if operator_thread.mode == 0 or operator_thread.mode == 3:
                operator_thread.play()

    def on_click(x, y, button, pressed):
        if button == mouse.Button.middle and operator_thread.mode == 1:
            if pressed:
                operator_thread.play()
            else:
                operator_thread.pause()
        
    
    # mouse listener in non-blocking manner
    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()
    # keyboard listener 
    with keyboard.Listener(on_press=on_press) as listener:
        print(f'Program starting in mode: {operator_thread.get_description()}')
        listener.join()

class Operator(threading.Thread):
    def __init__(self):
        super(Operator, self).__init__()
        self.mouse_ctl = mouse.Controller()
        self.keyboad_ctl = keyboard.Controller()
        self.running = False
        self.alive = True
        self.description = {0: 'autocommand',
                            1: 'hitting',
                            2: 'mob grinding',
                            # 3: 'naive nuke',
            }
        self.mode = 1

    def terminate(self):
        # to end this thread
        self.pause()
        self.alive = False

    def play(self):
        self.running = True

    def pause(self):
        self.running = False

    def get_description(self):
        return self.description[self.mode]

    def get_modecount(self):
        return len(self.description)

    def clicking(self):
        self.mouse_ctl.click(mouse.Button.left)
        d = 0.1+random.random()*0.1
        time.sleep(d)

    def command(self):
        pydirectinput.press('t')
        pydirectinput.write('/sell')
        time.sleep(0.02)
        pydirectinput.press('enter')
        pydirectinput.press('t')
        pydirectinput.write('/pmine regen')
        time.sleep(0.02)
        pydirectinput.press('enter')
        self.pause()

    def move_quarter_sphere(self):
        pydirectinput.move(0,5)
        self.pause()

    def run(self):
        while self.alive:
            while self.running:
                if self.mode == 0:
                    self.command()
                elif self.mode == 1:
                    self.clicking()
                elif self.mode == 2:
                    self.clicking()
                elif self.mode == 3:
                    self.move_quarter_sphere()
                else:
                    print(f'no implement error')
                    self.terminate()
                    break
            time.sleep(0.05)

if __name__ == "__main__":
    main()