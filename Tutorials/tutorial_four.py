# Student Name:     Dylan Murray
# Student Number:   121747725
# Tutorial 4: Args and Kwargs

def adder(x,y,z):
    print("sum:",x+y+z)

#adder(10,12,13)         #Output = Sum: 35
#adder(5,10,15,20,25)    #Output = TypeError: adder() takes 3 positional arguments but 5 were given

# Using for loop in function to iterate through any size list to get sum using args
def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

# adder(3,5)
# adder(4,5,6,7)
# adder(1,2,3,5,6)

# Kwargs by default creates a dictionary 
def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

#keys are determined in function call.
intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

'''
Things to Remember:

*args and **kwargs are special keyword which allows function to take variable length argument.

*args passes variable number of non-keyworded arguments and on which operation of the tuple can be performed.

**kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.

*args and **kwargs make the function flexible.
'''