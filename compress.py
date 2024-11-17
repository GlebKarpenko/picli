from PIL import Image
import os

INPUT_FOLDER = "../cropped"
OUTPUT_FOLDER = "../compressed"
DESIRED_WIDTH = 720
DESIRED_QUALITY = 12

for filename in os.listdir(INPUT_FOLDER):
    if (filename).endswith(".jpg"):
        img = Image.open(os.path.join(INPUT_FOLDER, filename))
        width, height = img.size
        aspect_ratio = width / height
        new_height = int(DESIRED_WIDTH / aspect_ratio)
        resized_image = img.resize((DESIRED_WIDTH, new_height))
        resized_image.save(os.path.join(OUTPUT_FOLDER, filename), format="JPEG", quality = DESIRED_QUALITY)

print("Compressing complete")