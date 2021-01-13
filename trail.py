import os
from PIL import Image
from shutil import copyfile
from tqdm import tqdm

framesCount = 0
d = "src"
r = "result"

if not os.path.exists("src/"):
	os.makedirs("src/") 
if not os.path.exists("result/"):
	os.makedirs("result/") 

for path in os.listdir(d):
    if os.path.isfile(os.path.join(d, path)):
        framesCount += 1
print ("\nFrames count: " + str(framesCount) + "\n")

copyfile(r'src\1.png', r'result\1.png')
curFrame = 1
resultPath = "result/"
srcPath = "src/"
for i in tqdm(range(framesCount-1)):
	background = Image.open(resultPath + str(curFrame) + ".png")
	foreground = Image.open(srcPath + str(curFrame+1) + ".png")
	curFrame += 1
	Image.alpha_composite(background, foreground).save(resultPath + str(curFrame) + ".png")
os.system('pause')
