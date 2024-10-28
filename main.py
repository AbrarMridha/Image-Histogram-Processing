# This program loads an image and compute the intensity histogram for each color channel of the given input image.
# It also performs histogram stretching, aggressive histogram stretching and histogram equalization.
# This is the main file that performs the run method in the class ImageProcessingApp in GUI.py


from GUI import ImageProcessingApp

if __name__ == "__main__":
    app = ImageProcessingApp()
    app.run()