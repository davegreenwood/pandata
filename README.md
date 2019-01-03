# Download Panoptic Studio Data

install using:

    pip install .

Using the `-e` flag allows editing of the module while in the python path.

## Usage

A CLI is provide:

Download all the panoptic studio data:
Select one or more options for pose, vga or hd data,
without at least one option nothing will download.
Smaller lists of scenes can be downloaded, or if no option set,
download all scenes.

A minimum example:

    panoptic --path /Users/Shared/tmp --pose --scene "150821_dance1"

Download everything:

    panoptic --path /Volumes/data1/tmp --pose --vga 240 --hd 30

Help:

    panoptic -h
