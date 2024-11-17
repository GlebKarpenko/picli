import argparse
import os
from PIL import Image

def parse_args():
    parser = argparse.ArgumentParser(description="Compress images in a folder based on desired width and quality.")
    parser.add_argument(
        "--input_folder",
        type=str,
        default="../to_compress",
        help="Input folder containing images to compress. Default is '../to_compress'."
    )
    parser.add_argument(
        "--output_folder",
        type=str,
        default="../compressed",
        help="Output folder for cropped images. Default is 'compressed'."
    )
    parser.add_argument(
        "--width",
        type=int,
        default=720,
        help="Width for result image. Height is determined respectivly to aspect ratio."
    )
    parser.add_argument(
        "--quality",
        type=int,
        default=80,
        help="Desired quality for result image. Bigger value means higher quality. Defaul is 80."
    )
    return parser.parse_args()

def compress_images(input_folder, output_folder, desired_width, desired_quality):
    for filename in os.listdir(input_folder):
        if (filename).endswith(".jpg"):
            img = Image.open(os.path.join(input_folder, filename))
            width, height = img.size
            aspect_ratio = width / height
            new_height = int(desired_width / aspect_ratio)
            resized_image = img.resize((desired_width, new_height))
            resized_image.save(os.path.join(output_folder, filename), format="JPEG", quality = desired_quality)

    print("Compressing complete")

def main():
    args = parse_args()
    compress_images(args.input_folder, args.output_folder, args.width, args.quality)

if __name__ == "__main__":
    main()