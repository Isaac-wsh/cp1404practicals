for i in range(1, 21, 2):
    print(i, end=' ')
print()

#a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#c
star_num = int(input("Number of stars: "))
for i in range(star_num):
    print("*", end='')
print()

#d
star = int(input("Number of stars: "))
for j in range(1, star + 1):
    for k in range(j):
        print("*", end='')
    print()