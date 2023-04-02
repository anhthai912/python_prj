import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Food Market Manager")

# Create a label for the title
title_label = tk.Label(root, text="Food Market Manager", font=("Helvetica", 18))
title_label.pack(pady=10)

# Create a frame for the input fields
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

# Create labels and entry fields for the input data
name_label = tk.Label(input_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(input_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

price_label = tk.Label(input_frame, text="Price:")
price_label.grid(row=1, column=0, padx=5, pady=5)
price_entry = tk.Entry(input_frame)
price_entry.grid(row=1, column=1, padx=5, pady=5)

quantity_label = tk.Label(input_frame, text="Quantity:")
quantity_label.grid(row=2, column=0, padx=5, pady=5)
quantity_entry = tk.Entry(input_frame)
quantity_entry.grid(row=2, column=1, padx=5, pady=5)

# Create a button to add the data to the inventory
def add_item():
    name = name_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()
    # Code to add the data to the inventory goes here
    print(f"Added {name} to inventory with price {price} and quantity {quantity}")

add_button = tk.Button(root, text="Add Item", command=add_item)
add_button.pack(pady=10)

# Create a button to view the inventory
def view_inventory():
    # Code to view the inventory goes here
    print("Viewing inventory...")

view_button = tk.Button(root, text="View Inventory", command=view_inventory)
view_button.pack(pady=10)

# Start the main loop
root.mainloop()
