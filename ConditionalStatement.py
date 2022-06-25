# This is conditional statement
stock = int(input("Enter Number"))
i = 1
while i <= stock:
    if i > 10:
        break
    if i % 2 == 0:
        i = i + 1
        continue
    print(i)
    i = i + 1
print("End")

for i in range(1,101):
    if i%3==0:
        pass
    else:
        print(i)
