import tkinter as tk


# Function to update the display with button click
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))


# Function to clear the display
def clear():
    entry.delete(0, tk.END)


# Function to perform calculation and display the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Create the main window
root = tk.Tk()
root.title("Shakunt Calculator")

# Create an entry widget for displaying the input and output
entry = tk.Entry(root, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Define and create the number and operator buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row, col = 1, 0

for button_text in buttons:
    if button_text == 'C':
        button = tk.Button(root, text=button_text, padx=20, pady=20, command=clear)
    elif button_text == '=':
        button = tk.Button(root, text=button_text, padx=20, pady=20, command=calculate)
    else:
        button = tk.Button(root, text=button_text, padx=20, pady=20,
                           command=lambda text=button_text: button_click(text))

    button.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
