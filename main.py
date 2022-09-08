from functools import partial

import panel as pn
import pandas as pd
import numpy as np
from bokeh.models import Button, ColumnDataSource, Select, MultiSelect, Slider, CustomJS

from callback import select_sorting_callback, query_callback,query_reset




### Create CBS

data_dict = {
    "sorting_alg": ['-'],
    "speed": [100],
    "size": [100],
    'flag': [False],
    'source': ['-']
}
data_cbs = ColumnDataSource(data_dict)

flag = False
### Default options

sorting_list = ['-','bubble_sort', 'selection_sort','insertion_sort','heap_sort']



#### Create the DOM
tabs = pn.Tabs(dynamic=True)

### Button

new_button = Button(label="Press Button for a new sorting algorithm",button_type="success")
new_button.on_click(partial(query_callback,data_cbs,tabs))

select_sorting = Select(name="Select sorting algorithm", options = sorting_list)
select_sorting.on_change('value', partial(select_sorting_callback,data_cbs))



### Sorting




### Sliders

def update_size(attrname, old, new):
    y = [new]
    data_cbs.data['size'] = y

size_slider = Slider(title="Sample size",
                    value=data_cbs.data['size'][0],
                    start=1, end=200, step=1)

size_slider.on_change('value', update_size)


def update_speed(attrname, old, new):
    y = [new]
    data_cbs.data['speed'] = y

speed_sider = Slider(title="Speed (miliseconds)",
                    value=data_cbs.data['size'][0],
                    start=1, end=3000, step=10)

speed_sider.on_change('value', update_speed)
### Serving

layout = pn.Row(
    pn.Column(new_button,select_sorting,size_slider,speed_sider),
)


tabs.append(("Sorting Algorithm", layout))
tabs.servable(),

