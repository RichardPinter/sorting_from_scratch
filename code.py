import bokeh
import pandas
import numpy
from bokeh.io import save, output, output_file
from bokeh.layouts import gridplot
from bokeh.plotting import figure
from numpy import random


### Different types of sorting algorithms

##          -   EASY   -


def create_colors(i, j, arr):

    return [
        "red"
        if (index != j and index != j + 1 )
        else 'blue'
        for index, hey in enumerate(arr)
    ]


def visualBar(index, arr, iter, j, i,sorted_num):

    colors = create_colors(i, j, arr)
    for number in sorted_num:
        colors[number] = 'green'
    f = figure()
    f.title = f"Bubble-sort-iteration:{iter}"
    f.vbar(x=index, top=arr, color=colors)

    return f




def bubble_sort(index, arr):
    plots = []
    sorted_num = []
    for i in range(1, len(arr)):
        for j in range(0, len(arr) - i):
            plots.append([visualBar(index, arr.copy(), i + j - 1, j, i,sorted_num)])
            if arr[j + 1] < arr[j]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]
            plots.append([visualBar(index, arr.copy(), i, j, i,sorted_num)])
        sorted_num.append(len(arr)-i)
    plots.append([visualBar(index, arr.copy(), i, j, i, sorted_num)])
    return (arr, gridplot(plots))


def selection_sort(index,arr):
    plots = []
    sorted_num = []
    for i,n in enumerate(arr):
        min_pos = i
        curr_pos = i
        minimum = arr[i]
        while curr_pos< len(arr):
            plots.append([selectin_bar(index, arr.copy(), i, min_pos,curr_pos, sorted_num)])
            if arr[curr_pos]<minimum:
                minimum = arr[curr_pos]
                min_pos = curr_pos
            curr_pos += 1
        print(arr[i], arr[min_pos])
        plots.append([selectin_bar(index, arr.copy(), i, min_pos,curr_pos, sorted_num)])
        arr[i], arr[min_pos] = arr[min_pos], arr[i]
        plots.append([selectin_bar(index, arr.copy(), i, min_pos,curr_pos, sorted_num)])
        sorted_num.append(i)
    plots.append([selectin_bar(index, arr.copy(), i, min_pos,curr_pos, sorted_num)])
    return (arr, gridplot(plots))


def selectin_bar(index, arr,iter,min_iter,curr_iter,sorted_num):
    color =  [
        "red"
        if (index != iter and index != min_iter  )
        else 'blue'
        for index, _ in enumerate(arr)
    ]
    for number in sorted_num:
        color[number] = 'green'
    if curr_iter <= len(color)-1:
        print(curr_iter,len(color))
        color[curr_iter] = 'black'
    f = figure()
    f.title = f"Bubble-sort-iteration:{iter}"
    f.vbar(x=index, top=arr, color = color)

    return f

def insertion_sort(index,arr):

    plots = []
    sorted_num = []
    for i,n in enumerate(arr):

        if i==0:
            continue
        j = i
        flag = False
        plots.append([insertion_bar(index, arr.copy(), i, j,flag)])
        while j>0 and arr[j-1]>arr[j]:
            plots.append([insertion_bar(index, arr.copy(), i, j,flag)])
            arr[j-1], arr[j] = arr[j], arr[j-1]
            plots.append([insertion_bar(index, arr.copy(), i, j,flag)])
            j-=1
        flag = True
        plots.append([insertion_bar(index, arr.copy(), i, j,flag)])

    return (arr, gridplot(plots))

def insertion_bar(index, arr,i,j,flag):
    color =  [
        "red"
        if (index != j and index != j-1  )
        else 'blue'
        for index, _ in enumerate(arr)
    ]
    color[i] = 'black'
    if flag == True:
        color = [
            "red"
            if (index >i)
            else 'green'
            for index, _ in enumerate(arr)
        ]
    f = figure()
    f.title = f"Bubble-sort-iteration:{i}"
    f.vbar(x=index, top=arr,color= color)

    return f


### Visualistion functiokn


if __name__ == "__main__":

    ## Creating test array
    size = 5
    llist = random.randint(100, size=size)
    print(llist)
    index = [i  for i in range(5)]

    ## Testing bubble sort
    sorted_arr, grid = bubble_sort(index, llist.copy())
    ## Verification
    output_file("hello.html")
    save(grid)

    ## Testing selection sort
    selection_arr, selection_grid = selection_sort(index,llist.copy())
    ## Verification
    print(llist, sorted_arr,selection_arr)
    output_file("selection_sort.html")
    save(selection_grid)

    insertion_arr,insertion_grid = insertion_sort(index,llist.copy())
    ## Verification
    print(llist, sorted_arr,insertion_arr)
    output_file("insertion.html")
    save(insertion_grid)



