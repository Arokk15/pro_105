import os
import cv2


images=[]

img_files=[]

image_ext=[".jpge",".jpg",".png",".gif"]

for i in os.listdir("image"):
    root,ext=os.path.splitext(i)
    images.append(i)
    if ext in image_ext:
        img_files.append("image/"+i)    

print(images)
print()
print(img_files)

size=(500,500)
video_fm="project_c105.avi"
forcecc=cv2.VideoWriter_fourcc(*"DIVX")
fps=0.8
si=size
out=cv2.VideoWriter(video_fm,forcecc,fps,si)

for i in range(len(images)):
    img=cv2.imread(img_files[i])
    out.write(img) 
print("don")

