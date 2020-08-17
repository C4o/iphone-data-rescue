import cv2
from scipy import ndimage
import os
import sys

def make_dir(filename):
    dir_path = os.path.dirname(filename)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

'''
slower version
def Mov2jpg(filename, dir_file, output_tag, sampling_rate = 10**10):
    #filename = 'IMG_3435.MOV'
    vidcap = cv2.VideoCapture(filename + '.MOV')
    success, image = vidcap.read()
    count = 0
    name_count = 0
    while success:
        if count%sampling_rate == 0:
            name_count +=1
            rotated = ndimage.rotate(image, 270)
            savename = "%s%s_%04d.jpg" % (dir_file + output_tag, filename[:-4], + name_count)
            print("saving %s" %(savename))
            make_dir(savename)
            cv2.imwrite(savename, rotated)
        count += 1
'''

def each_mov2jpg(filename, dir_file, output_tag, sampling_rate = 20):
    print filename
    vidcap = cv2.VideoCapture(dir_file + filename)
    len_frame = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    name_count = 0
    for i in range(1, len_frame, sampling_rate):
        vidcap.set(cv2.CAP_PROP_POS_FRAMES, i)
        success, image = vidcap.read()
        name_count +=1
        try:
            rotated = ndimage.rotate(image, 270)
            savename = "%s%s.jpg" % (dir_file + output_tag, filename[:-4])
            if os.path.isfile(savename):
                print('already exists %s' %(savename))
            else:
                print("saving %s" %(savename))
                make_dir(savename)
                cv2.imwrite(savename, rotated)
            break
        except RuntimeError:
            print("Cannot process %s" %(savename))
            pass
        
def main():
    video_path = sys.argv[1]
    files = [f for f in os.listdir(video_path) if os.path.isfile(os.path.join(video_path, f))]
    print files
    mov_files = [f for f in files if f[-4:] == '.MOV' or f[-4:] == '.mov']
    print mov_files
    for f in mov_files:
        print "1"
        each_mov2jpg(f, video_path,'photo/')
        
if __name__ == '__main__':
      main()