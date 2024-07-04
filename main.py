import tkinter as tk
from tkinter import colorchooser


class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")

        self.brush_size = 5
        self.brush_color = "black"

        self.canvas = tk.Canvas(root, bg="white", width=600, height=400)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.canvas.bind("<B1-Motion>", self.paint)

        self.brush_size_frame = tk.Frame(root)
        self.brush_size_frame.pack(side=tk.LEFT, padx=10)
        self.brush_size_label = tk.Label(self.brush_size_frame, text="Brush size:")
        self.brush_size_label.pack(side=tk.LEFT)

        self.brush_size_slider = tk.Scale(self.brush_size_frame, from_=1, to=10, orient=tk.HORIZONTAL)
        self.brush_size_slider.set(self.brush_size)
        self.brush_size_slider.pack(side=tk.LEFT)

        self.color_button = tk.Button(root, text="Choose color", command=self.choose_color)
        self.color_button.pack(side=tk.LEFT, padx=10)

        self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side=tk.LEFT, padx=10)

    def paint(self, event):
        self.brush_size = self.brush_size_slider.get()
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

    def choose_color(self):
        self.brush_color = colorchooser.askcolor(color=self.brush_color)[1]

    def clear_canvas(self):
        self.canvas.delete("all")


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
