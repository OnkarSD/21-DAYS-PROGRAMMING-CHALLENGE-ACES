#SINGLE NUMBER

#1.APPROCH OF HASHMAP

dict = {}

for i in nums:
	
	if i in dict:
		dict[i] += 1
	else:
		dict[i] = 1

for i,v in dict.items():
	if v==1:
	return i

#2APPROCH OF XOR

r = 0

for i in nums:
	r ^= i

return r
