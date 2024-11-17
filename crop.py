import argparse
import os
from PIL import Image

def parse_args():
    parser = argparse.ArgumentParser(description="Crop images in a folder based on given coordinates.")
    parser.add_argument(
        "--coords", 
        type=int, 
        nargs=4, 
        metavar=("left", "top", "right", "bottom"),
        required=True, 
        help="Coordinates for cropping (left, top, right, bottom)."
    )
    parser.add_argument(
        "--input_folder",
        type=str,
        default="../to_crop",
        help="Input folder containing images to crop. Default is 'to_crop_right'."
    )
    parser.add_argument(
        "--output_folder",
        type=str,
        default="../cropped",
        help="Output folder for cropped images. Default is 'cropped'."
    )
    return parser.parse_args()

def crop_images(input_folder, output_folder, crop_coordinates):
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg"):
            img = Image.open(os.path.join(input_folder, filename))
            img = img.crop(crop_coordinates)
            img.save(os.path.join(output_folder, filename))

print("Cropping complete")

def main():
    args = parse_args()
    crop_images(args.input_folder, args.output_folder, tuple(args.coords))

if __name__ == "__main__":
    main()