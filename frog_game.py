from tkinter import *
from tkinter import messagebox
import time
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
# FROG_SIZE = random.randint(32, 64)
number_frogs = 1
no_frogs = True


class Ground:

    def __init__(self):
        canvas.create_rectangle(0, 0, GAME_WIDTH, GAME_HEIGHT, fill="#24870c", tag="ground")


class Frog:

    def __init__(self):
        self.FROG_SIZE = random.randint(32, 64)
        self.num_frogs = 0
        self.coordinates = []

        for i in range(0, level):
            self.coordinates.append([0, 0])

        for j in range(0, level):
            x = int(random.randint(0, int(GAME_WIDTH / 64) + 1) * self.FROG_SIZE)
            y = int(random.randint(0, int(GAME_HEIGHT / 64) + 1) * self.FROG_SIZE)
            self.coordinates[j] = [x, y]
            canvas.create_image(x, y, image=frog_photo, tag=f"frog{j}")
            window.update()
            self.num_frogs += 1


def start():
    canvas.delete("ground")
    window.update()
    timer(frog)


def check_click_on_frog(frog):
    global level

    for i in range(level):
        if frog.num_frogs != 0:
            x, y = frog.coordinates[i]

            if x_event + 32 >= x >= x_event - 32 and y_event + 32 >= y >= y_event - 32:
                canvas.delete(f"frog{i}")
                window.update()
                frog.coordinates[i] = [-1, -1]
                frog.num_frogs -= 1


def timer(frog):
    sec = int(second.get())

    while sec > -1:
        second.set(sec)
        # updating the GUI window after decrementing the
        # temp value every time
        # window.update()
        time.sleep(1)
        window.update()

        check_click_on_frog(frog)
        window.update()
        # when temp value = 0; then a messagebox pop's up
        # with a message: "lets go"
        if sec == 0:
            canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2,
                               font=('consolas', 100), text="GAME OVER", fill="red", tag="gameover")
        elif frog.num_frogs == 0:
            next_level(frog)

        # after one sec the value of temp will be decremented
        # by one
        sec -= 1


def next_level(frog):
    global level

    level += 1
    Level.set(level)
    second.set(level)
    frog = Frog()
    window.update()
    timer(frog)


def mouse_click(event):
    global x_event
    global y_event

    x_event = event.x
    y_event = event.y


window = Tk()

window.title("Frog Game")
window.resizable(False, False)

frog_icon = PhotoImage(file='frog_icon.png')
window.iconphoto(True, frog_icon)

Level = StringVar()
Level.set("1")
level = 1

second = StringVar()
second.set("1")

x_event = 0
y_event = 0

frog_photo = PhotoImage(file='frog.png')

start_button = Button(window, text='Start', bd='5', bg="green", font=("consoles", 40),
                      activeforeground='red', command=start)
start_button.pack(side='bottom')

secondLabel = Label(window, width=2, font=("Arial", 40, ""), bg="black"
                    , fg="white", textvariable=second)
secondLabel.pack()

canvas = Canvas(window, bg="#24870c", height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

level_Label = Label(window, text=' Level ', fg="blue", font=('consoles', 50))
level_Label.place(x=0, y=790)

level_Label = Label(window, width=2, textvariable=Level, font=('consoles', 50))
level_Label.place(x=180, y=790)

window.update()

game_width = window.winfo_width()
game_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

X = int((screen_width / 2) - (game_width / 2))
Y = int((screen_height / 2) - (game_height / 2))

window.geometry(f'{game_width}x{game_height}+{X}+{Y}')

window.bind("<Button-1>", mouse_click)

frog = Frog()
ground = Ground()

window.mainloop()
