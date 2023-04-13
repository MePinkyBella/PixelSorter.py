from PIL import Image
import random

def pixel_sort(img_path):
    img = Image.open(img_path)
    pixels = img.load()
    width, height = img.size

    # Sort pixels horizontally
    for y in range(height):
        sorted_row = sorted([(pixels[x, y], x) for x in range(width)])
        for i, (pixel, x) in enumerate(sorted_row):
            pixels[i, y] = pixel

    # Sort pixels vertically
    for x in range(width):
        sorted_col = sorted([(pixels[x, y], y) for y in range(height)])
        for i, (pixel, y) in enumerate(sorted_col):
            pixels[x, i] = pixel

    # Add random noise
    for x in range(width):
        for y in range(height):
            noise = random.randint(-50, 50)
            r, g, b = pixels[x, y]
            pixels[x, y] = max(0, r+noise), max(0, g+noise), max(0, b+noise)

    img.show()

if __name__ == "__main__":
    pixel_sort("image.jpg")
