import numpy as np
import cv2
import math
import time
import random 

cap = cv2.VideoCapture(0)

class Snake():
	head = [200,200]
	len = 2
	tail = []
	ang = 180
    
	def initTail(snake):
		for i in range(0, snake.len):
			snake.tail.append([snake.head[0] - int(math.sin(snake.ang*math.pi/180)*16*(i+1)),snake.head[1] + int(math.cos(snake.ang*math.pi/180)*16*(i+1)) ])
			
	def updateTale(snake):
		for i in range(snake.len-1, -1, -1):
			if i == 0:
				snake.tail[i] = [snake.head[0], snake.head[1]]
			else:
				snake.tail[i] = [snake.tail[i-1][0], snake.tail[i-1][1]]
	
	def hasCrashed(snake):
		for i in range(0, snake.len):
			for j in range(0, snake.len):
				if i != j and snake.tail[i][0] == snake.tail[j][0] and snake.tail[i][1] == snake.tail[j][1]:
					return True
		return False
				

last = 0
new = 0
food = [100,100,5]
snake = Snake()
snake.initTail()

def DrawFood(img):
	cv2.circle(img,(food[0],food[1]), food[2], (0,0,255), -1)
	

def DrawSnake(img):	
	for var in snake.tail:
		cv2.circle(img,(var[0],var[1]), 8, (170,0,170), -1)
	
	cv2.circle(img,(snake.head[0],snake.head[1]), 10, (255,0,255), -1)
	cv2.circle(img,(snake.head[0]- int(math.cos(snake.ang*math.pi/180)*3),snake.head[1]- int(math.sin(snake.ang*math.pi/180)*3)), 3, (0,170,0), -1)
	cv2.circle(img,(snake.head[0]+ int(math.cos(snake.ang*math.pi/180)*3),snake.head[1]+ int(math.sin(snake.ang*math.pi/180)*3)), 3, (0,170,0), -1)


	
#function to get the time between each frame
lastFrameTime = int(round(time.time() * 1000))
def FrameDeltaTime():
	global lastFrameTime
	delta = int(round(time.time() * 1000)) - lastFrameTime
	lastFrameTime = int(round(time.time() * 1000))
	return delta
	
	
timer = 0
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	new = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	new = cv2.flip(new,1)
	
	#Calculate game logic below
	diff = new.copy()
	cv2.absdiff(last, new, diff)
	diff = cv2.medianBlur(diff,5)
	if np.amax(diff) > 100:
		ret3,diff = cv2.threshold(diff,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	else:
		diff = diff - diff
	
	h, w = diff.shape[:2]
	start_row, start_col = int(0), int(0)
	end_row, end_col = int(h), int(w*0.5)
	cropped_top = diff[start_row:end_row , start_col:end_col]
	leftSum = cv2.sumElems(cropped_top)
	
	start_row, start_col = int(0), int(w*0.5)
	end_row, end_col = int(h), int(w)
	cropped_bot = diff[start_row:end_row , start_col:end_col]
	rightSum = cv2.sumElems(cropped_bot)

	
	#Update Snake Pos
	timer += FrameDeltaTime()
	if timer > 700:
		if leftSum[0]*0.8 > rightSum[0] :
			snake.ang -= 90
		elif rightSum[0]*0.8 > leftSum[0]:
			snake.ang += 90
		timer = 0
		snake.updateTale()
		snake.head[0] += int(math.sin(snake.ang*math.pi/180)*16)
		snake.head[1] -= int(math.cos(snake.ang*math.pi/180)*16)
	
	#check for food eaten
	if abs(snake.head[0]-food[0]) < 10 and abs(snake.head[1]-food[1]) < 10:
		snake.len += 1
		food = [random.randint(10, h-10), random.randint(10, h-10), 5]
		snake.tail.append([snake.head[0],snake.head[1]])
		
	#reset images and draw game
	last = new.copy()
	draw = new.copy()
	draw = cv2.cvtColor(draw,cv2.COLOR_GRAY2RGB)
	
	overlay = draw.copy()
	
	if leftSum[0]*0.8 > rightSum[0] :
		start_row, start_col = int(0), int(0)
		end_row, end_col = int(h), int(w*0.5)
		cv2.rectangle(overlay, (start_col, start_row), (end_col, end_row), (0, 255, 0), -1)
	elif rightSum[0]*0.8 > leftSum[0]:
		start_row, start_col = int(0), int(w*0.5)
		end_row, end_col = int(h), int(w)
		cv2.rectangle(overlay, (start_col, start_row), (end_col, end_row), (0, 255, 0), -1)
	cv2.addWeighted(overlay, 0.1, draw, 1 - 0.1, 0, draw)
	
	DrawFood(draw)
	DrawSnake(draw)
	
	if snake.head[0] > w or snake.head[0] < 0 or snake.head[1] > h or snake.head[1] < 0 or snake.hasCrashed():
		print ("You lose! You got " + str(snake.len-2) + " points!")
		break
	
	# Display the resulting frame
	cv2.imshow('Diff',diff)
	cv2.imshow('Game',draw)
	#cv2.imshow('frame',draw)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
