# picli

<i>A simple CLI tool for batch image processing</i>

## Overview
<code>picli</code> is a command-line tool designed to automate multiple image editing tasks. It lets you process multiple files anywhere in your file system in a simple, configurable way.
<br><br>
This tool can be used when dealing with large image datasets that need to be edited in a scriptable way.

## Key features
  - Batch processing: Edit hundrets of images simultaneously.
  - Customizable operations: Multiple parameters for cropping, compression and input/output streams.
  - Cross-Platform: Windows, macOs, Linux
  - Automation-ready: can be scripted for required workflow

## Install
Check GitHub realeases for installation.

## Basic usage
`picli <command> [options]`

## Usage examples
<br>Crop images to a specific location:
  ```sh
  picli crop -coords 5%,0,20px,60 -input_folder ./images --output_folder ./cropped
  ```
<br>Crop images from current directory into ./edited:
  ```sh
  picli crop -c 5%,10%,0,0
  ```
<br>Compress with resizing images from current directory into ./edited:
  ```sh
  picli compress --width 80%, -q 55
  ```
<br>Resize images by width while remaining the aspect-ratio:
  ```sh
  picli compress -w 860px --output_folder ./resized`
  ```
<br>Config directories to edit from and save results to:
  ```sh
  picli config -i ../storage/images/raw_images -o ../storage/images/compressed
  ```

## Feedback
Feel free to email me at glebkarpenko1@gmail.com
