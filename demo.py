#!/usr/bin/env python
# coding: utf-8

# In[1]:


#simple demo for test

def que3():
    # input date and judge the day of the year
    # decide whether it's leap year
    def judge_leap(num):
        date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # (a leap year every four year and not a hundred year) or every four hundred year
        if (num % 4 == 0 and num % 100 != 0) or num % 400 ==0:
            date[1] =29
        return date
 
    # format transform
    date = (input('Please input a date like this：“2018.02.12”：'))
    date_list = (list(map(int, (date.split('.')))))
    # calculate the number of days
    day = date_list[2]
    for i in range(date_list[1]):
        day += judge_leap(date_list[0])[i]
    print('{}.{} is the {}th day of {} year\n'.format(date_list[1], date_list[2], day, date_list[0]))


# In[3]:


que3()

