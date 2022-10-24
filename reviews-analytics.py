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



# my code using while loop
i = 0
summary = 0
while i <= (len(data)-1):
	all_len.append(len(data[i]))
	summary = summary + len(data[i])
	i +=1


print(summary)
print(summary/len(data))
print(max(all_len))
print(min(all_len))



#Allen's code using for loop (simpler)
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print(sum_len)
print(sum_len/len(data))



