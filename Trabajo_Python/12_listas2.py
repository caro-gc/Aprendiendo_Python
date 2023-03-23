num = [99, 34, 25, 56, 72]
print(num)
num[1] = 88
print(num)
# num = [99, 88, 25, 56, 72]
# FUNCIÓN INSERT.
num.insert(1, 77)
print(num)
# num = [99, 77, 88, 25, 56, 72]
# FUNCIÓN APPEND:
num.append(100)
print(num)
# num = [99, 77, 88, 25, 56, 72, 100]
num2 = [9, 8, 7]
print(num)
# FUNCIÓN EXTEND:
num.extend(num2)
print(num)
# num = [99, 77, 88, 25, 56, 72, 100, 9,8,7]
# FUNCIÓN REMOVE:
num.remove(100)
print(num)
# num = [99, 77, 88, 25, 56, 72, 9, 8, 7]
# FUNCIÓN POP:
num.pop(2)
print(num)
# num = [99, 77, 25, 56, 72, 9, 8, 7]
# FUNCIÓN DEL
del num[0]
print(num)
# num = [77, 25, 56, 72, 9, 8, 7]
# FUNCIÓN CLEAR:
num2.clear()
print(num2)



