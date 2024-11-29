import os
from PIL import Image

from picli.image_utils import scale_metric
from picli import config_module
from picli import message_manager as mn

def format_coords(input_coords):
    if len(input_coords) == 1:
        return input_coords * 4
    elif len(input_coords) == 4:
        return input_coords
    else:
        raise ValueError(mn.get_tools_error("wrong_crop_coords_input"))

def crop_images(input_folder, output_folder, coords):
    """
    Coords are provided either as a number of pixels to crop
    or in percentage respective of image size.
    Inverts user coords to be represented in PIL system.
    Crops images in the input folder and saves them to the output folder.
    """

    os.makedirs(output_folder, exist_ok=True)

    edited_count = 0
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)
            
            width, height = img.size

            left = scale_metric(coords[0], width)
            top = scale_metric(coords[1], height)
            right = width - scale_metric(coords[2], width)
            bottom = height -scale_metric(coords[3], height)

            crop_box = (left, top, right, bottom)
            img = img.crop(crop_box)
            
            output_path = os.path.join(output_folder, filename)
            img.save(output_path)

            edited_count += 1

    if (edited_count > 0):
        print(mn.get_tools_message(
            key="cropping_complete",
            input_folder=input_folder, 
            output_folder=output_folder, 
            edited_count=edited_count))
    else:
        print(mn.get_tools_error(key="cropping_failed"))

def main(args):
    """Entry point for the crop subcommand."""

    input_folder = config_module.get_folder_path(args.input_folder, "input_folder")
    output_folder = config_module.get_folder_path(args.output_folder, "output_folder")
    
    cropping_coords = format_coords(tuple(args.coords))
    crop_images(input_folder, output_folder, cropping_coords)

if __name__ == "__main__":
    print(mn.get_general_error(key="no_module_execution"))