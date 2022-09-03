from functools import partial
from bokeh.layouts import column, row
from bokeh.models import Button, ColumnDataSource, Slider
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc
from numpy import random
import time
from bokeh.models.widgets import Select
import panel as pn
### Creating the data
from minheap import MinHeap

from functools import partial
from bokeh.layouts import column, row
from bokeh.models import Button, ColumnDataSource, Slider
from bokeh.palettes import RdYlBu3
from bokeh.plotting import figure, curdoc
from numpy import random
import time
from bokeh.models.widgets import Select
import panel as pn

size = 100
arr = random.randint(20, size=size).tolist()
index = [i for i in range(size)]
color = ['red' for _ in range(size)]


### Merge Sort Functino


def merge_sort(arr):
    pass

def heap_sort(arr):
    pass


### Heap implementationj



llist = []
heap = MinHeap(arr,color)

source = ColumnDataSource(dict(index=index, arr=arr, color=color))

### Visualisation basics
f = figure()
f.vbar(x='index', top='arr', fill_color='color', source=source)

removed = []
def callback():
    global removed,source,heap,size
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



# remove_flag = True
# last_index = len(heap.heap) - 1
# index  = 0
# def callback_1():
#     global removed, source, heap, size,remove_flag,last_index,index
#     if heap.heap:
#         # if remove_flag == True:
#         min = heap.remove()
#         removed.append(min)
#         ## First I have to swap
#         color = ['red'] * (size)
#         heap.swap(0, len(heap.heap) - 1, heap.heap,heap.color)
#         color[0] = 'blue'
#         color[len(heap.heap) - 1] =  'blue'
#         source.data['color'] =  color
#         ## Pop an element
#         value = heap.heap.pop(-1)
#         color[len(heap.heap) - 1] = 'blue'
#         source.data['color'] = color
#         removed.append(value)
#         llist = heap.heap.copy()
#         llist.extend(removed)
#         source.data['arr'] = llist
#         ## Rearrage
#     # else:
#         last_index = len(heap.heap) - 1
#         childNodeOne = index * 2 + 1
#         while childNodeOne <= last_index:
#
#             childIndexTwo = index * 2 + 2 if index * 2 + 2 <= last_index else -1
#             if childIndexTwo != -1 and heap.heap[childIndexTwo] < heap.heap[childNodeOne]:
#                 idxToSwap = childIndexTwo
#                 print('compare child nodes', heap.heap[childIndexTwo], heap.heap[childNodeOne])
#             else:
#                 idxToSwap = childNodeOne
#                 print('swap', heap.heap[idxToSwap])
#             if heap.heap[idxToSwap] < heap.heap[index]:
#                 color = ['red'] * (size)
#                 heap.swap(index, idxToSwap, heap.heap, color)
#                 color = ['red'] * size
#                 color[index] = 'blue'
#                 color[idxToSwap] = 'blue'
#                 source.data['color'] = color
#                 index = idxToSwap
#                 print('hey')
#                 childNodeOne = index * 2 + 1
#                 if childNodeOne <= last_index:
#                     print('update node', heap.heap[childNodeOne])
#             else:
#                 # llist = heap.heap.copy()
#                 # llist.extend(removed)
#                 # source.data['arr'] = llist
#                 # remove_flag = True
#                 # if remove_flag:
#                 #     print('remove', heap.heap[childNodeOne])
#                 # else:
#                 #     print('update node', heap.heap[childNodeOne])
#                 break
curdoc().add_root(column(f))
curdoc().add_periodic_callback(callback, 1000)