a = 1
say = True
while say:
    print(a)
    a += 1
    if a == 10000:
        say = False
        print(a)

for i in range(15):
    print ("NZ has " + str(i+1) + " balls")

balls = int(input("How many balls did NZ lose "))

print ("NZ has " + str(i+1 - balls) + " balls")

test = 1
print(test)