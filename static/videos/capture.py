from pickletools import uint8
import os, cv2
from tqdm import tqdm
import json

exp = "teaser1"

os.system('ffmpeg -i %s.mp4 -filter:v "crop=x=0:y=30:w=1920:h=1020" -c:a copy %s-cropped.mp4' % (exp, exp))
