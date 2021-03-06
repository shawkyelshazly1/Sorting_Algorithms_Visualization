from tkinter import Canvas, Frame, Tk
import random
import tkinter
from tkinter.constants import BOTTOM, CENTER, LEFT, NE, NSEW, NW, RIGHT, TOP
import time
from typing import Text


class Algorithm_Visualizer():
    def __init__(self, master):
        self.root = master
        self.control_frame = Frame(master)
        self.control_frame.pack(side=TOP, pady=5, padx=5, anchor=NE)
        self.visual_frame = Frame(master)
        self.visual_frame.pack(pady=25)
        self.random_set = []
        self.colors = []
        self.font_colors = []
        self.set_size = tkinter.IntVar(value=10)
        self.max_range = 470
        self.create_widgets()
        self.create_canvas()
        self.visual_speed = tkinter.DoubleVar(value=0.2)

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

        self.selection_sort_btn = tkinter.Button(
            self.control_frame, text='Selection Sort', command=self.selection_sort)
        self.selection_sort_btn.pack(side=LEFT, pady=0)

        self.merge_sort_btn = tkinter.Button(
            self.control_frame, text='Merge Sort', command=lambda: self.mergeSort(self.random_set, 0, self.set_size.get()-1))
        self.merge_sort_btn.pack(side=LEFT, pady=0)

    def create_canvas(self):
        self.canvas = Canvas(self.visual_frame, width=700, height=500)
        self.canvas.pack(padx=10)

    def draw_columns(self):
        self.canvas.delete("all")
        self.column_width = 700//self.set_size.get()
        for index, value in enumerate(self.random_set):
            x_0 = (index)*self.column_width
            x_1 = (index+1)*self.column_width
            self.canvas.create_rectangle(
                x_0, 0, x_1, value, fill=self.colors[index])
            self.canvas.create_text(
                (x_0+x_1)/2, value/2, text=str(value), font='arial 10 bold', fill=self.font_colors[index])

        self.root.update_idletasks()

    def generate_random_set(self):
        self.set_size.set(self.set_size_scaler.get())

        if len(self.random_set) > 0 and self.set_size.get() == len(self.random_set):
            random.shuffle(self.random_set)
        else:
            self.random_set = random.sample(
                range(10, self.max_range), self.set_size.get())

        self.colors = ['yellow' for i in range(self.set_size.get())]
        self.font_colors = ['#000' for i in range(self.set_size.get())]

        self.draw_columns()

    def bubble_sort(self):
        self.disable_controls()
        swap = True
        while swap:
            time.sleep(self.visual_speed.get())
            swap = False
            for index in range(len(self.random_set)-1):
                curr_item = self.random_set[index]
                next_item = self.random_set[index+1]
                self.colors[index] = 'red'
                self.colors[index+1] = 'blue'
                self.font_colors[index] = 'white'
                self.font_colors[index+1] = 'white'
                self.draw_columns()
                time.sleep(self.visual_speed.get())
                if next_item < curr_item:
                    self.random_set[index], self.random_set[index +
                                                            1] = next_item, curr_item
                    self.colors[index], self.colors[index +
                                                    1] = self.colors[index+1], self.colors[index]
                    swap = True
                    self.draw_columns()
                    time.sleep(self.visual_speed.get())

                self.colors[index] = 'yellow'
                self.colors[index+1] = 'yellow'
                self.font_colors[index] = '#000'
                self.font_colors[index+1] = '#000'
                self.draw_columns()
                time.sleep(self.visual_speed.get())

        self.disable_controls()

    def selection_sort(self):
        self.disable_controls()
        pointer = 0
        while pointer != len(self.random_set):
            for index in range(pointer, len(self.random_set)):
                self.colors[index] = 'red'
                self.colors[pointer] = 'blue'
                self.font_colors[index] = 'white'
                self.font_colors[pointer] = 'white'
                self.draw_columns()
                time.sleep(self.visual_speed.get())
                if self.random_set[index] < self.random_set[pointer]:
                    self.random_set[pointer], self.random_set[index] = self.random_set[index], self.random_set[pointer]
                    self.colors[index], self.colors[pointer] = self.colors[pointer], self.colors[index]
                    self.draw_columns()
                    time.sleep(self.visual_speed.get())

                self.colors[index] = 'yellow'
                self.colors[pointer] = 'yellow'
                self.font_colors[index] = '#000'
                self.font_colors[pointer] = '#000'
                self.draw_columns()
                time.sleep(self.visual_speed.get())
            pointer += 1

        self.disable_controls()

    def merge(self, arr, start, mid, end):

        start2 = mid + 1

        # If the direct merge is already sorted
        if (arr[mid] <= arr[start2]):
            return

        # Two pointers to maintain start
        # of both arrays to merge
        while (start <= mid and start2 <= end):

            # If element 1 is in right place
            if (arr[start] <= arr[start2]):
                self.colors[start] = 'red'
                self.colors[start2] = 'blue'
                self.draw_columns()
                time.sleep(self.visual_speed.get())
                self.colors[start] = 'yellow'
                self.colors[start2] = 'yellow'
                start += 1
                self.draw_columns()
                time.sleep(self.visual_speed.get())
            else:
                value = arr[start2]
                index = start2

                # Shift all the elements between element 1
                # element 2, right by 1.
                while (index != start):
                    self.draw_columns()
                    time.sleep(self.visual_speed.get())
                    self.colors[index] = 'red'
                    self.colors[index-1] = 'blue'
                    arr[index] = arr[index - 1]
                    self.draw_columns()
                    time.sleep(self.visual_speed.get())
                    self.colors[index] = 'yellow'
                    self.colors[index-1] = 'yellow'
                    index -= 1

                arr[start] = value
                self.draw_columns()
                time.sleep(self.visual_speed.get())
                # Update all the pointers
                start += 1
                mid += 1
                start2 += 1

    def mergeSort(self, arr, l, r):
        self.disable_controls()
        if (l < r):

            # Same as (l + r) / 2, but avoids overflow
            # for large l and r
            m = l + (r - l) // 2

            # Sort first and second halves
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            self.draw_columns()
            time.sleep(self.visual_speed.get())
            self.merge(arr, l, m, r)
        self.disable_controls()

    def disable_controls(self):
        if self.set_size_scaler['state'] == 'normal' and self.random_btn['state'] == 'normal' and self.bubble_sort_btn['state'] == 'normal':
            self.set_size_scaler['state'] = 'disabled'
            self.random_btn['state'] = 'disabled'
            self.bubble_sort_btn['state'] = 'disabled'
            self.selection_sort_btn['state'] = 'disabled'
            self.merge_sort_btn['state'] = 'disabled'
        else:
            self.set_size_scaler['state'] = 'normal'
            self.random_btn['state'] = 'normal'
            self.bubble_sort_btn['state'] = 'normal'
            self.selection_sort_btn['state'] = 'normal'
            self.merge_sort_btn['state'] = 'normal'


root = Tk()
root.title('Sorting Algorithms Visualizer')
root.geometry('700x500')
root.iconbitmap('./python_103279.ico')

visualizer = Algorithm_Visualizer(root)
root.mainloop()
