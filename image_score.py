import cv2
import imquality.brisque as brisque
import PIL.Image
import time

# im = PIL.Image.open("sample1.jpg")
# print(brisque.score(im))
# im = PIL.Image.open("sample1_compressed.jpg")
# print(brisque.score(im))

# im = PIL.Image.open("sample2.jpg")
# print(brisque.score(im))

path = "sample1.jpg"
img = PIL.Image.open(path)
img = img.convert('RGB')
start = time.time()
print(brisque.score(img))
end = time.time()
print("time taken: ", end-start)
