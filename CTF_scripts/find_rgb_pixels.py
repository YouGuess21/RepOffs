from PIL import Image

# Open the image file
image = Image.open("./starry_night_sky.png")  # Replace with the path to your image file

# Get the width and height of the image
width, height = image.size

# Iterate through each pixel
for x in range(width):
    for y in range(height):
        # Get the RGB color of the pixel
        pixel_color = image.getpixel((x, y))

        # Check if the pixel color is (0, 0, 0)
        if pixel_color == (255, 255, 255):
            # Change the pixel color to (255, 0, 0)
            image.putpixel((x, y), (255, 0, 0))
        else:
            image.putpixel((x, y), (0, 0, 0))

# Save the modified image
image.save("modified_image.png")

# Show the modified image (optional)
image.show()
