from tkinter import Canvas, Frame, Tk
import random
import tkinter
from tkinter.constants import BOTTOM, CENTER, LEFT, NE, NSEW, NW, RIGHT, TOP
import time


class Algorithm_Visualizer():
    def __init__(self, master):
        self.root = master
        self.control_frame = Frame(master)
        self.control_frame.pack(side=TOP, pady=5, padx=5, anchor=NE)
        self.visual_frame = Frame(master)
        self.visual_frame.pack(side=BOTTOM, pady=5)
        self.random_set = []
        self.set_size = tkinter.IntVar(value=10)
        self.max_range = 300
        self.create_widgets()
        self.create_canvas()

    def create_widgets(self):
        self.set_size_scaler = tkinter.Scale(
            self.control_frame, from_=10, to=70, orient=tkinter.HORIZONTAL)
        self.set_size_scaler.set(value=self.set_size.get())
        self.set_size_scaler.pack(side=RIGHT, pady=0)

        self.random_btn = tkinter.Button(
            self.control_frame, text='Reset | Random Set', command=self.generate_random_set)
        self.random_btn.pack(side=RIGHT, pady=0)

        self.bubble_sort_btn = tkinter.Button(
            self.control_frame, text='Bubble Sort', command=self.bubble_sort)
        self.bubble_sort_btn.pack(side=LEFT, pady=0)

    def create_canvas(self):
        self.canvas = Canvas(self.visual_frame, width=700)
        self.canvas.pack(padx=10)

    def draw_columns(self):
        self.canvas.delete("all")
        self.column_width = 700//self.set_size.get()
        for index, value in enumerate(self.random_set):
            x_0 = (index)*self.column_width
            x_1 = (index+1)*self.column_width
            self.canvas.create_rectangle(
                x_0, 0, x_1, value, fill="yellow", tags=str(value))

    def generate_random_set(self):
        self.set_size.set(self.set_size_scaler.get())

        if len(self.random_set) > 0 and self.set_size.get() == len(self.random_set):
            random.shuffle(self.random_set)
        else:
            self.random_set = random.sample(
                range(self.max_range), self.set_size.get())

        self.draw_columns()

    def bubble_sort(self):
        swap = True
        while swap:
            swap = False
            for index in range(len(self.random_set)-1):
                curr_item = self.random_set[index]
                next_item = self.random_set[index+1]
                self.bubble_color_rect(curr_item, next_item)
                if next_item < curr_item:
                    self.random_set[index], self.random_set[index +
                                                            1] = next_item, curr_item
                    swap = True

                time.sleep(0.1)

    def bubble_color_rect(self, tag1, tag2):
        self.canvas.itemconfig(str(tag1), fill='red')
        self.canvas.itemconfig(str(tag2), fill='blue')

    def switch_columns_location(self, tag1, tag2):
        self.canvas.move(str(tag1), -self.column_width, 0)
        self.canvas.move(str(tag2), self.column_width, 0)

    def bubble_reset_color(self, tag1, tag2):
        self.canvas.itemconfig(str(tag1), fill='yellow')
        self.canvas.itemconfig(str(tag2), fill='yellow')


root = Tk()
root.title('Sorting Algorithms Visualizer')
root.geometry('700x500')
root.iconbitmap('./python_103279.ico')


visualizer = Algorithm_Visualizer(root)
root.mainloop()
