#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def b(a):
    toplam=0
    x=int(len(str(a)))
    c=x
    y=a
    while c>0:
        bsm=y//10**(c-1) #basamak degeri
        y=y%10**(c-1) 
        toplam+=bsm**x
        c-=1
        
    if a==toplam:
        print("{} sayidi bu kurala uygundur".format(a))
    #else:
     #   print("{} sayidi bu kurala uygun degildir".format(a))

z=0
sayi=int(input("Hangi Sayiya kadar bulmak istersin?:"))
while z<sayi:
         b(z)
         z+=1
        
    
    
    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




