#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import deque
text_shower=deque(maxlen=2)
mode="normal"


# In[ ]:

## for pyinstaller
import gymnasium.envs.box2d



# In[2]:


import gymnasium as gym


# In[3]:


env = gym.make(
    "LunarLander-v2",
    continuous= True,
    gravity= -9.0,
    enable_wind = False,
    # wind_power = 15.0,
    # turbulence_power = 1.5,
    render_mode="human",
)


# In[4]:


main_env=env.env.env.env


# In[5]:


main_env.reset()


# In[6]:


from pygame.locals import *
import pygame
import numpy


# In[7]:


pygame.display.set_caption("lunar")


# In[8]:


screen = pygame.display.get_surface()


# In[9]:


font = pygame.font.SysFont(None, 48)


# In[ ]:





# In[ ]:





# In[10]:


def readable_score(r):
    r+=10
    r*=4
    r=int(r)
    return min(max(r,0),100)


# In[ ]:





# In[11]:


throttle=0
rotate=0
th_step=0.05

main_env.reset()

running=True
while running:
    o,r,terminated,*_=main_env.step((throttle,rotate))
    
    events=pygame.event.get()
    
    for event in events:
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button==1:
                mode="normal"
            if event.button==3:
                mode="hard"
            main_env.reset()
            throttle=0
            rotate=0
        if event.type==pygame.QUIT:
            running=False
    
    
    rotate=0
    pressed=pygame.key.get_pressed()
    
    
    if pressed[K_ESCAPE]:running=False
    
    if mode == "normal":
        throttle+=th_step*(int(pressed[K_UP])-int(pressed[K_DOWN]))
        throttle=min(max(0,throttle),1)
    elif mode == "hard":
        delta=th_step*(int(pressed[K_UP])-int(pressed[K_DOWN]))
        if throttle==0 and delta>0:delta=0.2
        throttle+=delta
        if throttle<0.2:throttle=0
        throttle=min(max(0,throttle),1)
        
    rotate=int(pressed[K_LEFT])-int(pressed[K_RIGHT])
    rotate=-rotate

    if not terminated:text_shower.append(r)
    
    score=readable_score(text_shower[0])
    screen.blit(font.render(str(score), True, (0, 0, 255)),[10,50])
    screen.blit(font.render(str(mode), True, (0, 0, 255)),[10,10])
    pygame.display.update()
    import time
    time.sleep(0.02)


# In[12]:


pygame.display.quit()


# In[ ]:




