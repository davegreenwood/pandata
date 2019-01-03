from .utils import scenes as pscenes
from .pose import parts, get_pose
from .video import get_hd, get_vga
import argparse
import sys

usage = """
Download all the panoptic studio data:
Select one or more options for pose, vga or hd data
(Without at least one option nothing will download).
Smaller lists of scenes can be downloaded, or if no option set,
download all scenes.

A minimum example:
panoptic --path /Users/Shared/tmp --pose --scene "150821_dance1"

Download everything:
panoptic --path /Volumes/data1/tmp --pose --vga 240 --hd 30

Help:
panoptic -h

"""

parser = argparse.ArgumentParser(usage=usage)

parser.add_argument(
    "--path",
    default="",
    help="Path to save the data, default: current working directory.")

parser.add_argument(
    "--pose",
    action="store_true",
    help="Download the pose data if set True."
)

parser.add_argument(
    "--vga",
    type=int,
    default=0,
    help="Download the vga video data - number of cameras - max 240."
)

parser.add_argument(
    "--hd",
    type=int,
    default=0,
    help="Download the hd video data - number of cameras - max 30."
)

parser.add_argument(
    "--scene",
    type=str,
    default=None,
    nargs="*",
    help="Download specified scene - if not set, download all."
)


def download(scenes, path="", pose=False, vga=0, hd=0):
    for scene in scenes:
        if pose:
            for part in parts:
                get_pose(scene, part, path)
        get_vga(scene, vga, path)
        get_hd(scene, hd, path)


def test(path):
    print("Running test...")
    get_pose("171204_pose1", "hdPose3d_stage1_coco19.tar", path)


def main():
    args = parser.parse_args(args=None if sys.argv[1:] else ['--help'])
    scenes = args.scene if args.scene else pscenes
    download(scenes, path=args.path, pose=args.pose, vga=args.vga, hd=args.hd)
