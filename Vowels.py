
# Vowels Finder
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
list1 = [ ]
vowels = ('a', 'e', 'i', 'o', 'u','A','E','I','O','U')
for state in state_name:
    for letter in state:
         if letter in vowels:
            state = state.replace(letter,"")
    list1.append(state)
print(list1)

# with the help of the while loop
state_name1 = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
list2 = []
i=0
while i<len(state_name1):
    state1 = state_name1[i]
    i=i+1
    x=0
    while x<len(state1):
        letter1 = state1[x]
        if letter1 in vowels:
            state1 = state1.replace(letter1,"")
        x=x+1
    list2.append(state1)
print(list2)