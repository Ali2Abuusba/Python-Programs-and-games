from tkinter import *
from tkinter import messagebox
import time
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
FROG_SIZE = 64
number_frogs = 1
no_frogs = True

class Ground:

    def __init__(self):
        canvas.create_rectangle(0, 0, GAME_WIDTH, GAME_HEIGHT, fill="#24870c", tag="ground")

class Frog:

    def __init__(self):
        x = random.randint(0, int(GAME_WIDTH / FROG_SIZE) - 1) * FROG_SIZE
        y = random.randint(0, int(GAME_HEIGHT / FROG_SIZE) - 1) * FROG_SIZE

        self.coordinates = [x, y]

        canvas.create_image(x, y, image=frog_photo, tag="frog")


def start_game(event):

    canvas.delete("ground")

    x, y = frog.coordinates

    x_event = event.x
    y_event = event.y

    if x_event + 32 >= x >= x_event - 32 and y_event + 32 >= y >= y_event - 32:
        canvas.delete("frog")
        #del frog.coordinates[x, y]
        #frog = Frog()
    timer()


def next_level():
    pass


def timer():
    sec = int(second.get())

    while sec > -1:
        second.set(sec)

        # updating the GUI window after decrementing the
        # temp value every time
        window.update()
        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message: "lets go"
        if sec == 0:
            messagebox.showinfo("Time Countdown",
                                "Time is out, and unfortunately there are still frogs ")

        # after one sec the value of temp will be decremented
        # by one
        sec -= 1


window = Tk()

window.title("Frog Game")
window.resizable(False, False)

frog_icon = PhotoImage(file='frog_icon.png')
window.iconphoto(True, frog_icon)

Level = StringVar()
Level.set(" 1 ")

second = StringVar()
second.set(" 4 ")

frog_photo = PhotoImage(file='frog.png')



start_button = Button(window, text='Start', bd='5', font=("consoles", 40),
                      activeforeground='red', command=start_game)
start_button.pack(side='bottom')

secondLabel = Label(window, width=2, font=("Arial", 40, ""), bg="black"
                    , fg="white", textvariable=second)
secondLabel.pack()

canvas = Canvas(window, bg="#24870c", height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

manyFrogsLabel = Label(window, text=' Level ', fg="blue", font=('consoles', 50))
manyFrogsLabel.place(x=0, y=790)

manyFrogsLabel = Label(window, width=2, textvariable=Level, font=('consoles', 50))
manyFrogsLabel.place(x=180, y=790)

window.bind("<Button-1>", start_game)

window.update()

game_width = window.winfo_width()
game_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

X = int((screen_width / 2) - (game_width / 2))
Y = int((screen_height / 2) - (game_height / 2))

window.geometry(f'{game_width}x{game_height}+{X}+{Y}')

frog = Frog()
ground = Ground()

window.mainloop()
