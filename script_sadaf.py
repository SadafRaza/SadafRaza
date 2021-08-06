#!/usr/bin/env python3
# coding: utf-8

# In[1]:


print("NAME: Sadaf Raza \nE-MAIL: sadafraza48@gmail.com \nSLACK USERNAME: @sadaf \nBIOSTACK: Genomics \nTwitter Handle: @svdvf")
def hamming_distance(a,b):
    count=0
    for i in range(len(a)):
        if a[i] != b[i]:
            count +=1
    return count

print(hamming_distance('@sadaf','@svdvf'))


# In[ ]:




