import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "Del":
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="green")

entry = tk.Entry(root, font=("Arial", 20), bd=5)
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["Del"]
]

for row in buttons:
    frame = tk.Frame(root, bg="green")
    frame.pack()
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font=("Arial", 18), bg="red", fg="white", width=5, height=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", on_click)

root.mainloop()
