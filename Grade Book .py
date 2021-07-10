#!/usr/bin/env python
# coding: utf-8

# ## Grade Book 

# In[3]:


last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below:
subjects = ["physics","calculus","poetry","history"] 
grades = [98,97,85,88]

gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
print("Gradebook")
print(gradebook)

gradebook.append(["computer science",100])
gradebook.append(["visual arts", 93])

gradebook[-1][-1] = 98
gradebook[2].remove(85)
gradebook[2].append("Pass")

full_gradebook = last_semester_gradebook + gradebook
print("")
print("last Semester's Gradebook plus Gradebook")
print(full_gradebook)


