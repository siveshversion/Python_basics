#Example 1

numlist = [1,3,5]
doubled = []

#without list comprehension

for x in numlist:
    doubled.append(x**2)

print(doubled)


#with list comprehension
doubled = [x**2 for x in numlist]

print(doubled)


#Example 2 

cricketers = ["sachin","shewag","sunil","dhoni"]
seniorPlayers = []

#without list comprehension with a conditional statement
for x in cricketers:
    if(x.startswith('s')):
     seniorPlayers.append(x)

print(seniorPlayers)

#with list comprehension with a conditional statement

seniorPlayers = [x for x in cricketers if x.startswith('s') ]
print(seniorPlayers)