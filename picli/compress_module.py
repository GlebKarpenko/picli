import os
from PIL import Image
from picli import config_module
from picli import message_manager as mn

"""Compress images in the input folder and save them to the output folder."""
def compress_images(input_folder, output_folder, desired_width, desired_quality):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            width, height = img.size
            aspect_ratio = width / height
            new_height = int(desired_width / aspect_ratio)
            resized_image = img.resize((desired_width, new_height))

            output_path = os.path.join(output_folder, filename)
            resized_image.save(output_path, format="JPEG", quality = desired_quality)

    print(mn.get_tools_message(key="compressing_complete"))

def main(args):
    """Entry point for the compress subcommand."""
    input_folder = config_module.get_folder_path(args.input_folder, "input_folder")
    output_folder = config_module.get_folder_path(args.output_folder, "output_folder")
    compress_images(input_folder, output_folder, args.width, args.quality)

if __name__ == "__main__":
    print(mn.get_general_error(key="no_module_execution"))