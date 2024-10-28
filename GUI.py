# This file holds the code for the graphical user interface.

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import histogram_funcs as hf
from tkinter import Frame, Tk, Button, Label, filedialog
import numpy as np

class ImageProcessingApp:
    def __init__(self):
        # Initialize the main tkinter window
        self.root = Tk()
        self.root.title("Image Processing Tool")
        self.root.geometry("600x500")
        self.image = None

        # Frame for buttons
        self.frame = Frame(self.root)
        self.frame.grid(row=1, column=0, columnspan=3, pady=10)

        # Buttons for operations
        btn_load = Button(self.frame, text="Load Image", command=self.load_image, width=20)
        btn_load.grid(row=0, column=0, padx=10, pady=10)

        btn_rgb_histogram = Button(self.frame, text="RGB Histograms", command=self.display_rgb_histogram, width=20)

        btn_rgb_histogram.grid(row=0, column=4, padx=10, pady=10)


        btn_aggressive_stretch = Button(self.frame, text="Aggressive Stretch", command=self.display_aggressive_stretch,
                                        width=20)
        btn_aggressive_stretch.grid(row=0, column=2, padx=10, pady=10)

        btn_equalize = Button(self.frame, text="Histogram Equalization", command=self.display_histogram_equalization,
                              width=20)
        btn_equalize.grid(row=0, column=3, padx=10, pady=10)


    # Function to plot and display image on the tkinter window
    def display_image(self, image, title="Image"):
        figure, ax = plt.subplots(figsize=(5, 4))
        ax.imshow(image)
        ax.set_title(title)
        ax.axis('off')

        canvas = FigureCanvasTkAgg(figure, master=self.root)  # A tk.DrawingArea
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    # Function to load an image using a file dialog
    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = plt.imread(file_path)
            if self.image.max() <= 1.0:
                self.image = (self.image * 255).astype(np.uint8)
            self.display_image(self.image, "Original Image")


    # Function to display the RGB histogram
    def display_rgb_histogram(self):
        if self.image is not None:
            hf.plot_histogram(self.image)


    # Apply aggressive histogram stretch and display
    def display_aggressive_stretch(self):
        if self.image is not None:
            aggressive_image = hf.aggressive_stretch(self.image)
            self.display_image(aggressive_image, "Aggressive Stretched Image")

    # Apply histogram equalization and display
    def display_histogram_equalization(self):
        if self.image is not None:
            equalized_image = hf.histogram_equalization(self.image)
            self.display_image(equalized_image, "Histogram Equalized Image")

    # Function to run the tkinter main loop
    def run(self):
        self.root.mainloop()