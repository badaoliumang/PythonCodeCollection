#声明树的高度
height = 5
#树的雪花数，初始为1
stars = 1
#以数的高度作为循环次数

for i in range(height):
    print((' ' * (height - i)) + ('*' * stars))
    stars += 2
#输出树干
print((' ' * height) + '|')
