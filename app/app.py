from tkinter.constants import S
import cv2
# import pyautogui
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk,ImageGrab
class App:
    def __init__(self):
        # self.path = path
        self.window = tk.Tk()
        self.window.geometry("600x500")
        self.screen = MyFrame()
        self.label = tk.Label(self.window)
        self.label.pack()
        self.delay = 15
    # @staticmethod
    def update(self):
        frame = self.screen.getframe()
        # print(frame.shape)
        photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
        self.label.image = photo
        self.label.configure(image=photo)
        self.label.place(x=0,y=0)
        self.window.after(self.delay,self.update)
    def run(self):
        self.update()
        self.window.mainloop()
class MyFrame:
    def __init__(self):
        pass
    def getframe(self):
        img = ImageGrab.grab()
        frame = np.array(img)
        frame = cv2.resize(frame,(480,270))
        return cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

if __name__ == "__main__":
    a = App()
    a.run()