from PIL import Image
import os

#crop region: left, top, right, bottom
CROPPED_COORDINATES = (0, 0, 550, 825)

INPUT_FOLDER = "../to_crop_right"
OUTPUT_FOLDER = "../cropped"

for filename in os.listdir(INPUT_FOLDER):
    if filename.endswith(".jpg"):
        img = Image.open(os.path.join(INPUT_FOLDER, filename))
        img = img.crop(CROPPED_COORDINATES)
        img.save(os.path.join(OUTPUT_FOLDER, filename))

print("Cropping complete")