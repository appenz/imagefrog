#
# Tool to sort through lots of images in a local directory
#
# (c) in 2024 by Guido Appenzeller

import sys
import os
import click
import tqdm
from PIL import Image

from imagefrog.imagefrog import *

# Option definitions. Click can't yet do them globally, so we need to define for each command. *Sigh*

ratio_option = click.option("--ratio", type=click.Choice(['wide', 'ultrawide', 'square', 'portrait', 'landscape'], case_sensitive=False), 
                            help="select images of this width/height ratio")
minimum_width_option = click.option("--min-width", type=int, help="select images of this min width")
minimum_height_option = click.option("--min-height", type=int, help="select images of this min height")

@click.group()
@click.option("--verbose", is_flag=True, help="verbose/debug output")
def cli(verbose):
    """Process image files in a directory using rules or image recognition"""
    return

@cli.command()
@click.argument("srcdir", required=False, type=click.Path(exists=True))
@ratio_option
@minimum_width_option
@minimum_height_option
def find(srcdir, ratio, min_width, min_height):
    """Find image files that match the criteria, default is all"""
    find_images(srcdir)

@cli.command()
@click.argument("srcdir", required=False, type=click.Path(exists=True))
@click.argument("destdir", required=False, type=click.Path(exists=True))
@ratio_option
@minimum_width_option
@minimum_height_option
def copy(srcdir, destdir, ratio, min_width, min_height):
    """Copy image files from source to destination"""
    print(f'not implemented yet: copying images from {srcdir} to {destdir}')

    