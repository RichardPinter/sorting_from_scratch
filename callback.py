from functools import partial
import panel as pn
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from numpy import random
from bokeh.models import Button, ColumnDataSource, Select, MultiSelect, Slider, CustomJS
from minheap import MinHeap



### Callback for  selection the sorting algorithm ###
def select_sorting_callback(data_cbs, attr, old, new):
    data_cbs.data["sorting_alg"] = [new]

##### Helper functions for the main function #####
###  Bubble Sort

bubble_sort_h = 1
bubble_sort_j = 0
sorted = 0


def bubble_sort(arr):
    global bubble_sort_h, bubble_sort_j
    if bubble_sort_h < len(arr):
        if bubble_sort_j < len(arr) - bubble_sort_h:
            if arr[bubble_sort_j + 1] < arr[bubble_sort_j]:
                arr[bubble_sort_j + 1], arr[bubble_sort_j] = (
                    arr[bubble_sort_j],
                    arr[bubble_sort_j + 1],
                )
            bubble_sort_j += 1
    return arr.copy()


def bubble_sort_callback(data_cbs, source):
    global bubble_sort_h, bubble_sort_j, sorted

    arr = source.data["arr"]
    size = data_cbs.data["size"][0]
    source.data["arr"] = bubble_sort(arr)
    color = [
        "red" if bubble_sort_j != index and bubble_sort_j + 1 != index else ("blue")
        for index in range(size)
    ]
    if sorted > 0:
        for i in range(sorted):
            color[-i - 1] = "green"
    source.data["color"] = color
    if bubble_sort_j == len(arr) - bubble_sort_h:
        source.data["color"] = [
            "red" if bubble_sort_j > index else "green" for index in range(size)
        ]
        bubble_sort_j = 0
        bubble_sort_h += 1
        sorted += 1


###  Insertion Sort

insertion_sort_i = 1
insertion_sort_j = insertion_sort_i
insertion_flag = False


def insertion_sort(arr):
    global insertion_sort_i, insertion_sort_j
    n = len(arr)
    if insertion_sort_i < n:
        if insertion_sort_j > 0 and arr[insertion_sort_j - 1] > arr[insertion_sort_j]:
            arr[insertion_sort_j - 1], arr[insertion_sort_j] = (
                arr[insertion_sort_j],
                arr[insertion_sort_j - 1],
            )
        insertion_sort_j -= 1
    return arr.copy()


def insertion_sort_callback(data_cbs, source):
    global insertion_sort_i, insertion_sort_j, insertion_flag
    arr = source.data["arr"]
    size = data_cbs.data["size"][0]
    source.data["arr"] = insertion_sort(arr)
    color = ["red" for index in range(size)]
    n = len(arr)
    if insertion_sort_j < n - 1:
        color[insertion_sort_j] = "blue"
        if insertion_sort_j > 0:
            color[insertion_sort_j - 1] = "blue"
    source.data["color"] = color
    if insertion_sort_i < n - 1:
        if insertion_sort_j == 0:
            insertion_sort_i += 1
            insertion_sort_j = insertion_sort_i
            for i in range(insertion_sort_j):
                color[i] = "green"
            source.data["color"] = color
            insertion_flag = True
    if insertion_flag == True:
        if insertion_sort_j < n:
            color[insertion_sort_j] = "blue"
            if insertion_sort_j > 0:
                color[insertion_sort_j - 1] = "blue"
            source.data["color"] = color
        insertion_flag = False


### Main Selection sort algorithm
selection_sort_i = 0
selection_sort_min_pos = 0
selection_sort_curr_pos = 0
selection_sort_minimum = 20
selection_presorted = 0
selection_bool = False


def selection_sort(arr):
    global selection_sort_i, selection_sort_min_pos, selection_sort_curr_pos, selection_sort_minimum

    if selection_sort_i < len(arr):
        if selection_sort_curr_pos < len(arr):
            print(selection_sort_curr_pos,selection_sort_minimum)
            if arr[selection_sort_curr_pos] < selection_sort_minimum:
                selection_sort_minimum = arr[selection_sort_curr_pos]
                selection_sort_min_pos = selection_sort_curr_pos
            selection_sort_curr_pos += 1
        if selection_sort_curr_pos == len(arr):
            arr[selection_sort_i], arr[selection_sort_min_pos] = (
                arr[selection_sort_min_pos],
                arr[selection_sort_i],
            )
    return arr.copy()


def selection_sort_callback(data_cbs, source):
    ## Selection sort
    global selection_sort_i, selection_sort_min_pos, selection_sort_curr_pos, selection_sort_minimum, selection_presorted, \
        selection_bool
    arr = source.data["arr"]
    size = data_cbs.data["size"][0]
    if selection_bool == False:
        source.data["arr"] = selection_sort(arr)
        color = [
            "red" if selection_sort_curr_pos != index else "black"
            for index in range(size)
        ]
        for i in range(selection_presorted):
            color[i] = "green"
        color[selection_sort_i] = "blue"
        color[selection_sort_min_pos] = "green"
        source.data["color"] = color
        if selection_sort_curr_pos == len(arr):
            if selection_sort_i < len(arr) - 1:
                selection_sort_i += 1
                selection_sort_curr_pos = selection_sort_i
                selection_sort_minimum = arr[selection_sort_i]
                selection_sort_min_pos = selection_sort_i
                selection_presorted += 1
                print(selection_presorted)
            else:
                if selection_bool == False:
                    print("finsihed")
                    for i in range(selection_presorted):
                        color = ["green" for _ in range(size)]
                    source.data["color"] = color
                    selection_bool = True
                else:
                    pass


### Main heap sort algorithm
removed = []
def heap_sort_callback(data_cbs, source,heap):
    global removed
    size = data_cbs.data["size"][0]
    if heap.heap:
        min = heap.remove()
        removed.append(min)
        llist = heap.heap.copy()
        llist.extend(removed)
        source.data['arr'] = llist
        color = ['red'] * size
        for i in range(len(removed)):
            color[len(color)-1-i]='green'
        source.data['color'] = color

def query_callback(data_cbs, tabs,flag, event):
    print('hey)')
    if data_cbs.data["sorting_alg"][0] != "-":
        print('works')
        speed = data_cbs.data["speed"][0]
        size = data_cbs.data["size"][0]
        print(size,'This is size of the data')
        arr = [i + 1 for i in range(size)]
        random.shuffle(arr)
        index = [i for i in range(size)]
        color = ["red" for _ in range(size)]
        source = ColumnDataSource(dict(index=index, arr=arr, color=color))
        data_cbs.data["source"][0] = source
        ### Visualisation basics
        f = figure(height = 800, width = 1600)
        f.vbar(x="index", top="arr", fill_color="color", source=source)
        tabs[0].append(
            pn.Column(
                f,
            )
        )
        if data_cbs.data["sorting_alg"][0] == "bubble_sort":
            callback =  partial(bubble_sort_callback, data_cbs, source)
        elif data_cbs.data["sorting_alg"][0] == "insertion_sort":
            callback = partial(insertion_sort_callback, data_cbs, source)
        elif data_cbs.data["sorting_alg"][0] == "selection_sort":
            callback =  partial(selection_sort_callback, data_cbs, source)
        elif data_cbs.data["sorting_alg"][0] == "heap_sort":
            heap = MinHeap(arr, color)
            callback =  partial(heap_sort_callback, data_cbs, source, heap)

        this = pn.state.add_periodic_callback(
           callback, period=speed,count= 3
        )
        flag = data_cbs.data["flag"][0]
        if flag == True:
            # print(dir(pn.state))
            # pn.state.add_periodic_callback(
            #     callback,  count=, period=speed
            # )
            data_cbs.data["flag"][0] = False



bubble_sort_h = 1
bubble_sort_j = 0
sorted = 0
def query_reset(data_cbs,tabs,flag,event):
    global bubble_sort_h, bubble_sort_j,sorted
    data_dict = {
        "sorting_alg": ['-'],
        "speed": [100],
        "size": [100],
        'flag': [True],
        'source': ['-']
    }

    options = ['-','bubble_sort', 'selection_sort','insertion_sort','heap_sort']

    data_cbs.data = data_dict
    tabs[0].pop(-1)
    print('hey')

    select_sorting = Select(name="Select sorting algorithm", options=options)
    select_sorting.on_change('value', partial(select_sorting_callback, data_cbs))
    speed = data_cbs.data["speed"][0]
    print(speed)
    size = data_cbs.data["size"][0]
    arr = [i + 1 for i in range(size)]
    random.shuffle(arr)
    index = [i for i in range(size)]
    color = ["red" for _ in range(size)]
    print('why',data_cbs.data)
    source = ColumnDataSource(dict(index=index, arr=arr, color=color))
    data_cbs.data["source"][0] = source
    tabs[0][0][1] = select_sorting
    data_cbs.data["flag"][0] = True