#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
def countdown(t):
    while(t):
        mins,secs=divmod(t,60)
        timer='{}:{:01d}'.format(mins,secs)
        print(timer)
        time.sleep(1)
        t-=1
    print('fire in the hole')
t=int(input('enter'))
countdown(t)


# In[ ]:




