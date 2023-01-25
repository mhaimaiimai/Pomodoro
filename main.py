from tkinter import *
import time
import datetime
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TICK_MARK = "✓"

reps=0
timer_working=False
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def timer_reset():
    global reps, timer_working
    canvas.itemconfig(timer_display, text=f"00:00")
    title_lbl.config(text="Timer", fg=GREEN)
    tick_lbl.config(text="")
    reps = 0
    timer_working = False
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def timer_start():
    global timer_working, reps
    if not timer_working:
        timer_working = True
        reps +=1
        work_total_sec = 60 * WORK_MIN
        short_total_sec = 60 * SHORT_BREAK_MIN
        long_total_sec = 60 * LONG_BREAK_MIN
        
        if reps%8==0:
            title_lbl.config(text="Break", fg=RED)
            update_tick()
            count_down(long_total_sec)
        elif reps%2==0:
            title_lbl.config(text="Break", fg=PINK)
            update_tick()
            count_down(short_total_sec)
        else:
            title_lbl.config(text="Work", fg=GREEN)
            count_down(work_total_sec)
    else:
        pass
            
def update_time(sec):
    [timer_min, timer_sec] = divmod(sec,60)
    canvas.itemconfig(timer_display, text=f"{timer_min}:{timer_sec:02d}")
    
def update_tick():
    text_val = tick_lbl["text"] + TICK_MARK
    tick_lbl.config(text=f"{text_val}")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    if(count>0):
        update_time(count)
        global timer
        timer = window.after(1000, count_down, count-1)
    else: 
        timer_start()
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=210, height=234, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(106,118, image=tomato_img)
timer_display = canvas.create_text(106,134,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

title_lbl = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40), bg=YELLOW)
title_lbl.grid(row=0, column=1)

start_btn = Button(text="Start", command=timer_start, bg="white", highlightbackground=YELLOW)
start_btn.grid(row=2, column=0)

reset_btn = Button(text="Reset", command=timer_reset, bg="white", highlightbackground=YELLOW)
reset_btn.grid(row=2, column=2)

tick_lbl = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME,20))
tick_lbl.grid(row=3, column=1)

window.mainloop()