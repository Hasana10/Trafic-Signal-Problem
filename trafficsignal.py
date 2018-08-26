import cv2


car_cascade = cv2.CascadeClassifier('cars.xml')

bike_cascade = cv2.CascadeClassifier('bike.xml')





# im1 = cv2.imread('trafficimages/car1.jpg')
im1 = cv2.imread('bk4.png')
im2 = cv2.imread('cb1.jpg')
im3 = cv2.imread('cb2.jpg')
im4 = cv2.imread('ck1.jpg')


#for image 1
gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
	# Detects cars of different sizes in the input image
cars = car_cascade.detectMultiScale(gray, 1.1, 1)
	# To draw a rectangle in each cars
# for (x,y,w,h) in cars:
# 	cv2.rectangle(im1,(x,y),(x+w,y+h),(0,0,255),2)
bikes = bike_cascade.detectMultiScale(gray, 1.01, 1)
	# To draw a rectangle in each cars
# for (x,y,w,h) in bikes:
# 	cv2.rectangle(im1,(x,y),(x+w,y+h),(0,0,255),2)
var1 = len(cars)+len(bikes)
#for image 2

gray = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)
	# Detects cars of different sizes in the input image
cars = car_cascade.detectMultiScale(gray, 1.1, 1)
	# To draw a rectangle in each cars
# for (x,y,w,h) in cars:
# 	cv2.rectangle(im2,(x,y),(x+w,y+h),(0,0,255),2)
bikes = bike_cascade.detectMultiScale(gray, 1.01, 1)
	# To draw a rectangle in each cars
# for (x,y,w,h) in bikes:
# 	cv2.rectangle(im1,(x,y),(x+w,y+h),(0,0,255),2)
var2 = len(cars)+len(bikes)

#for image3

gray = cv2.cvtColor(im3, cv2.COLOR_BGR2GRAY)
	# Detects cars of different sizes in the input image
cars = car_cascade.detectMultiScale(gray, 1.1, 1)
	# To draw a rectangle in each cars
# for (x,y,w,h) in cars:
# 	cv2.rectangle(im3,(x,y),(x+w,y+h),(0,0,255),2)
bikes = bike_cascade.detectMultiScale(gray, 1.01, 1)
	# To draw a rectangle in each cars
# for (x,y,w,h) in bikes:
# 	cv2.rectangle(im1,(x,y),(x+w,y+h),(0,0,255),2)
var3 = len(cars)+len(bikes)
#for image4

gray = cv2.cvtColor(im4, cv2.COLOR_BGR2GRAY)
	# Detects cars of different sizes in the input image
cars = car_cascade.detectMultiScale(gray, 1.1, 1)
	# To draw a rectangle in each cars
# for (x,y,w,h) in cars:
# 	cv2.rectangle(im4,(x,y),(x+w,y+h),(0,0,255),2)
bikes = bike_cascade.detectMultiScale(gray, 1.01, 1)
	# To draw a rectangle in each cars
# for (x,y,w,h) in bikes:
# 	cv2.rectangle(im1,(x,y),(x+w,y+h),(0,0,255),2)
var4 = len(cars)+len(bikes)
# print(var1)
# print(var2)
# print(var3)
# print(var4)

max = 0
flag = 0
if var1 > var2:
    max = var1
    flag = 1
else:
    max = var2
    flag = 2
if max < var3:
    max = var3
    flag = 3
else:
    if max < var4:
        max = var4 
        flag = 4
# print(max)


print("The lane " +str(flag)+ " is open")


cv2.imshow('image1',im1)
cv2.imshow('image2',im2)
cv2.imshow('image3',im3)
cv2.imshow('image4',im4)




cv2.waitKey(0)
cv2.destroyAllWindows()
