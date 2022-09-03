from functools import partial

import numpy as np
from bokeh.layouts import column, row
from bokeh.models import Button, ColumnDataSource, Slider
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc
from numpy import random
import time
from bokeh.models.widgets import Select
import panel as pn
### Creating the data

data_dict = {
    "sorting_alg": ['-'],
    "speed": [2],
    "size": [2],
}
data_cbs = ColumnDataSource(data_dict)


size = data_cbs.data['size'][0]
arr = random.randint(20, size=size)
index = [i for i in range(size)]
color = ['red' for _ in range(size)]
source = ColumnDataSource(dict(index=index,arr=arr,color=color))
h = 1
j= 0
sorted = 0
### Visualisation basics
f = figure()
f.vbar(x='index', top='arr', fill_color = 'color', source=source)


### Pre-selection

### Main bubble-sort algorithm
def bubble_sort(arr):
    global h,j,llist
    if h< len(arr):
        if j < len(arr)-h:
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j+=1
    return arr.copy()




### Main Selection sort algorithm
selection_sort_i = 0
selection_sort_min_pos = 0
selection_sort_curr_pos = 0
selection_sort_minimum = arr[0]
selection_presorted = 1
selection_bool = False
def selection_sort(arr):
    global selection_sort_i,selection_sort_min_pos,selection_sort_curr_pos,selection_sort_minimum


    if selection_sort_i < len(arr):
        if selection_sort_curr_pos < len(arr):

            if arr[selection_sort_curr_pos] < selection_sort_minimum:
                selection_sort_minimum = arr[selection_sort_curr_pos]
                selection_sort_min_pos = selection_sort_curr_pos
            selection_sort_curr_pos+=1
        if selection_sort_curr_pos== len(arr):
            arr[selection_sort_i], arr[selection_sort_min_pos] = arr[selection_sort_min_pos], arr[selection_sort_i]
    return arr.copy()




### Main insertion sort alogirhtm
insertion_sort_i = 1
insertion_sort_j = insertion_sort_i
n = len(arr)
insertion_flag = False

def insertion_sort(arr):
    global insertion_sort_i,insertion_sort_j,n
    if insertion_sort_i < n:
        if insertion_sort_j>0 and arr[insertion_sort_j-1] > arr[insertion_sort_j]:
            arr[insertion_sort_j-1], arr[insertion_sort_j] = arr[insertion_sort_j], arr[insertion_sort_j-1]
        insertion_sort_j-=1
    return arr.copy()


### Sorting algoirhtm button
sorting_list = ['-','bubble_sort', 'selection_sort','insertion_sort']
sorting = ['']
sortin_source = ColumnDataSource(dict(sorting=sorting, arr = arr))
select = Select(title="monthly csv-s", options=sorting_list)

### Set size button

def slider_callback(attr,old,new):
    global source
    index = [i for i in range(new)]
    color = ['red' for _ in range(new)]
    arr = random.randint(100, size=new)
    source.data = ColumnDataSource(dict(index=index,arr=arr,color=color)).data

slider  = Slider(start = 10, end = 1000, value = 0, title = ' Set the size of the array')
slider.on_change('value',slider_callback)


def update_sort(attr, old, new):
    global sortin_source
    sortin_source.data['sorting'] = [select.value]


select.on_change('value', update_sort)


### Updating bubble-sort algorithm
def callback():

    global sortin_source,arr


    if sortin_source.data['sorting'][0] == 'bubble-sort':
        print('bubble-srtt hey')
        ## Bubble sort
        global h, j, sorted
        source.data['arr'] = bubble_sort(arr)
        color = ['red' if j != index and j + 1 != index else ('blue') for index in range(size)]
        if sorted > 0:
            for i in range(sorted):
                color[-i - 1] = 'green'
        source.data['color'] = color
        if j == len(arr) - h:
            source.data['color'] = ['red' if j > index else 'green' for index in range(size)]
            j = 0
            h += 1
            sorted += 1

    elif sortin_source.data['sorting'][0] == 'selection-sort':

        ## Selection sort
        global selection_sort_i, selection_sort_min_pos, selection_sort_curr_pos, selection_sort_minimum, selection_presorted, selection_bool
        if selection_bool == False:
            source.data['arr'] = selection_sort(arr)
            color = ['red' if selection_sort_curr_pos != index else 'black' for index in range(size)]
            for i in range(selection_presorted):
                color[i] = 'pink'
            color[selection_sort_i] = 'blue'
            color[selection_sort_min_pos] = 'green'
            source.data['color'] = color
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
                        print('finsihed')
                        for i in range(selection_presorted):
                            color = ['pink' for _ in range(size)]
                        source.data['color'] = color
                        selection_bool = True
                    else:
                        pass

    elif sortin_source.data['sorting'][0] == 'insertion_sort':
        ### Insertion sort
        global insertion_sort_i, insertion_sort_j, n, insertion_flag

        source.data['arr'] = insertion_sort(arr)
        color = ['red' for index in range(size)]
        if insertion_sort_j < n-1:
            color[insertion_sort_j] = 'blue'
            if insertion_sort_j > 0:
                color[insertion_sort_j-1] = 'blue'
        source.data['color'] = color
        if insertion_sort_i <n-1:
            if insertion_sort_j == 0:
                insertion_sort_i+=1
                insertion_sort_j = insertion_sort_i
                for i in range(insertion_sort_j):
                    color[i]='pink'
                source.data['color'] = color
                insertion_flag = True
        if insertion_flag==True:
            if insertion_sort_j < n:
                color[insertion_sort_j] = 'blue'
                if insertion_sort_j > 0:
                    color[insertion_sort_j - 1] = 'blue'
                source.data['color'] = color
            insertion_flag = False

def update_size(attrname, old, new):
    y = [new]
    data_cbs.data['size'] = y
    arr = random.randint(20, size=new)
    index = [i for i in range(new)]
    color = ['red' for _ in range(new)]
    source.data = dict(index=index, arr=arr, color=color)
    sortin_source.data['arr'] = [1]
sortin_source.data['arr'] = [1]

size_slider = Slider(title="Sample size",
                    value=data_cbs.data['size'][0],
                    start=1, end=1000, step=1)

size_slider.on_change('value', update_size)


def update_speed(attrname, old, new):
    y = [new]
    data_cbs.data['speed'] = y

speed_sider = Slider(title="Step Speed",
                    value=data_cbs.data['size'][0],
                    start=1, end=100, step=1)

speed_sider.on_change('value', update_speed)
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

curdoc().add_root(column(f,row(select,speed_sider,size_slider)))
def selection():
    global sortin_source
    if  sortin_source.data['sorting'] != ['']:
        sortin_source.data['arr'] = [1]
        curdoc().add_periodic_callback(callback, 10)
curdoc().add_periodic_callback(selection, 10)