import tkinter
#import tk
from tkinter import ttk
from tkinter import StringVar, IntVar, PhotoImage
import tkinter.messagebox
import customtkinter
from multiprocessing import Process

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_appearance_mode("light")

from time import strftime
from time import gmtime
import threading
import time
from playsound import playsound

import random

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()        
        startscale = 1 
        self.colormode = "light"
        monitor_height = self.winfo_screenheight()
        monitor_width = self.winfo_screenwidth()
        self.HEIGHT = int(monitor_height * startscale) 
        self.WIDTH = int(monitor_height*1.3 * startscale)
        self.WScale = self.WIDTH/1300
        print(self.HEIGHT,self.WIDTH)

        self.starttime = 390
        self.bank = 600

        # self.starttime = 15
        # self.bank = 15

        self.time = {
            "t1":self.starttime,
            "t2":self.starttime,
            "b1":self.bank,
            "b2":self.bank,
        }
        
        self.title("BBBank")
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.NormalMode()

        self.ap = 1
        
    def on_closing(self, event=0):
        self.sampling = False
        self.quit()
        self.destroy()

    def start(self):
        self.mainloop()

    def my_time(self):
        time_string = strftime('%M:%S') # time format 
        l1.after(1000,my_time) # time delay of 1000 milliseconds 
        
        
    def NormalMode(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=2)
        #self.grid_rowconfigure(1, weight=1)

        self.timestr = {
            "t1":strftime("%M:%S", gmtime(self.starttime)),
            "t2":strftime("%M:%S", gmtime(self.starttime)),
            "b1":strftime("%M:%S", gmtime(self.bank)),
            "b2":strftime("%M:%S", gmtime(self.bank)),        
        }
        self.timevar = {
            "t1":StringVar(),
            "t2":StringVar(),
            "b1":StringVar(),
            "b2":StringVar(), 
        }
        
        self.frame_left = customtkinter.CTkFrame(master=self)
        self.frame_left.grid(row=0, column=0, sticky="nswe",padx=int(20*self.WScale), pady=int(20*self.WScale))
        
        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=int(20*self.WScale), pady=int(20*self.WScale))
        
        self.frame_left.grid_columnconfigure(0, weight=1)
        self.frame_left.grid_columnconfigure(1, weight=2)
        self.frame_left.grid_columnconfigure(2, weight=1)        
        self.frame_left.grid_rowconfigure(0, weight=1)
        self.frame_left.grid_rowconfigure(1, weight=2)
        self.frame_left.grid_rowconfigure(2, weight=1)        

        self.frame_left_name = customtkinter.CTkFrame(master=self.frame_left,height=50)
        self.frame_left_name.grid(row=0, column=0, sticky="nswe",padx=int(20*self.WScale), pady=int(20*self.WScale),columnspan=3)
        self.p1 = customtkinter.CTkLabel(master=self.frame_left_name,text="Player 1",font=("Roboto Medium", int(30*self.WScale) ))  # font name and size in p
        self.p1.grid(row=1, column=0, pady=int(5*self.WScale), padx=int(10*self.WScale)) 
        self.p1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.timevar["t1"].set(self.timestr["t1"])
        self.frame_left_bank = customtkinter.CTkFrame(master=self.frame_left)
        self.frame_left_bank.grid(row=1, column=0, sticky="nswe",padx=int(20*self.WScale), pady=int(20*self.WScale),columnspan=3)
        self.t1 = customtkinter.CTkLabel(master=self.frame_left_bank,textvariable=self.timevar["t1"],font=("Roboto Medium", int(52*self.WScale) ))  # font bank and size in p
        self.t1.grid(row=1, column=0, pady=int(5*self.WScale), padx=int(10*self.WScale)) 
        self.t1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.timevar["b1"].set(self.timestr["b1"])
        self.frame_left_time = customtkinter.CTkFrame(master=self.frame_left)
        self.frame_left_time.grid(row=2, column=0, sticky="nswe",padx=int(20*self.WScale), pady=int(20*self.WScale),columnspan=3)
        self.b1 = customtkinter.CTkLabel(master=self.frame_left_time,textvariable=self.timevar["b1"],font=("Roboto Medium", int(42*self.WScale) ))  # font time and size in p
        self.b1.grid(row=1, column=1, pady=int(5*self.WScale), padx=int(10*self.WScale),sticky="nswe",rowspan=5) 
        self.b1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_columnconfigure(1, weight=2)
        self.frame_right.grid_columnconfigure(2, weight=1)        
        self.frame_right.grid_rowconfigure(0, weight=1)
        self.frame_right.grid_rowconfigure(1, weight=2)
        self.frame_right.grid_rowconfigure(2, weight=1)        

        self.frame_right_name = customtkinter.CTkFrame(master=self.frame_right,height=50)
        self.frame_right_name.grid(row=0, column=0, sticky="nswe",padx=int(20*self.WScale), pady=int(20*self.WScale),columnspan=3)
        self.p2 = customtkinter.CTkLabel(master=self.frame_right_name,text="Player 2",font=("Roboto Medium", int(30*self.WScale) ))  # font name and size in p
        self.p2.grid(row=1, column=0, pady=int(5*self.WScale), padx=int(10*self.WScale)) 
        self.p2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.timevar["t2"].set(self.timestr["t2"])
        self.frame_right_bank = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_right_bank.grid(row=1, column=0, sticky="nswe",padx=int(20*self.WScale), pady=int(20*self.WScale),columnspan=3)
        self.t2 = customtkinter.CTkLabel(master=self.frame_right_bank,textvariable=self.timevar["t2"],font=("Roboto Medium", int(52*self.WScale) ))  # font bank and size in p
        self.t2.grid(row=1, column=0, pady=int(5*self.WScale), padx=int(10*self.WScale)) 
        self.t2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.timevar["b2"].set(self.timestr["b2"])
        self.frame_right_time = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_right_time.grid(row=2, column=0, sticky="nswe",padx=int(20*self.WScale), pady=int(20*self.WScale),columnspan=3)
        self.b2 = customtkinter.CTkLabel(master=self.frame_right_time,textvariable=self.timevar["b2"],font=("Roboto Medium", int(42*self.WScale) ))  # font time and size in p
        self.b2.grid(row=1, column=0, pady=int(5*self.WScale), padx=int(10*self.WScale)) 
        self.b2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        #self.Start()        
        self.bind('<Return>', self.NextPlayer)        

    def NextPlayer(self,event=None):
        print(self.ap)
        self.stop = False
        self.Pause = False
        if self.ap == 1:
            self.timer = "t1"
            self.time[self.timer] = self.starttime+1
            self.timestr[self.timer] = strftime("%M:%S", gmtime(self.starttime+1))
            self.timevar[self.timer].set(self.timestr[self.timer])
            self.update_idletasks()
            self.thread = threading.Thread(target=self.Timer).start()
            self.thread2 = threading.Thread(target=self.Waiter).start()
            self.thread3 = threading.Thread(target=self.WaiterPause).start()       
        if self.ap == 2:
            self.timer = "t2"
            self.time[self.timer] = self.starttime+1
            self.timestr[self.timer] = strftime("%M:%S", gmtime(self.starttime+1))
            self.timevar[self.timer].set(self.timestr[self.timer])
            self.update_idletasks()            
            self.thread = threading.Thread(target=self.Timer).start()
            self.thread2 = threading.Thread(target=self.Waiter).start()
            self.thread3 = threading.Thread(target=self.WaiterPause).start()       

    def Waiter(self):
        while True and not self.stop:
            time.sleep(0.1)
            self.bind('<space>', self.Next)
            
    def WaiterPause(self):
        while True and not self.stop:
            time.sleep(0.1)
            self.bind('s', lambda event: self.PauseMode())
            self.bind('c', lambda event: self.RollCasualty())
            self.bind('v', lambda event: self.RollDice())
            self.bind('b', lambda event: self.RollBlock())
            self.bind('n', lambda event: self.RollDoubleBlock())
            self.bind('m', lambda event: self.Scatter())

    def RollCasualty(self,event=None):
        t = 0
        if self.Pause == False:
            self.PauseMode()
        while t < 3:
            roll = random.randint(1, 16)
            self.timevar[self.timer].set("rolling ... "+str(k))        
            self.update_idletasks()
            time.sleep(0.1)
            t += 0.1
        roll = random.randint(1, 16)
        self.timevar[self.timer].set("D16: "+str(k))        
        self.update_idletasks()
        
    def RollDice(self,event=None):
        roll = random.randint(1, 6)        
        self.timevar[self.timer].set("rolling ... ")        
        self.update_idletasks()
        time.sleep(0.1)
        self.timevar[self.timer].set("D6: "+str(roll))        
        self.update_idletasks()
        if self.Pause == False:
            self.PauseMode()

    def RollBlock(self,event=None):
        trans = {1:"Skull",2:"Both-Down",3:"Push",4:"Push",5:"Stumble",6:"Pow"}
        roll = random.randint(1, 6)
        self.timevar[self.timer].set("rolling ... ")        
        self.update_idletasks()
        time.sleep(0.1)
        self.timevar[self.timer].set(trans[roll])        
        self.update_idletasks()
        if self.Pause == False:
            self.PauseMode()
        
    def RollDoubleBlock(self,event=None):
        trans = {1:"Skull",2:"Both-Down",3:"Push",4:"Push",5:"Stumble",6:"Pow"}
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        self.timevar[self.timer].set("rolling ... ")        
        self.update_idletasks()
        time.sleep(0.1)
        self.timevar[self.timer].set(trans[r1]+" + "+trans[r2])        
        self.update_idletasks()
        if self.Pause == False:
            self.PauseMode()

    def Scatter(self,event=None):
        roll = random.randint(1, 8)
        self.timevar[self.timer].set("rolling ... ")        
        self.update_idletasks()
        time.sleep(0.1)
        self.timevar[self.timer].set("D8: "+str(roll))        
        self.update_idletasks()
        if self.Pause == False:
            self.PauseMode()
        
    def PauseMode(self,event=None):
        print("pause entered")
        if self.Pause == True:
            print("pause end")
            self.timevar[self.timer].set(self.timestr[self.timer])        
            self.update_idletasks()
            self.Pause=False
        else:
            print("pause")
            self.Pause=True

    def Next(self,event=None):
        print("Next")
        if self.ap == 1:
            self.ap = 2
            print("Next player is ",self.ap)
            self.stop = True
            time.sleep(2)
            self.NextPlayer()
        else:
            self.ap = 1
            print("Next player is ",self.ap)
            self.stop = True
            time.sleep(2)
            self.NextPlayer()

    def Countdown(self):
        print("Starting countdown")
        playsound("count.mp3")
        
    def Manage(self):
        while True and not self.stop:
            time.sleep(0.1)
        self.cd.kill()
            
    def Timer(self):
        print("timer: ",self.timer,self.time[self.timer])
        while self.time[self.timer] > 0 and not self.stop:
            print(self.time[self.timer])
            if not self.Pause:
                self.time[self.timer] -= 1
                self.timestr[self.timer] = strftime("%M:%S", gmtime(self.time[self.timer]))
                self.timevar[self.timer].set(self.timestr[self.timer])
                self.update_idletasks()
            time.sleep(1)
            if self.ap == 1:
                if self.time["b1"] < 1 or self.time["t1"]:
                    if self.time[self.timer] == 11:
                        self.cd = Process(target=self.Countdown)
                        self.cd.start()                    
                        self.cdmanage = threading.Thread(target=self.Countdown).start()                    
            if not self.ap == 1:
                if self.time["b2"] < 1  or self.time["t2"]:
                    if self.time[self.timer] == 11:
                        self.cd = Process(target=self.Countdown)
                        self.cd.start()                    
                        self.cdmanage = threading.Thread(target=self.Manage).start()                                        
                        
        if self.time[self.timer] < 1 and not self.stop:
            if self.ap == 1:
                self.timer = "b1"
            if self.ap == 2:
                self.timer = "b2"
            while self.time[self.timer] > 0 and not self.stop:
                print(self.time[self.timer])
                if not self.Pause:
                    self.time[self.timer] -= 1
                    self.timestr[self.timer] = strftime("%M:%S", gmtime(self.time[self.timer]))
                    self.timevar[self.timer].set(self.timestr[self.timer])
                    self.update_idletasks()
                time.sleep(1)
                if self.time[self.timer] == 12:
                    self.cd = Process(target=self.Countdown)
                    self.cd.start()                    
                    self.cdmanage = threading.Thread(target=self.Manage).start()                                        
            
if __name__ == "__main__":
    app = App()
    app.start()


    
