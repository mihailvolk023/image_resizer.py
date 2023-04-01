from PIL import Image
import os

def resize_image(input_dir, output_dir, new_size):
    for filename in os.listdir(input_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(input_dir, filename))
            img_resized = img.resize(new_size)
            img_resized.save(os.path.join(output_dir, filename))

input_dir = "/path/to/input/directory"
output_dir = "/path/to/output/directory"
new_size = (800, 600)

resize_image(input_dir, output_dir, new_size)
