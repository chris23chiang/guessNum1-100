#產生一個隨機整數1~100
#讓使用者重複輸入數字去猜
#猜對的話 印出 "終於猜對了!"
#猜錯的話 要告訴他 比答案大/小

import random
ans = random.randint(1, 100)
count = 0

while True:
	count += 1
	print('這是你猜的第', count, "次!")
	guess = eval(input('請輸入一個數字1~100:'))
	if guess == ans:
		print("終於猜對了!")
		break
	else:
		if guess > ans:
			print('比答案還大!')
			print(' ')
		else:
			print('比答案還小!')
			print(' ')

