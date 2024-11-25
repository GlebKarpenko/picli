import argparse
from image_tools import crop_module, compress_module

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

    # Compress command
    compress_parser = subparsers.add_parser(
        "compress",
        help = "Compress images in a folder based on desired width and quality."
    )
    compress_parser.add_argument(
        "--input_folder",
        type=str,
        default="../to_compress",
        help="Input folder containing images to compress. Default is '../to_compress'."
    )
    compress_parser.add_argument(
        "--output_folder",
        type=str,
        default="../compressed",
        help="Output folder for cropped images. Default is 'compressed'."
    )
    compress_parser.add_argument(
        "--width",
        type=int,
        default=720,
        help="Width for result image. Height is determined respectivly to aspect ratio."
    )
    compress_parser.add_argument(
        "--quality",
        type=int,
        default=80,
        help="Desired quality for result image. Bigger value means higher quality. Defaul is 80."
    )

    # Help command
    help_parser = subparsers.add_parser(
        "help",
        help="Show available commands and their descriptions."
    )

    args = parser.parse_args()

    commands = {
        "help": parser.print_help(),
        "crop": lambda: crop_module.main(args),
        "compress": lambda: compress_module.main(args)
    }

    unknown_command = parser.print_help()
    commands.get(args.command, unknown_command)()

if __name__ == "__main__":
    main()
    