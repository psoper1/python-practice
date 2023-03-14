def sum(*nums):
    print("\nData type of argument:",type(nums))
    # print("sum:", x+y+z)
    sum = 0
    for num in nums:
        sum = sum + num

    print('Sum: ', sum)

sum(1,2,3) # sum: 6
# sum(2,3,4) # sum: 9
# sum(3,3,3,3,3,3,3) # sum: 21

# *args, **kwargs

def namer(**person):
    print("\nData type of argument:",type(person))

    for key, value in person.items():
        print("{} is {}".format(key,value))

namer(first='Tryon', last='Baldwin', age=25, dogs_name='Goodest Boy')