# # myarr = [10, 30, 10,10, 30, 40,40,40]
# # freq = {}
# # count = 0
# # for item in myarr:
# #     if (item in freq):
# #         freq[item] += 1
# #     else:
# #         freq[item] = 1
# #
# # for key, value in freq.items():
# #     if value>1:
# #         count+=value//2
# # # print(freq)
# # print("Pairs : ",count)
# #
#
#
# x = 'ababa'
#
# # def getPairsCount(arr, n):
# #     count = 0  # Initialize result
# #     stri = ''
# #     myli=[]
# #     # Consider all possible pairs
# #     # and check their sums
# #     for i in range(0, n):
# #
# #         for j in range(i+1, n):
# #
# #                 me =arr[i]+arr[j]
# #                 for k in range(j+1,n):
# #                     me+=arr[k]
# #                 myli.append(me)
# #                 count += 1
# #
# #     print(myli.count('aba'))
# #
# # getPairsCount(x, 5)
#
# #
# strin = 'AABCAAADA'
# def merge_the_tools(string):
#     l=[]
#     m=0
#     k=3
#     for i in range(len(string)//3):
#         l.append(strin[m:m+k])
#         m+=k
#     print(l)
#     for v in l:
#         print(''.join(list(dict.fromkeys(list(v)).keys())))
#
# merge_the_tools(strin)
#
#
# # stock_prices = {
# #     'march1': 310.0,
# #     'march2': 200
# # }
# # print(stock_prices['march1'])
#
# #
# # class HashMap:
# #     def __init__(self):
# #         self.size = 10
# #         self.bucket = [None] * self.size
# #         # print(self.bucket)
# #
# #     def hashFunction(self, key):
# #         Hash = 0
# #         for x in key:
# #             Hash += ord(x)
# #             return Hash % self.size
# #
# #     def add(self, key, value):
# #         keyIndexHash = self.hashFunction(key)
# #         arr = [key, value]
# #         if self.bucket[keyIndexHash] is None:
# #             self.bucket[keyIndexHash] = list([arr])
# #             return True
# #         else:
# #             for pair in self.bucket[keyIndexHash]:
# #                 if pair[0] == key:
# #                     pair[1] = value
# #                 else:
# #                     pass
# #             self.bucket[keyIndexHash].append(arr)
# #             return True
# #
# #     def __setitem__(self, key, value):
# #         return self.add(key, value)
# #
# #     def print(self):
# #         print(self.bucket)
# #     def __str__(self):
# #         return f'{self.bucket}'
# #     def get(self,key):
# #         keyIndexHash = self.hashFunction(key)
# #         if self.bucket[keyIndexHash] is None:
# #             return None
# #         else:
# #             for pair in self.bucket[keyIndexHash]:
# #                 if pair[0]==key:
# #                     return pair[1]
# #             raise KeyError('Does not exist')
# #     def __getitem__(self,item):
# #         return self.get(item)
# #
# #     def delete(self, key):
# #         keyIndexHash = self.hashFunction(key)
# #         if self.bucket[keyIndexHash] is None:
# #             return None
# #         else:
# #             for i in range(0, len(self.bucket[keyIndexHash])):
# #                 self.bucket[keyIndexHash].pop()
# #                 return True
# #             return None
# #
# #
# # d = HashMap()
# # # d.add('name', 'sam')
# # d['name']='John'
# # d['email']='J@y.com'
# # print(d['name'])
# # d.delete('name')
# # print(d)
#
# # num = d.hashFunction('name')
# # print(num)
#
# # Python3 code to demonstrate
# # Merge Consecutive digits Strings
# # using regex() + join()
# import re
#
#
# # Initializing list
# # test_list = ['g', '1', '2', 'i', '5', 'b', '6', '7']
#
# # printing original list
# # print("The original list is : " + str(test_list))
#
# # Merge Consecutive digits Strings
# # using regex() + join()
# # res = re.findall('\d+|.',''.join(test_list))
#
# # printing result
# # print ("List after digit merge : " + str(res))
#
# class HashTable:
#     def __init__(self):
#         self.size = 11
#         self.bucket = [None] * self.size
#
#     def hashFxn(self, key):
#         hash = 0
#         for item in key:
#             hash += ord(item)
#             return hash % self.size
#
#     def insert(self, key, value):
#         idx = self.hashFxn(key)
#         arr = [key, value]
#         if self.bucket[idx] is None:
#             self.bucket[idx] = list([arr])
#             self.bucket[idx].append(arr)
#         else:
#             for pair in self.bucket[idx]:
#                 if pair[0] == key:
#                     pair[1] = value
#                 else:
#                     pass
#
#             return True
#
#     def __setitem__(self, key, value):
#         return self.insert(key, value)
#
#     def print(self):
#         print(self.bucket)
#
#     def getValue(self, key):
#         idk = self.hashFxn(key)
#         if self.bucket[idk] is None:
#             return None
#         else:
#             for pair in self.bucket[idk]:
#                 if pair[0] == key:
#                     return pair[1]
#                 else:
#                     pass
#             raise KeyError('Key doesnt exist')
#
#
# # k = HashTable()
# #
# # k.insert('John', '675234')
# # k.print()
# # print(k.getValue('John'))
# word1 = 'abcd'
# word2 = 'dcda'
#
#
#
#
# def merging(word1, word2):
#     count = 0
#     li = ''
#     while word1 and word2:
#         if word1 > word2:
#             li+=word1[0]
#             word1 = word1[1:]
#
#         else:
#             li+=word2[0]
#             word2 = word2[1:]
#
#     li+=word1
#     li+=word2
#     print(li)
# # merging(word1,word2)
#
# x = [1,2,1,3,4,2]
#
# def sol(x):
#     arr = []
#     m = 0
#     k = 3
#
#     for i in range(len(x)-2):
#         # arr.append(x[m:m+k])
#         if x[i]<x[i+1]>x[i+2] or x[i]>x[i+1]<x[1+2]:
#             arr.append(1)
#         else:
#             arr.append(0)
#             m+=1
#     return arr
#
#
#
# # print(sol(x))
#
# def order(A):
#     if A == sorted(A):
#         return True
#     elif A == sorted(A,reverse=True):
#         return False
#
#
# def solution(a):
#     b=[]
#     for i in range(len(a)):
#         b=a
#         if len(a)<=1:
#             return True
#         elif len(a)>=1 and len(a)<=2:
#             if order(a):
#                 return True
#             else:
#                 return False
#         elif len(a)>=1 and len(a)<=3:
#             b[2]=a[1]
#             print(b)
#             print(a)
#             if order(b):
#                 return True
#             else:
#                 return False
#         elif len(a) >= 1 and len(a) <= 4:
#             b[3] = a[2]
#             b[2] = a[1]
#
#             if order(b):
#                 return True
#             else:
#                 return False
#         elif len(a) >= 1 and len(a) <= 5:
#             b[4] = a[2]
#             b[3] = a[2]
#             b[2] = a[1]
#
#             if order(b):
#                 return True
#             else:
#                 return False
#         elif len(a) >= 1 and len(a) <= 6:
#             b[5] = a[3]
#             b[4] = a[2]
#             b[3] = a[2]
#             b[2] = a[1]
#
#             if order(b):
#                 return True
#             else:
#                 return False
#         elif len(a) > 6:
#             b[5] = a[-3]
#             b[4] = a[2]
#             b[3] = a[-2]
#             b[2] = a[1]
#             b[1] = a[-1]
#
#             if order(b):
#                 return True
#             else:
#                 return False
# a=[1,7,5,2]
# # print(order(a))
# print(solution(a))
#
print(True or False and False)
r= lambda q:q*2
s= lambda q:q*3
x=2
x=r(x)
x=s(x)
x=r(x)
print(x)
x=1
print(all([2,4,0,6]))
import math
# math.pow(x,y,z)

print(round(4.576))

import math

x=2
y=3
z=4
print(math.pow(x,y,z))