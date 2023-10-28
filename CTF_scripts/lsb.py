from PIL import Image

# Open the PNG image
image = Image.open('encoded.png')

# Create a new image with the same size and 'RGB' mode
extracted_image = Image.new('RGB', image.size)

# Iterate through each pixel and extract the LSB from each color channel
for x in range(image.width):
    for y in range(image.height):
        pixel = image.getpixel((x, y))
        red_lsb = pixel[0] & 1
        green_lsb = pixel[1] & 1
        blue_lsb = pixel[2] & 1
        extracted_pixel = (red_lsb * 255, green_lsb * 255, blue_lsb * 255)
        extracted_image.putpixel((x, y), extracted_pixel)

# Save the extracted image
extracted_image.save('new.png')

# Close the images
image.close()
extracted_image.close()
