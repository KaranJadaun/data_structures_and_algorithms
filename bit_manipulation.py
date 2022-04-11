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

#4
# lucky number are those numbers in which we have to 
# remove 
