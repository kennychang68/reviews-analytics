data = []
all_len = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count +=1
		if count % 10000 == 0:
			print(len(data))

print('the file has been read out, totally', len(data), 'messages')

#print(len(data[1]))
#print(data[1])

#all_len.append(len(data[0]))
#all_len.append(len(data[1]))
#all_len.append(len(data[2]))
#print(all_len)


# my code using while loop
i = 0
summary = 0
while i <= (len(data)-1):
	all_len.append(len(data[i]))
	summary = summary + len(data[i])
	i +=1

print(all_len[999999])
print(len(all_len))
print(summary)
print(summary/len(data))
print(max(all_len))
print(min(all_len))






