import cv2
import os

num = 0

all_jumps = os.listdir("C:/Users/fawaz/Videos/ValoGun/jumping")
print(all_jumps)

def breakVideo(file_path):
    global num
    capture = cv2.VideoCapture(file_path)
    while(True):
        success, frame = capture.read()

        scale_percent = 99.98
        crop_percent = .3

        if success:
            print(frame.shape)
            width = frame.shape[0]
            height = frame.shape[1]
            
            frame = frame[int(width*crop_percent):int(width - width*crop_percent), int(height*crop_percent):int(height - height*crop_percent)]
            
            resized = cv2.resize(frame, (64, 64), interpolation=cv2.INTER_AREA)
            cv2.imwrite(f'C:/Users/fawaz/Pictures/valo_gun/sample_run/frame_' + str(num) + '.png', resized)
        else:
            break

        num += 1

        if(num > 200):
            break

    capture.release()

    pass


        


for jump in all_jumps:
    breakVideo("C:/Users/fawaz/Videos/ValoGun/jumping/" + jump)

#breakVideo("C:/Users/fawaz/Videos/ValoGun/standing.mp4")

