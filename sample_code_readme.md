

<i>Drop down graph</i>

```python
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output

# Sample data
data = {
    'Category 1': [10, 20, 30],
    'Category 2': [15, 25, 35],
    'Category 3': [20, 30, 40]
}

categories = list(data.keys())

# Dropdown menu
dropdown = widgets.Dropdown(
    options=categories,
    value=categories[0],
    description='Select Category:',
)

# Create the bar plot
def update_bar_plot(category):
    clear_output(wait=True)
    plt.figure(figsize=(8, 5))
    plt.bar(range(len(data[category])), data[category], color='blue')
    plt.title(f"Bar Graph for {category}")
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.show()

# Use interactive to link the dropdown and the plotting function
interactive_plot = widgets.interactive(update_bar_plot, category=dropdown)

# Display the interactive plot only (this includes the dropdown)
display(interactive_plot)
```

<i>Multi select - multi graphs</i>
```python
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output

# Sample data
data = {
    'Category 1': [10, 20, 30],
    'Category 2': [15, 25, 35],
    'Category 3': [20, 30, 40]
}

categories = list(data.keys())

# Multi-select menu
multi_select = widgets.SelectMultiple(
    options=categories,
    value=[categories[0]],
    description='Select Categories:',
)

# Create the bar plots
def update_bar_plots(categories):
    clear_output(wait=True)
    fig, axes = plt.subplots(len(categories), 1, figsize=(8, 5 * len(categories)))
    if len(categories) == 1:
        axes = [axes]
    
    for ax, category in zip(axes, categories):
        ax.bar(range(len(data[category])), data[category], color='blue')
        ax.set_title(f"Bar Graph for {category}")
        ax.set_xlabel('X-axis Label')
        ax.set_ylabel('Y-axis Label')
    
    plt.tight_layout()
    plt.show()

# Use interactive to link the multi-select and the plotting function
interactive_plot = widgets.interactive(update_bar_plots, categories=multi_select)

# Display the multi-select and the interactive plot
display(interactive_plot)

```


<i>Multi select into 1 graph<i/>

```python
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display, clear_output
import numpy as np

# Sample data
data = {
    'Category 1': [10, 20, 30],
    'Category 2': [15, 25, 35],
    'Category 3': [20, 30, 40]
}

categories = list(data.keys())

# Multi-select menu
multi_select = widgets.SelectMultiple(
    options=categories,
    value=[categories[0]],
    description='Select Categories:',
)

# Create the combined bar plot
def update_bar_plots(selected_categories):
    clear_output(wait=True)
    indices = np.arange(len(data[categories[0]]))
    width = 0.2
    
    plt.figure(figsize=(10, 6))
    
    for i, category in enumerate(selected_categories):
        plt.bar(indices + i * width, data[category], width, label=category)
    
    plt.xlabel('X-axis Label')
    plt.ylabel('Y-axis Label')
    plt.title('Combined Bar Graph for Selected Categories')
    plt.xticks(indices + width * (len(selected_categories) - 1) / 2, [f'Item {i+1}' for i in indices])
    plt.legend()
    plt.show()

# Use interactive to link the multi-select and the plotting function
interactive_plot = widgets.interactive(update_bar_plots, selected_categories=multi_select)

# Display the multi-select and the interactive plot
display(interactive_plot)


```