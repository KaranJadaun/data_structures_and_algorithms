#1
# # use bin function to get the binary representation of any number
# use format(12,"b") to get exact binary representation
# print(bin(23)) 

#2
# calculate multiple of 3 in a efficient method
# loop while num!=0, if left most bit it 1 then odd+=1
# if left most bit is 0 then even += 1
# def ismultipleof3(num):
#     odd = 0
#     even = 0
#     if (num<0): num = -num
#     if (num==0): return 1
#     if (num==1): return 0
#     while (num):
#         if (num&1): odd += 1
#         if (num&2): even += 1
#         num = num>>2
#     return ismultipleof3(abs(odd-even))
# print("yes" if ismultipleof3(24) else "no")

#3
# calculte the efficient way to multiply with 7
# you can multiply any number just left shift the number to the
# nearest perfect square and minus remaining number
# def multiplybyseven(num):
#     return ((num<<3)-num)
# print(multiplybyseven(4))

#4 pending
# lucky number are those numbers in which we have to 
# remove every second number then remove every third number
# and continue the process till length
# arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# count = 2
# for i in range(1,len(arr)):
#     for j in range(1,len(arr)):
#         if j%count==0:
#             arr.remove(arr[j])
#         count += 1
# print(arr)

#5
# find the square root of a number
# def squareroot(num):
#     x = num
#     y = 1
#     e = 0.00001
#     while (x-y > e):
#         x = (x+y)/2
#         y = num/x
#     return x
# print(squareroot(int(input())))

#6
# find fibonacci numbers
# def fibonacci(num, second_last, last):
#     if num-1==0: return second_last
#     else:
#         new_last = second_last + last
#         second_last = last
#         return fibonacci(num-1, second_last, new_last)
# print(fibonacci(1,0,1))

#7
# 
