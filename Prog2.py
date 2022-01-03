# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 19:27:38 2021

@author: Prince
"""
# CIS 443-01 - Analytics Programming
## Program 2
# Spring 2021
# __Grading ID__: P8330 <br>
#__Due__: Thursday, October 21 11:59 PM) <br />
#__Worth__: 50 pts.<br />

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def input_test_scores ():
    #input the number of students
    stu = int(input('How many students: '))
    #number of test
    test = int(input('How many test for each student: '))
    #list to store the scores
    score = []
    #loop 
    for i in range(stu):
        #list for students
        Name_lst = []
        #input name
        Stu_name = input("Enter the student's name: ")
        Name_lst.append(Stu_name)
        
        #input score
        for k in range(test):
            print("Enter score for the test",k+1,": ")
            #take input to Name_lst
            Name_lst.append(int(input()))
            #append lst to score to make 2d list
            score.append(Name_lst)
    return score

#function to mean and display grade
def summarize_test_scores(score):
    #number of test
    sum_score = len(score[0])-1
    mean = []
    #calculate mean for each student and append to mean list
    for data in score:
        m = sum(data[1:])/sum_score
        mean.append(m)
    
    #list to store students grade
    grade = []
    for z in mean:
        if z>=90:
            grade.append('A')
        elif z>=80 and z<90:
            grade.append('B')
        elif z>=70 and z<80:
            grade.append('C')
        elif z>=60 and z<70:
            grade.append('D')
        elif z<60:
            grade.append('F')
                 
#shows the list of scores
    print('\n    Test Score Summary')
    print(f'Student {"Average":>8}   Grade')
    print('--------------------')
    for i in range(len(score)):
        print(score[i][0],"  ",str(round(mean[i], 2)),"   ",grade[i])

    #creating the bar plot
    Name = []
    Name = score
    Name.append(score)
    Average = []
    Average = mean
    Average.append(mean)
 
    sns.set_style('whitegrid')
    
    # Display frequency & bar 
    plt.bar(Name, Average)
    plt.title('Student*s Average Test Score', fontsize=14 )
    plt.xlabel('Name', fontsize=14)
    plt.ylabel('Average Test Score', fontsize=14)
    plt.show()    
    
# Application logic
score = input_test_scores()
summarize_test_scores(score)



