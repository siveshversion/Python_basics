
#Immutable Types 
# 1.Strings 2.Tuples 3. Integers 4.Floats 5. Booleans 6. Frozen sets

a= "Hello"
b= a
a+= "world"
print(f"a:{a}")
print(f"b:{b}")
print(id(a))
print(id(b))