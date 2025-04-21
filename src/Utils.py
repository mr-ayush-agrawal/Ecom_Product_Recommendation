from math import ceil

def display_grid(items, columns):
    num_columns = len(columns)
    num_rows = ceil(len(items) / num_columns)  # Calculate how many rows will be needed

    for row in range(num_rows):
        cols = columns  # Create the columns
        for i in range(num_columns):
            index = row * num_columns + i  # Get the correct index
            if index < len(items):
                cols[i].write(items[index])
