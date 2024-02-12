from PIL import Image, ImageEnhance

def zoom_and_crop(image_path, zoom_ratio, crop_ratio, brightness_factor=1.0, contrast_factor=1.0):
   
    image = Image.open(image_path)


    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness_factor)

  
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(contrast_factor)

   
    width, height = image.size

    
    new_width = int(width * zoom_ratio)
    new_height = int(height * zoom_ratio)

  
    zoomed_image = image.resize((new_width, new_height))

    
    crop_width = int(new_width * crop_ratio)
    crop_height = int(new_height * crop_ratio)
    left = (new_width - crop_width) // 2
    top = (new_height - crop_height) // 2
    right = left + crop_width
    bottom = top + crop_height
    crop_box = (left, top, right, bottom)

    
    cropped_image = zoomed_image.crop(crop_box)

    cropped_image.show()  # To display the image
    # cropped_image.save("cropped_image.jpg")  


image_path = input("Enter the path to the input image:E://Swopner4-1//The_ashes.jpg ")
zoom_ratio = float(input("Enter the zoom ratio (1.0 means no zoom): "))
crop_ratio = float(input("Enter the crop ratio (0.0 means no crop): "))
brightness_factor = float(input("Enter the brightness factor (1.0 means no change): "))
contrast_factor = float(input("Enter the contrast factor (1.0 means no change): "))


zoom_and_crop(image_path, zoom_ratio, crop_ratio, brightness_factor, contrast_factor)
