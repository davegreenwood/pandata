"""
Download all the 3d Pose data from the CMU panopticum studio.
"""

from .utils import download_file
import os

# parts
body = "hdPose3d_stage1_coco19.tar"
face = "hdFace3d.tar"
hands = "hdHand3d.tar"
parts = [body, face, hands]


def get_pose(scene, part, path=""):
    base = "http://domedb.perception.cs.cmu.edu/webdata/dataset/{}/{}"
    url = base.format(scene, part)
    download_file(url, os.path.join(path, scene, part))
