
from PIL import Image

def zoom_and_crop(image_path, zoom_ratio, crop_ratio):
    # Open the image
    image = Image.open(image_path)

    # Get the dimensions of the original image
    width, height = image.size

    # Calculate the new dimensions after zooming
    new_width = int(width * zoom_ratio)
    new_height = int(height * zoom_ratio)

    # Resize the image to the new dimensions
    zoomed_image = image.resize((new_width, new_height))

    # Calculate the cropping box
    crop_width = int(new_width * crop_ratio)
    crop_height = int(new_height * crop_ratio)
    left = (new_width - crop_width) // 2
    top = (new_height - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height
    crop_box = (left, top, right, bottom)

    # Crop the image
    cropped_image = zoomed_image.crop(crop_box)

    # Display or save the cropped image
    cropped_image.show()  # To display the image
    # cropped_image.save("cropped_image.jpg")  # To save the image

# Get input from the user
image_path = input("Enter the path to the input image: ")
zoom_ratio = float(input("Enter the zoom ratio (1.0 means no zoom): "))
crop_ratio = float(input("Enter the crop ratio (0.0 means no crop): "))

# Call the function with user input
zoom_and_crop(image_path, zoom_ratio, crop_ratio)
