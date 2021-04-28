#產生一個隨機整數1~100
#讓使用者重複輸入數字去猜
#猜對的話 印出 "終於猜對了!"
#猜錯的話 要告訴他 比答案大/小

import random
ans_min = eval(input('請決定要猜數字的最小值: '))
ans_max = eval(input('請決定要猜數字的最大值: '))
ans = random.randint(ans_min, ans_max)
count = 0

while True:
	count += 1
	print('這是你猜的第', count, "次!")
	guess = eval(input('請輸入一個數字{}~{}:'.format(ans_min, ans_max)))
	if guess == ans:
		print("終於猜對了!")
		break
	else:
		if guess > ans:
			print(' ')
			ans_max = guess - 1
		else:
			print(' ')
			ans_min = guess + 1

