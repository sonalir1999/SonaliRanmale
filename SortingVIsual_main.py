from tkinter import *
from tkinter import ttk
import random

# We need the time module to create some time difference between each comparison
import time
# Importing algorithms

DARK_GRAY = '#65696B'
LIGHT_GRAY = '#C4C5BF'
BLUE = '#0CA8F6'
DARK_BLUE = '#4204CC'
WHITE = '#FFFFFF'
BLACK = '#000000'
RED = '#F22810'
YELLOW = '#F7E806'
PINK = '#F50BED'
LIGHT_GREEN = '#05F50E'
PURPLE = '#BF01FB'
# Main window
window = Tk()
window.title("Sorting Algorithms Visualization")
window.maxsize(1000, 700)
window.config(bg=WHITE)

algorithm_name = StringVar()
algo_list = ['Bubble Sort', 'Merge Sort', 'Selection Sort']

speed_name = StringVar()
speed_list = ['Fast', 'Medium', 'Slow']

data = []

# This function will draw randomly generated list data[] on the canvas as vertical bars


def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 2
    spacing = 4
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()

# This function will generate array with random values every time we hit the generate button


def generate():
    global data

    data = []
    for i in range(0, 10):
        random_value = random.randint(1, 150)
        data.append(random_value)
    print(data)
    drawData(data, [BLUE for x in range(len(data))])

# This function will set sorting speed


def set_speed():
    if speed_menu.get() == 'Slow':
        return 1
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001

# This funciton will trigger a selected algorithm and start sorting


def sort():
    global data
    timeTick = set_speed()

    if algo_menu.get() == 'Bubble Sort':
        bubble_sort(data, drawData, timeTick)

    elif algo_menu.get() == 'Merge Sort':
        merge_sort(data, 0, len(data)-1, drawData, timeTick)

    elif algo_menu.get() == 'Selection Sort':
        ##print('sonali before sorting', data)
        selection_sort(data, drawData, timeTick)
        ##print('after sorting data', data)


def bubble_sort(data, drawData, timeTick):
    size = len(data)
    for i in range(size-1):
        for j in range(size-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, [YELLOW if x == j or x == j +
                         1 else BLUE for x in range(len(data))])
                time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])


def selection_sort(data, drawData, timeTick):
    size = len(data)
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            #drawData(data, [RED for min_index in range(len(data))])
            # time.sleep(timeTick)
            # select the minimum element in every iteration
            # drawData(data, [PINK if data[x] == data[j] or data[x] == data[min_index]
            #               else BLUE for x in range(len(data))])
            if data[j] < data[min_index]:
                min_index = j

            drawData(data, [PINK if data[x] == data[j] or data[x] == data[min_index]
                            else BLUE for x in range(len(data))])
            time.sleep(timeTick)
         # swapping the elements to sort the array

        # time.sleep(timeTick)
        (data[ind], data[min_index]) = (data[min_index], data[ind])
        drawData(data, [BLUE for x in range(len(data))])


def merge(data, start, mid, end, drawData, timeTick):
    p = start
    q = mid + 1
    tempArray = []

    for i in range(start, end+1):
        if p > mid:
            tempArray.append(data[q])
            q += 1
        elif q > end:
            tempArray.append(data[p])
            p += 1
        elif data[p] < data[q]:
            tempArray.append(data[p])
            p += 1
        else:
            tempArray.append(data[q])
            q += 1

    for p in range(len(tempArray)):
        data[start] = tempArray[p]
        start += 1


def merge_sort(data, start, end, drawData, timeTick):
    if start < end:
        mid = int((start + end) / 2)
        merge_sort(data, start, mid, drawData, timeTick)
        merge_sort(data, mid+1, end, drawData, timeTick)

        merge(data, start, mid, end, drawData, timeTick)

        drawData(data, [PURPLE if x >= start and x < mid else YELLOW if x == mid
                        else DARK_BLUE if x > mid and x <= end else BLUE for x in range(len(data))])
        time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])


    ### User interface here ###
UI_frame = Frame(window, width=900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown to select sorting algorithm
l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(
    UI_frame, textvariable=algorithm_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# dropdown to select sorting speed
l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# sort button
b1 = Button(UI_frame, text="Sort", command=sort, bg=LIGHT_GRAY)
b1.grid(row=2, column=1, padx=5, pady=5)

# button for generating array
b3 = Button(UI_frame, text="Generate Array", command=generate, bg=LIGHT_GRAY)
b3.grid(row=2, column=0, padx=5, pady=5)

# canvas to draw our array
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)


window.mainloop()
