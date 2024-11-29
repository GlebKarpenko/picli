import argparse

from picli import resource_manager as mn
from picli.image_utils import parse_metric

def add_crop_command_parser(subparsers):
    crop_parser = subparsers.add_parser(
        "crop",
        help=mn.get_command_prop(command_name="crop", prop="help")
    )
    crop_parser.add_argument(
        "-c",
        "--coords", 
        # Determine type based on user input
        type=lambda v: [parse_metric(coord) for coord in v.split(',')],
        metavar="left, top, right, bottom",
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

def add_compress_command_parser(subparsers):
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
        "-w",
        "--width",
        type=int,
        default=720,
        help=mn.get_command_arg_prop(command_name="compress", arg_name="width", prop="help")
    )
    compress_parser.add_argument(
        "-q",
        "--quality",
        type=int,
        default=80,
        help=mn.get_command_arg_prop(command_name="compress", arg_name="quality", prop="help")
    )

def add_config_command_parser(subparsers):
    config_parser = subparsers.add_parser(
        "config",
        help=mn.get_command_prop(command_name="config", prop="help")
    )
    config_parser.add_argument(
        "-i",
        "--input_folder",
        type=str,
        required=False,
        help=mn.get_command_arg_prop(command_name="config", arg_name="input_folder", prop="help")
    )
    config_parser.add_argument(
        "-o",
        "--output_folder",
        type=str,
        required=False,
        help=mn.get_command_arg_prop(command_name="config", arg_name="output_folder", prop="help")
    )

def add_help_command_parser(subparsers):
    help_parser = subparsers.add_parser(
        "help",
        help=mn.get_command_prop(command_name="help", prop="help")
    )

def setup_subparsers(parser):
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help=mn.get_command_prop(command_name="picli", prop="help")
    )

    return subparsers

def setup_cli():
    parser = argparse.ArgumentParser(
        description=mn.get_command_prop(command_name="picli", prop="descr")
    )
    subparsers = setup_subparsers(parser)
    
    add_compress_command_parser(subparsers)
    add_crop_command_parser(subparsers)
    add_config_command_parser(subparsers)
    add_help_command_parser(subparsers)

    return parser