import argparse
from image_tools import crop_module

def main():
    parser = argparse.ArgumentParser(
        description="A CLI toolset for image editing."
    )
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help="Subcommand to run (e.g., crop, resize, filter)."
    )

    # Crop command
    crop_parser = subparsers.add_parser(
        "crop",
        help="Crop images in a folder based on given coordinates."
    )
    crop_parser.add_argument(
        "--coords", 
        type=int, 
        nargs=4, 
        metavar=("left", "top", "right", "bottom"),
        required=True, 
        help="Coordinates for cropping (left, top, right, bottom)."
    )
    crop_parser.add_argument(
        "--input_folder",
        type=str,
        default="../to_crop",
        help="Input folder containing images to crop. Default is '../to_crop'."
    )
    crop_parser.add_argument(
        "--output_folder",
        type=str,
        default="../cropped",
        help="Output folder for cropped images. Default is '../cropped'."
    )

    args = parser.parse_args()

    if args.command == "crop":
        crop_module.main(args)

if __name__ == "__main__":
    main()
    