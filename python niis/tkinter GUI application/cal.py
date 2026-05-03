import tkinter as tk

# -------------------------------
# Functions
# -------------------------------
def click(value):
    current = entry_var.get()
    entry_var.set(current + str(value))

def clear():
    entry_var.set("")

def backspace():
    current = entry_var.get()
    entry_var.set(current[:-1])

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except:
        entry_var.set("Error")

# -------------------------------
# Main Window
# -------------------------------
root = tk.Tk()
root.title("Calculator")
root.geometry("350x500")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# -------------------------------
# Entry Display
# -------------------------------
entry_var = tk.StringVar()

entry = tk.Entry(
    root,
    textvariable=entry_var,
    font=("Arial", 24),
    bd=10,
    relief=tk.RIDGE,
    justify="right",
    bg="white"
)
entry.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=20)

# -------------------------------
# Button Frame
# -------------------------------
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack()

# Button Style
btn_font = ("Arial", 18)
btn_width = 5
btn_height = 2

# -------------------------------
# Row 1
# -------------------------------
tk.Button(button_frame, text="C", font=btn_font, width=btn_width, height=btn_height,
          command=clear, bg="#ff6666").grid(row=0, column=0, padx=5, pady=5)

tk.Button(button_frame, text="⌫", font=btn_font, width=btn_width, height=btn_height,
          command=backspace, bg="#ffcc66").grid(row=0, column=1, padx=5, pady=5)

tk.Button(button_frame, text="%", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("%"), bg="#66b3ff").grid(row=0, column=2, padx=5, pady=5)

tk.Button(button_frame, text="/", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("/"), bg="#66b3ff").grid(row=0, column=3, padx=5, pady=5)

# -------------------------------
# Row 2
# -------------------------------
tk.Button(button_frame, text="7", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("7")).grid(row=1, column=0, padx=5, pady=5)

tk.Button(button_frame, text="8", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("8")).grid(row=1, column=1, padx=5, pady=5)

tk.Button(button_frame, text="9", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("9")).grid(row=1, column=2, padx=5, pady=5)

tk.Button(button_frame, text="*", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("*"), bg="#66b3ff").grid(row=1, column=3, padx=5, pady=5)

# -------------------------------
# Row 3
# -------------------------------
tk.Button(button_frame, text="4", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("4")).grid(row=2, column=0, padx=5, pady=5)

tk.Button(button_frame, text="5", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("5")).grid(row=2, column=1, padx=5, pady=5)

tk.Button(button_frame, text="6", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("6")).grid(row=2, column=2, padx=5, pady=5)

tk.Button(button_frame, text="-", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("-"), bg="#66b3ff").grid(row=2, column=3, padx=5, pady=5)

# -------------------------------
# Row 4
# -------------------------------
tk.Button(button_frame, text="1", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("1")).grid(row=3, column=0, padx=5, pady=5)

tk.Button(button_frame, text="2", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("2")).grid(row=3, column=1, padx=5, pady=5)

tk.Button(button_frame, text="3", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("3")).grid(row=3, column=2, padx=5, pady=5)

tk.Button(button_frame, text="+", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("+"), bg="#66b3ff").grid(row=3, column=3, padx=5, pady=5)

# -------------------------------
# Row 5
# -------------------------------
tk.Button(button_frame, text="0", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("0")).grid(row=4, column=0, padx=5, pady=5)

tk.Button(button_frame, text=".", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click(".")).grid(row=4, column=1, padx=5, pady=5)

tk.Button(button_frame, text="(", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click("(")).grid(row=4, column=2, padx=5, pady=5)

tk.Button(button_frame, text=")", font=btn_font, width=btn_width, height=btn_height,
          command=lambda: click(")")).grid(row=4, column=3, padx=5, pady=5)

# -------------------------------
# Equal Button
# -------------------------------
tk.Button(
    root,
    text="=",
    font=("Arial", 22, "bold"),
    bg="#4CAF50",
    fg="white",
    command=calculate
).pack(fill="both", ipadx=8, ipady=15, padx=10, pady=15)

# -------------------------------
# Run App
# -------------------------------
root.mainloop()