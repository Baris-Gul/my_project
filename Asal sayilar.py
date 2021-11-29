#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def asal(a):
    if a==0 or a==1:
        print("{} asal sayi degildir".format(a))
    elif a==2:
        print("{} asal sayidir".format(a))
    elif a>2:
        for i in range(2,a):
            if a%2==0:
                print("{} asal sayi degildir".format(a))
                break
        else:
            print("{} asaldir".format(a))
while True:
    answer=input("Do u want to control whether the number is prime?:")
    if answer=="yes":
        number=int(input("please Number:"))
        asal(number)
    elif answer=="no":
        break
    else:
        print("I dont understand the anwser!")
        


# In[ ]:




