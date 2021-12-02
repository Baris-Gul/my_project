#!/usr/bin/env python
# coding: utf-8

# In[11]:


liste=[]
for i in range(1,101):
    if i%3==0 and i%5==0:
        liste.append("FizzBuzz")
        continue
    elif i%3==0:
        liste.append("Fizz")
    elif i%5==0:
        liste.append("Buzz")
    else:
        liste.append(i)
        

    

    
print(liste)


# In[ ]:




