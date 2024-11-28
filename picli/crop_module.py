import os
from PIL import Image
from picli import config_module
from picli import message_manager as mn

def parse_coords(coordinate):
    """
    Parses a coordinate value which can be an integer or a percentage string.
    Returns the value as a tuple of (type, value), where type is 'px' or '%'.
    """
    if coordinate.endswith('%'):
        try: 
            return ('%', float(coordinate[:-1]))
        except ValueError:
            raise ValueError(mn.get_tools_error("cropping_wrong_percent", coordinate))
    else:
        try:
            return (('px'), int(coordinate))
        except ValueError:
            raise ValueError(mn.get_tools_error("cropping_wrong_pixel", coordinate))

def scale_coord(pair, image_scale):
    """
    Converts percentage values to image scale
    """
    dtype, value = pair

    if (dtype == '%'
        and value > 0 
        and value < 100):
        scaled_value = int(value / 100 * image_scale)
        return scaled_value
    elif isinstance(value, int): 
        return value
    else: 
        return 0

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

            left = scale_coord(coords[0], width)
            top = scale_coord(coords[1], height)
            right = width - scale_coord(coords[2], width)
            bottom = height -scale_coord(coords[3], height)

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
    crop_images(input_folder, output_folder, tuple(args.coords))

if __name__ == "__main__":
    print(mn.get_general_error(key="no_module_execution"))