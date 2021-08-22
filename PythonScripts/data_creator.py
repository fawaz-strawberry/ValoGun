'''
The following script takes in a video file, and directory with videos containing
green screen backgrounds.
It then will split the video into individual frames.
Then it will randomly apply crops, and shifts to each frame, maybe even mess
with the lighting

python data_creator.py -f "C:/Users/fawaz/Videos/ValoGun/latest_vids/standing/standing_0.mp4" -g "C:/Users/fawaz/Pictures/GreenScreenBackdrops/" -o "C:/Users/fawaz/Videos/ValoRedScreen_2/train/Standing/"
'''

import argparse
import cv2
import os
import random
import numpy as np
from numpy.core.fromnumeric import resize

parser = argparse.ArgumentParser(description='The following script takes in a video file, and directory with videos containing\ngreen screen backgrounds.\nIt then will split the video into individual frames\nrandomly apply crops, and shifts to each frame, maybe even mess\nwith the lighting')

parser.add_argument("-f", "--video_file", help="Video File to be framed")
parser.add_argument("-g", "--green_screens", help="Directory of images to use in green screen")
parser.add_argument("-o", "--output_directory", help="Directory to save file images")
args = parser.parse_args()

video_file = args.video_file
green_screens = args.green_screens
output_directory = args.output_directory

#Frame Number We're On
num = 0

all_backdrops = os.listdir(green_screens)
pop_later = []
for i in range(len(all_backdrops)):
    if(all_backdrops[i].find(".gif")):
        pop_later.append(i)

for i in range(len(pop_later)-1, 0, i-1):
    print("Pop")
    print(len(all_backdrops))
    print(pop_later[i])
    all_backdrops.pop(pop_later[i])

#Take video and chop into frames
def breakVideo(file_path, output_path):
    global num
    capture = cv2.VideoCapture(file_path)
    while(True):
        success, frame = capture.read()

        if success:
            frame_modified = randomizeFrame(frame)
            cv2.imwrite(str(output_path) + 'frame_' + str(num) + '.png', frame_modified)
        else:
            break

        num += 1

    capture.release()

    pass

def randomizeFrame(frame, crop_range=[0, .2]):
    crop_percent = crop_range[0] + (crop_range[1] - crop_range[0]) * random.random()

    width = frame.shape[0]
    height = frame.shape[1]

    try:
        frame = frame[int(width*crop_percent):int(width - width*crop_percent), int(height*crop_percent):int(height - height*crop_percent)]
        resized = cv2.resize(frame, (64, 64), interpolation=cv2.INTER_AREA)

        selection = random.randint(0, len(all_backdrops))
        image = cv2.imread(green_screens + all_backdrops[selection])
        image = cv2.resize(image, (64, 64))

        u_green = np.array([106, 68, 240])
        l_green = np.array([18, 0, 122])
    
        mask = cv2.inRange(resized, l_green, u_green)
        res = cv2.bitwise_and(resized, resized, mask = mask)
    
        f = resized - res
        f = np.where(f == 0, image, f)
        
        return resized

    except:
        print("Error when resizing something")
        resized = cv2.resize(frame, (64, 64), interpolation=cv2.INTER_AREA)
        return resized
    
    






breakVideo(video_file, output_directory)