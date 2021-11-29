#!/usr/bin/env python
# coding: utf-8

# In[1]:


def asaluntil(a):
    print("We look at the function which reveal prime numbers from 1 to the entered number")
    for i in range(1,a):
        if i==1:
            continue
        elif i==2:
            print("{} is prime number".format(i))
        elif i>2:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print("{} is prime ".format(i))
x=int(input("at until which number do u want to look?:"))
asaluntil(x)
            


# In[ ]:





# In[ ]:





# In[ ]:




