import cv2

# configurable paramters
source = "sunit.png"
destination = "NewSunit.png"
scale_percent = 50

src = cv2.imread(source,cv2.IMREAD_UNCHANGED)
# cv2.imshow("title",src)

# Percent by which the image is resized

# Calculate the 50 percent of original dimensions
width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

# Dsize
dsize = (width, height)

# Resize image
output = cv2.resize(src, dsize)

cv2.imwrite(destination, output)
# cv2.waitKey(0)