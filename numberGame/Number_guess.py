# -*-coding:utf-8 -*-

from random import randint
import time


def avg(total, time):
    if time > 0:
        return float(total)/time
    else:
        return 0
# 计算平均

record = open("record")
lines = record.readlines()
record.close()
# 读取存档

name = raw_input("告诉我你的名字：")
scores = {}
for l in lines:
    s = l.split()
    scores[s[0]] = s[1:]

score = scores.get(name)
if score is None:
    score = [0, 0, 0, 0]

game_times = int(score[0])
min_times = int(score[1])
total_times = int(score[2])
min_time = int(score[3])
avg_times = avg(total_times, game_times)
print"你一共玩了%d次，最快用了%d轮，%d秒，平均每局%.2f轮。" % (game_times, min_times, min_time, avg_times)
# 存档分析

random_num = randint(1, 1000)
print "在1到1000之间猜一个数字吧："
timeStart = time.time()
guess = input(">>")
timer = 0
while guess != random_num:
    if guess < random_num:
        print "太小了"
        timer += 1
    if guess > random_num:
        print "太大了"
        timer += 1
    print "\n再试试？"
    guess = input(">>")

timeEnd = time.time()
used_time = timeEnd-timeStart
print "BINGO！你用了%d轮,%d秒猜到这个数字！" % (timer, used_time)

# 游戏主体

game_times += 1
total_times += timer
if min_times == 0 or timer < min_times:
    min_times = timer
avg_times = avg(total_times, game_times)
if min_time == 0 or used_time < min_time:
    min_time = used_time

print"你一共玩了%d次，最快用了%d轮，%d秒，平均每局%.2f轮。" % (game_times, min_times, used_time,  avg_times)

scores[name] = [str(game_times), str(min_times), str(total_times), str(used_time)]
result = ""
for n in scores:
    line = n + " " + " ".join(scores[n]) + "\n"
    result += line
# 临时存储

record = open("record", "w")
record.write(result)
record.close()
# 存档
