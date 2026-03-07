import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Create the Treeview widget
tree = ttk.Treeview(root)
tree["columns"] = ("1", "2", "3")
tree.column("#0", width=100)
tree.column("1", width=100)
tree.column("2", width=100)
tree.column("3", width=100)
tree.heading("#0", text="Name")
tree.heading("1", text="Age")
tree.heading("2", text="City")
tree.heading("3", text="Country")
tree.pack(pady=10)

# Create the Entry widget for search
search_entry = tk.Entry(root)
search_entry.pack(pady=10)

# Sample data
data = [
    ("John", 25, "New York", "USA"),
    ("Jane", 32, "London", "UK"),
    ("Bob", 41, "Paris", "France"),
    ("Alice", 28, "Sydney", "Australia"),
    ("Tom", 35, "Tokyo", "Japan"),
]

# Function to highlight the matching letters in the Treeview items
def highlight_matches(text, search_term):
    highlighted_text = ""
    for char in text:
        if char.lower() in search_term.lower():
            highlighted_text += f"<highlight>{char}</highlight>"
        else:
            highlighted_text += char
    return highlighted_text

# Function to filter the Treeview based on the search query
def search_treeview(event):
    search_term = search_entry.get()
    if search_term:
        # Clear the Treeview
        for item in tree.get_children():
            tree.delete(item)

        # Populate the Treeview with matching items
        for item in data:
            if all(search_term.lower() in str(value).lower() for value in item):
                highlighted_name = highlight_matches(item[0], search_term)
                highlighted_values = [highlight_matches(str(value), search_term) for value in item[1:]]
                tree.insert("", "end", text=highlighted_name, values=highlighted_values)
    else:
        # Clear the Treeview if the search query is empty
        for item in tree.get_children():
            tree.delete(item)

# Bind the Entry widget's <KeyRelease> event to the search function
search_entry.bind("<KeyRelease>", search_treeview)

root.mainloop()