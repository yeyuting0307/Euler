# https://projecteuler.net/problem=119

# The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. Another example of a number with this property is 614656 = 28^4.

# We shall define an to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.

# You are given that a2 = 512 and a10 = 614656.

# Find a30.

#%%

# Way 1 : tooooooooooo slooooooooooow
# i = 1
# num = 10
# a = []

# while i <= 30 :
#     if num % 10**6 == 0:
#         print(num)
#     split_sum = sum([int(s) for s in str(num)])
#     temp = num
#     while temp % split_sum == 0 and split_sum != 1:
#         temp = temp // split_sum
#         if temp == 1:
#             print('a%s:'% i, num)
#             a.append(num)
#             i += 1
#             break
#     num += 1
    

#%%
# Way 2
a = []
for base in range(2, 100):
    b = base
    for x in range(2, 10):
        num = b ** x
        if sum(int(s) for s in str(num)) == b:
            print(num)
            a.append(num)
a.sort()
print(a[30-1])







#%%
