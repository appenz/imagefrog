# imagefrog.py
#
# (c) in 2024 by Guido Appenzeller
#
# Tool to sort through lots of images in a local directory
#

import os
import click
from PIL import Image

def check_image_properties(image_file):
    """Check if the image fulfills the properties set in the options"""
    image = Image.open(image_file)

    if 'ratio' in click.get_current_context().params:
        ratio = click.get_current_context().params['ratio']
        if ratio:
            width, height = image.size
            aspect_ratio = width / height

            # Check if this image has the correct aspect ratio
            if ratio == 'square':
                if aspect_ratio < 0.99 and aspect_ratio > 1.01:
                    return False
            elif ratio == 'portrait':
                if aspect_ratio < 1:
                    return False
            elif ratio == 'landscape':
                if aspect_ratio > 1:
                    return False
            elif ratio == 'wide':
                if aspect_ratio < 2.2:
                    return False
            elif ratio == 'ultrawide':
                if aspect_ratio < 3.4:
                    return False
            
    # Check if minimum width criteria is fulfilled
    if 'min_width' in click.get_current_context().params:
        min_width = click.get_current_context().params['min_width']
        if min_width:
            if width < min_width:
                return False

    # Check if minimum height criteria is fulfilled
    if 'min_height' in click.get_current_context().params:        
        min_height = click.get_current_context().params['min_height']
        if min_height:
            if height < min_height:
                return False

    return True

def find_image_files(srcdir):
    """Find image files in a directory and its subdirectories. Ignore raw files."""
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp')  
    
    image_files = []
    for root, _, files in os.walk(srcdir):
        for file in files:
            if file.lower().endswith(image_extensions):
                image_files.append(os.path.join(root, file))
    
    return image_files

def find_images(srcdir):
    """Find images in a directory"""

    images = find_image_files(srcdir)
    for image in images:
        if check_image_properties(image):
            print(image)

