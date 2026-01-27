# Import tkinter for creating GUI window, buttons, labels
import tkinter as tk

# Import time module to pause between images
import time

# Import Image and ImageTk from PIL (external library)
# Image     -> open and resize images
# ImageTk   -> convert images so Tkinter can display them
from PIL import Image, ImageTk


# -------------------- MAIN WINDOW --------------------

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("Python Image Slideshow App")

# Set the window size
root.geometry("900x600")


# -------------------- IMAGE PATHS --------------------
# List of image file paths (change paths as per your system)

image_paths = [
    r"C:\Users\ajeetkumar\OneDrive\Pictures\Wild Animal_6_OBGA.OIGP.VyDxrAtSbW6Ba7g61uNv_Wild Animal.jpg",
    r"C:\Users\ajeetkumar\OneDrive\Pictures\Wild Animal_188_OBGA.AdobeStock_697812048_Wild Animal.jpg",
    r"C:\Users\ajeetkumar\OneDrive\Pictures\WhatsApp Image 2025-12-17 at 2.08.07 PM.jpeg"
]


# -------------------- IMAGE PROCESSING --------------------

# Set fixed size for all images
image_size = (800, 500)

# List to store resized PIL images
images = []

# Open and resize each image using PIL
for path in image_paths:
    img = Image.open(path)          # Open image
    img = img.resize(image_size)    # Resize image
    images.append(img)              # Store image


# Convert PIL images to Tkinter compatible images
photo_images = []
for img in images:
    photo = ImageTk.PhotoImage(img)
    photo_images.append(photo)


# -------------------- IMAGE DISPLAY AREA --------------------

# Label widget used as image frame
image_label = tk.Label(root)
image_label.pack(pady=20)


# -------------------- SLIDESHOW FUNCTION --------------------

def start_slideshow():
    # Loop through all images
    for photo in photo_images:
        # Set image on label
        image_label.config(image=photo)

        # Keep reference to image (important to avoid image disappearing)
        image_label.image = photo

        # Update the GUI to show the image
        root.update()

        # Pause for 2 seconds before showing next image
        time.sleep(2)


# -------------------- BUTTON --------------------

# Button to start the slideshow
play_button = tk.Button(
    root,
    text="Play Slideshow",
    font=("Arial", 14),
    command=start_slideshow
)

# Place button on the window
play_button.pack(pady=10)


# -------------------- RUN APPLICATION --------------------

# Start the event loop and keep window open
root.mainloop()

