import tkinter as tk
from tkinter import messagebox

from silly_print import get_pages

def get_pages_action():
    output.delete("0.0", tk.END)

    try:
        first_page = int(first_page_entry.get())
        last_page = int(last_page_entry.get())
        pages_on_sheet = int(pages_on_sheet_entry.get())

        even, not_even = get_pages(first_page, last_page, pages_on_sheet)
        output.insert(tk.END, ','.join(even)) 
        output.insert(tk.END, '\n')
        output.insert(tk.END, ','.join(not_even)) 
        output.insert(tk.END, '\n')

    except:
        messagebox.showerror("Error", "Something went wrong")

root = tk.Tk() 
frame = tk.Frame(root, bd=5)
frame.pack()

entry_frame = tk.Frame(frame, bd=3)
entry_frame.pack()

first_page_label = tk.Label(entry_frame, text="First page", width=15)
first_page_label.grid(row=0, column=0)
first_page_entry = tk.Entry(entry_frame, width=3)
first_page_entry.grid(row=0, column=1)

last_page_label = tk.Label(entry_frame, text="Last page", width=15)
last_page_label.grid(row=1, column=0)
last_page_entry = tk.Entry(entry_frame, width=3)
last_page_entry.grid(row=1, column=1)

pages_on_sheet_label = tk.Label(entry_frame, text="Pages on sheet", width=15)
pages_on_sheet_label.grid(row=2, column=0)
pages_on_sheet_entry = tk.Entry(entry_frame, width=3)
pages_on_sheet_entry.grid(row=2, column=1)

get_pages_button = tk.Button(frame, text="Get pages", command=get_pages_action)
get_pages_button.pack(pady=3)

output = tk.Text(frame, height=2, width=50) 
output.pack() 

tk.mainloop() 

    