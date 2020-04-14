# Character Frequency 
string = input("Enter the string:-")
all_freq = {} 

for i in string: 
	if i in all_freq: 
		all_freq[i] += 1
	else: 
		all_freq[i] = 1
print (str(all_freq)) 