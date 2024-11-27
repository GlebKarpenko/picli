import argparse

from image_tools import message_manager as mn
from image_tools import crop_module
from image_tools import compress_module
from image_tools import config_module

def main():
    parser = argparse.ArgumentParser(
        description=mn.get_command_prop(command_name="picli", prop="descr")
    )
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help=mn.get_command_prop(command_name="picli", prop="help")
    )

    # Crop command
    crop_parser = subparsers.add_parser(
        "crop",
        help=mn.get_command_prop(command_name="crop", prop="help")
    )
    crop_parser.add_argument(
        "--coords", 
        type=int, 
        nargs=4, 
        metavar=("left", "top", "right", "bottom"),
        required=True, 
        help=mn.get_command_arg_prop(command_name="crop", arg_name="coords", prop="help")
    )
    crop_parser.add_argument(
        "-i",
        "--input_folder",
        type=str,
        help=mn.get_command_arg_prop(command_name="crop", arg_name="input_folder", prop="help")
    )
    crop_parser.add_argument(
        "-o",
        "--output_folder",
        type=str,
        help=mn.get_command_arg_prop(command_name="crop", arg_name="output_folder", prop="help")
    )

    # Compress command
    compress_parser = subparsers.add_parser(
        "compress",
        help = mn.get_command_prop(command_name="compress", prop="help")
    )
    compress_parser.add_argument(
        "-i",
        "--input_folder",
        type=str,
        help=mn.get_command_arg_prop(command_name="compress", arg_name="input_folder", prop="help")
    )
    compress_parser.add_argument(
        "-o",
        "--output_folder",
        type=str,
        help=mn.get_command_arg_prop(command_name="compress", arg_name="output_folder", prop="help")
    )
    compress_parser.add_argument(
        "--width",
        type=int,
        default=720,
        help=mn.get_command_arg_prop(command_name="compress", arg_name="width", prop="help")
    )
    compress_parser.add_argument(
        "--quality",
        type=int,
        default=80,
        help=mn.get_command_arg_prop(command_name="compress", arg_name="quality", prop="help")
    )

    # Config command
    config_parser = subparsers.add_parser(
        "config",
        help=mn.get_command_prop(command_name="config", prop="help")
    )
    config_parser.add_argument(
        "-i"
        "--input_folder",
        type=str,
        required=False,
        help=mn.get_command_arg_prop(command_name="config", arg_name="input_folder", prop="help")
    )
    config_parser.add_argument(
        "-o"
        "--output_folder",
        type=str,
        required=False,
        help=mn.get_command_arg_prop(command_name="config", arg_name="output_folder", prop="help")
    )

    # Help command
    help_parser = subparsers.add_parser(
        "help",
        help=mn.get_command_prop(command_name="help", prop="help")
    )

    args = parser.parse_args()

    commands = {
        "help": lambda: parser.print_help(),
        "crop": lambda: crop_module.main(args),
        "compress": lambda: compress_module.main(args),
        "config": lambda: config_module.main(args)
    }

    unknown_command = commands["help"]
    commands.get(args.command, unknown_command)()

if __name__ == "__main__":
    main()
    