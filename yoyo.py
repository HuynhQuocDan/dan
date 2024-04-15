import tkinter as tk
import os
import pandas as pd

def save_to_file():
    user_input = entry.get()
    df = pd.DataFrame({"Characters": [user_input]})
    df.to_excel("output.xlsx", index=True)
    print(f"Saved '{user_input}' to output.xlsx")

# Create the main window
window = tk.Tk()
window.title("Check out paper")
window.geometry("500x400")

# Create an entry widget
entry = tk.Entry(window)
entry.pack()

# Create a button
save_button = tk.Button(window, text="Save to output.xlsx", command=save_to_file)
save_button.pack()

# Start the GUI event loop
window.mainloop()
