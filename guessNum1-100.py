#產生一個隨機整數1~100
#讓使用者重複輸入數字去猜
#猜對的話 印出 "終於猜對了!"
#猜錯的話 要告訴他 比答案大/小

import random
ans = random.randint(1, 100)

while True:
	guess = eval(input('請輸入一個數字1~100:'))
	if guess == ans:
		print("終於猜對了!")
		break
	else:
		if guess > ans:
			print('猜錯了，猜得比答案還大!')
		else:
			print('猜錯了，猜得比答案還小!')
