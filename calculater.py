#Calculater

#if you want to run sth over and over agian, you could start a function
def add(x,y):
    c = x+y #
    print("{} + {} = {}".format(x,y,c))
    return c

def substract(x,y):
    c = x-y #
    print("{} - {} = {}".format(x,y,c))
    return c

def multiply(x,y):
    c = x*y #
    print("{} * {} = {}".format(x,y,c))
    return c

x = input("Enter a letter:") #stop and wait the input
print("You entered {}".format(x))
if x == "a":
    z = add(200,2)
    if z > 100:
        print("This is a number is too high")
elif x == "s":
    z = substract(4,5)
    if z > 100:
        print("This is a number is too high")
elif x =="m":
    z = multiply(200,5)
    if z > 100:
        print("This is a number is too high")
else:
    print("The {} command is not recognized.".format(x))
print("Done")
