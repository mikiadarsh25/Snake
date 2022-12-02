from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
watch = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    timer.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    tick.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(watch)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(short_break)
    elif reps % 8 == 0:
        timer.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN)
    else:
        timer.config(text="Working", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global watch
        watch = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        working_session = math.floor(reps / 2)
        for _ in range(working_session):
            mark += "✔"
        tick.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer.grid(column=1, row=0)

tick = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
tick.grid(column=1, row=3)

start = Button(text="Start", command=start_timer, highlightthickness=0)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(row=2, column=2)

window.mainloop()
