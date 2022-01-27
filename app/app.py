from tkinter.constants import S
import cv2
# import pyautogui
import numpy as np
import tkinter as tk
import datetime
from PIL import Image, ImageTk,ImageGrab
class App:
    def __init__(self):
        # self.path = path
        self.window = tk.Tk()
        self.window.geometry("600x400")
        self.screen = MyFrame()
        self.r = False
        self.out = cv2.VideoWriter()
        self.label = tk.Label(self.window)
        self.label.pack()
        self.delay = 15
        self.path = "/home/danh/Desktop/record-app/app/"
        self.count = 1
    # @staticmethod
    def update(self):
        #print(self.r)
        #print(self.count)
        time = datetime.datetime.now()
        nameVideo = self.path + time.strftime("%d")+"-"+time.strftime("%m")+"-"+time.strftime("%Y")+"-"+time.strftime("%H")+"-"+time.strftime("%f")+".avi"
        frame_width,frame_height,frame,frameResized = self.screen.getframe()
        #print(frame_width,frame_height)
        if self.r == True:
            self.out = cv2.VideoWriter(nameVideo,cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width,frame_height))
            self.r = False
        if self.count % 2 == 0:
            self.out.write(frame)
        photo = ImageTk.PhotoImage(image = Image.fromarray(frameResized))
        self.label.image = photo
        self.label.configure(image=photo)
        self.label.place(x=0,y=0)
        self.window.after(self.delay,self.update)
    def run(self):
        self.createButton()
        self.update()
        # self.createButton()
        self.window.mainloop()
    def createButton(self):
        self.B1 = tk.Button(self.window,text="save",command=self.save)
        self.L1 = tk.Label(self.window,text="Path")
        self.P1 = tk.Entry(self.window)
        self.P1.place(x=70,y=300)
        self.L1.place(x=30,y=300)
        self.B1.place(x=250,y=300)
        if self.r == True:
            self.button = tk.Button(self.window,text="recording",command=self.record)
            self.button.place(x=500,y=0)
        else:
            self.button = tk.Button(self.window,text="record",command=self.record)
            self.button.place(x=500,y=0)
    def save(self):
        self.path = self.P1.get()
        print(self.path)

    def record(self):
        self.count += 1
        self.r = True if self.count % 2 == 0 else False
        #self.rText = "recording" if self.r == True else "record"
class MyFrame:
    def __init__(self):
        pass
    def getframe(self):
        img = ImageGrab.grab()
        frame = np.array(img)
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frameResized = cv2.resize(frame,(480,270))
        return frame.shape[1],frame.shape[0],frame,frameResized
if __name__ == "__main__":
    a = App()
    a.run()
