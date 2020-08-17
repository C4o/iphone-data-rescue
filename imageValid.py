# coding=utf-8

# python x.py images-path valid-images-path invalid-images-path

# pip install opencv-python
import cv2
import os
import sys
import time
import shutil

def move2dir(imagePath, imageName, path):
	try:
		shutil.move(imagePath + "/" + imageName, path + "/" + imageName)
	except:
		print "[*] move file %s error." % (imagePath + "/" + imageName)

def imagesCV(imagePath, imageName, validPath, invalidPath):
	image = cv2.imread(imagePath + "/" + imageName)
	try:
		img2gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		move2dir(imagePath, imageName, validPath)
	except:
		move2dir(imagePath, imageName, invalidPath)

if __name__ == '__main__':

	types4 = [".png", ".jpg", ".PNG", ".JPG"]
	types5 = [".jpeg", "JPEG"]
	imagePath = sys.argv[1]
	validPath = sys.argv[2]
	invalidPath = sys.argv[3]
	files = os.listdir(imagePath)
	nums = len(files)
	print '[*] {} files found...'.format(nums)
	done = 0
	for file in files:
		if not os.path.isdir(file) and ((file[-4:] in types4) or (file[-5:] in types5)):
			imagesCV(imagePath, file, validPath, invalidPath)
		done += 1
		sys.stdout.write('{}/{}'.format(done, nums) + '\r')
		sys.stdout.flush()

