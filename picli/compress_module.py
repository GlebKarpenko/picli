import os
from PIL import Image
from picli import config_module
from picli import resource_manager as mn
from picli import image_utils 
from sys import stdout

def compress_images(input_folder, output_folder, desired_width, desired_quality, fallback_format="JPEG"):
    """Compress images in the input folder and save them to the output folder."""
    os.makedirs(output_folder, exist_ok=True)

    edited_count = 0

    desired_quality = image_utils.format_quality(desired_quality)    
    supported_extensions = image_utils.get_supported_file_extensions()

    for filename in os.listdir(input_folder):
        file_extension = image_utils.get_file_extension(filename)

        if file_extension in supported_extensions:
            img_path = os.path.join(input_folder, filename)
            img = Image.open(img_path)

            width, height = img.size
            aspect_ratio = width / height

            scaled_width = image_utils.scale_metric(desired_width, width)
            scaled_width = scaled_width if scaled_width > 0 else width
            scaled_height = int(scaled_width / aspect_ratio)
            resized_image = img.resize((scaled_width, scaled_height))

            output_path = os.path.join(output_folder, filename)

            try:
                resized_image.save(output_path, quality = desired_quality)
            except Exception as e:
                resized_image.save(output_path, format=fallback_format, quality=desired_quality)
                print(mn.get_tools_message(
                    key="compressed_as_fallback",
                    filename=filename,
                    original=file_extension,
                    fallback=fallback_format))
            edited_count += 1

            stdout.write(f"\rProcessed images: {edited_count}")
            stdout.flush()

    if edited_count > 0:
        print()
        print(mn.get_tools_message(
            key="compressing_complete",
            input_folder=input_folder,
            output_folder=output_folder,
            edited_count=edited_count))
    else:
        print(mn.get_tools_error(key="compressing_failed",
                                 input_folder=input_folder))

def main(args):
    """Entry point for the compress subcommand."""
    input_folder = config_module.get_folder_path(args.input_folder, "input_folder")
    output_folder = config_module.get_folder_path(args.output_folder, "output_folder")
    compress_images(input_folder, output_folder, args.width, args.quality)

if __name__ == "__main__":
    print(mn.get_general_error(key="no_module_execution"))