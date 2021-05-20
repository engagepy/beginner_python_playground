from datetime import datetime

alphabets = str(ascii)
a_list = list(alphabets)

print(a_list)

for i in range(len(alphabets)-1):
	a_list[i] = a_list.append(datetime.now())

print(a_list)


