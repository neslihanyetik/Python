#!/usr/bin/env python
# coding: utf-8

# Problem :
# 
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# Input:
# 
# [1,2,3]
# 
# Output:
# 
# [
#   [1,2,3],
#   
#   [1,3,2],
#   
#   [2,1,3],
#   
#   [2,3,1],
#   
#   [3,1,2],
#   
#   [3,2,1]
#   
# ]

# In[ ]:


def permütasyon(n):
  l=[]
  y=0
  for i in n:
      x=n.index(i)
      z=n.index(i)
      l.append(n[x:]+n[:y])
      z=sorted(n,reverse=True)
      l.append(z[x:]+z[:y])
      y+=1
      k=sorted(l)     
  return k
print(permütasyon([1,2,3]))


# In[ ]:


listem=[]
gir_list = [1, 2, 3]
a,b,c=gir_list[0],gir_list[1],gir_list[2]
rakam=(str(a)+str(b)+str(c))
for i in [0,1,2]:
   for j in [0,1,2]:
      for k in [0,1,2]:
         text=rakam[i]+rakam[j]+rakam[k]
         listem.append(text)
listek=[]
for gas in range(len(listem)-1):listek.append(list(listem[gas]))
final_list=[o for o in listek if o.count(str(a))==1 and o.count(str(b))==1]
print(final_list)


# In[ ]:


lst = [1,2,3]
lst_new = []
for i in lst:
    for j in lst:
        for k in lst:
            if i != j and j != k and i != k:
                lst_new.append([i,j,k])
print(lst_new)


# In[ ]:


list1 = [1, 2, 3]
i = 1
fact = 1
while i < len(list1) + 1 :
    fact *= i
    i += 1
i = 1
fact_dict = {}
while i < fact + 1:
    fact_dict[i] = []
    i += 1

indx= 0 
for i in range(len(list1)):
    for k in range(1, fact+1):
        fact_dict[k].append(list1[indx])
        indx += 1
        if indx == len(list1):
            indx = 0
    indx += 1   
       
print(list(fact_dict.values()))


# In[ ]:


import random
a = [1, 2, 3, 4]
uzunluk = len(a)
fact = 1
liste = []
son = []
for i in range(1, uzunluk + 1):
    fact *= i
while True:
    x = random.choice(a)
    if x not in liste:
        liste.append(x)
    if len(liste) == uzunluk:
        if liste not in son:
            son.append(liste)
            liste = []
            if len(son) == fact:
                break
        else:
            liste = []
son.sort()
for i in son:
    print(i)


# In[ ]:


def permütasyon(num, i=0):
   if i == len(num):
      print (num)
   else:
      for x in range(i, len(num)):
            num[i], num[x] = num[x] ,num[i]
            permütasyon(num, i+1)
            num[i], num[x] = num[x], num[i]
permütasyon([1,2,3])

