import time
import random as r

words_list = ['list', 'love', 'cat', 'dog', 'head', 'at', 'on', 'like', 'dad', 'find', 'plane', 'drive', 'six', 'good',
              'worse', 'nine', 'horse', 'including', 'school', 'lawyer', 'kids', 'super', 'a', 'an', 'dream', 'toy', 'universe',
              'one', 'friends', 'family', 'bomb', 'flower', 'peace', 'world', 'ecology']

x = r.randint(9, 15)
nes_list = []
for i in range(x):
    a = r.randint(0, len(words_list) - 1)
    nes_list.append(words_list[a])

answer = ""
neceserry_words = ''

for el in nes_list:
    neceserry_words += str(el) + ' '

neceserry_words = neceserry_words[0:-1]

a = ''
while a != 'start':
    print("You'll have three second to prepare")
    print("You'll see the phrase when you start")
    print("If you made a mistake, the task won't be completed")
    a = input('Write -start- to start \n')

time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print(neceserry_words)
print('START')

starttime = time.time()
lasttime = starttime

while answer.lower() != neceserry_words:
    answer = input()
    laptime = round((time.time() - lasttime), 2)
    totaltime = round((time.time() - starttime), 2)
    lasttime = time.time()

time_for_one_word = totaltime / len(nes_list)

print("Total Time: " + str(totaltime))
print(f'Symbols: {len(neceserry_words)}')
print(f'Words: {len(nes_list)}')
print(f'WPM: {60 // time_for_one_word}')
print("_" * 20)
