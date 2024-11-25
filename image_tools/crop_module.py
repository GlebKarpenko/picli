import os
from PIL import Image

"""Crop images in the input folder and save them to the output folder."""
def crop_images(input_folder, output_folder, crop_coordinates):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            img = img.crop(crop_coordinates)
            output_path = os.path.join(output_folder, filename)
            img.save(output_path)
    print("Cropping complete")

def main(args):
    """Entry point for the crop subcommand."""
    crop_images(args.input_folder, args.output_folder, tuple(args.coords))

if __name__ == "__main__":
    print("This script is meant to be imported.")