from tqdm import tqdm
import requests
import os
import sys

scenes = [
    "171204_pose1",
    "171204_pose2",
    "171204_pose3",
    "171204_pose4",
    "171204_pose5",
    "171204_pose6",
    "171026_pose1",
    "171026_pose2",
    "171026_pose3",
    "161202_haggling1",
    "160422_haggling1",
    "160226_haggling1",
    "160224_haggling1",
    "160422_ultimatum1",
    "160226_ultimatum1",
    "160224_ultimatum1",
    "160224_ultimatum2",
    "151125_ultimatum1",
    "160422_mafia1",
    "160422_mafia2",
    "160226_mafia1",
    "160226_mafia2",
    "160224_mafia1",
    "160224_mafia2",
    "151125_mafia",
    "150821_dance1",
    "150821_dance2",
    "150821_dance3",
    "150821_dance4",
    "150821_dance5",
    "160317_moonbaby1",
    "160317_moonbaby2",
    "160317_moonbaby3",
    "160906_band1",
    "160906_band2",
    "160906_band3",
    "160906_band4",
    "150406_drum3",
    "150406_drum4",
    "150406_drum5",
    "150406_drum6",
    "150406_drum7",
    "150303_celloScene1",
    "150303_celloScene2",
    "150303_celloScene3",
    "150303_celloScene4",
    "150209_celloCapture1",
    "150209_celloCapture2",
    "160906_ian1",
    "160906_ian2",
    "160906_ian3",
    "160906_ian5",
    "160401_ian1",
    "160401_ian2",
    "160401_ian3",
    "131015_extra",
    "131015_extra2",
    "131015_baseball",
    "131015_baby1",
    "131015_baby2",
    "160906_pizza1",
    "160317_meeting1",
    "151125_bang",
    "150129_007game",
]


def download_file(url, fname):
    response = requests.get(url, stream=True)
    status = response.status_code

    if status != 200:
        print("Status {}: {}".format(status, url), file=sys.stderr)
        return

    total_size = int(response.headers.get('content-length', 0))
    chunk_size = 1024
    total = total_size//chunk_size
    os.makedirs(os.path.dirname(fname), exist_ok=True)

    with open(fname, "wb") as fid:
        print("Downloading: {}".format(fname))
        for chunk in tqdm(response.iter_content(chunk_size),
                          total=total, unit='KB', unit_scale=False):
            if chunk:
                fid.write(chunk)
