import threading
import time
import tkinter as tk
from wintoast import ToastNotifier
from playsound import playsound


class CountdownTimer:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('420x220')
        self.root.title('Timer')
        self.root.resizable(False, False)

        self.time_entry = tk.Entry(self.root, font=('Calibri', 30))
        self.time_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.start_button = tk.Button(self.root, width='5', font=('Calibri', 30), text='Start', command=self.start_thread)
        self.start_button.place(x=5, y=70)
        # self.start_button.grid(row=1, column=0, padx=5, pady=5)

        self.stop_button = tk.Button(self.root, width='5', font=('Calibri', 30), text='Stop', command=self.stop)
        self.stop_button.place(x=300, y=70)

        self.time_label = tk.Label(self.root, font=('Calibri', 30), text='Time: 00:00:00')
        self.time_label.place(x=80, y=160)

        self.stop_loop = False

     
        self.root.mainloop()
    
    def start_thread(self):
        threader = threading.Thread(target=self.start)
        threader.start()

    def start(self):
        self.stop_loop = False

        hours, minutes, seconds = 0, 0, 0
        string_split = self.time_entry.get().split(":")
        if len(string_split) == 3:
            hours = int(string_split[0])
            minutes = int(string_split[1])
            seconds = int(string_split[2])
        elif len(string_split) == 2:
            minutes = int(string_split[0])
            seconds = int(string_split[1])
        elif len(string_split) == 1:
            seconds = int(string_split[0])
        else:
            print('Invalid Entry Format')
            return

        full_seconds = hours * 3600 + minutes * 60 + seconds

        while full_seconds > 0 and not self.stop_loop:
            full_seconds -= 1

            minutes, secpnds = divmod(full_seconds, 60)
            hours, minutes = divmod(minutes, 60)
        
            self.time_label.config(text=f"Time: {hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)

        if not self.stop_loop:
            toaster = ToastNotifier()
            toaster.show_toast("Timer", "Time's Up!", duration=10)
            playsound("alarm.mp3")
    def stop(self):
        self.stop_loop = True
        self.time_label.config(text='Text: 00:00:00')

CountdownTimer()