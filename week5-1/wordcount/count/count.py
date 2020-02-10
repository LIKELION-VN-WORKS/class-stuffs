
example_string = 'I am a man of fortune, I must seek my fortune'

spliting_string = example_string.split(' ')

dic = {}

for i in spliting_string:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)
