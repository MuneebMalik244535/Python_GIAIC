import tkinter as tk  # ✅ Tkinter library import karna

# ✅ Grid settings
CELL_SIZE = 40  # Har square ka size
ERASER_SIZE = 20  # Eraser ka size

def erase(event):
    """Jis cell ke upar mouse jayega, uska color white ho jayega"""
    x, y = event.x, event.y  # ✅ Mouse ka position lena
    items = canvas.find_overlapping(x, y, x + ERASER_SIZE, y + ERASER_SIZE)  # ✅ Find touched objects
    for item in items:
        canvas.itemconfig(item, fill="white")  # ✅ White color set karna (erase effect)

# ✅ Window (Canvas) Create Karna
root = tk.Tk()
root.title("Eraser")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# ✅ Grid of blue squares draw karna
for row in range(0, 400, CELL_SIZE):
    for col in range(0, 400, CELL_SIZE):
        canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="blue", outline="black")

# ✅ Mouse click + drag par erase function call hoga
canvas.bind("<B1-Motion>", erase)

root.mainloop()
