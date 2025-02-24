import streamlit as st.

# Data input
height = int(input("Enter your height in cm"))
weight = int(input("Enter your weight in kg"))
age = int(input("Enter your age"))
sex = st.selectbox("Select your sex", ("Male"), ("Female"))


# BMI calculation
BMI = weight * 2 / height ^ 2

print("Your BMI is", BMI)

if BMI <= 18 ：
    print ("You are too skinny, that's unhealthy, find a more healthy diet!")
    
if 18 < BMI < 23 :
    print ("You are healthy, keep it up!")
    
if BMI >= 23 :
    print ("You are obese, exercise more often and control your diet!")

# body fat percentage calculation
if sex == "Male" :
    body_fat_percentage = BMI * 1.2 + 0.23 * age - 5.4 - 10.8
    
    if body_fat_percentage <= 10 :
        print ("Your body fat percentage is low")
    
    if 10 < body_fat_percentage < 22 :
        print ("Your body condition is at the peak of health state, keep it up!")
        
    if body_fat_percentage >= 22 :    if body_fat_percentage <= 10 :
        print ("Your body fat percentage is low")
    
    if 10 < body_fat_percentage < 23 :
        print ("Your body condition is at the peak of health state, keep it up!")
        
    if body_fat_percentage >= 23 :
        print ("Your body fat percentage is high, you should exercise more and control your diet.")
       
    
if sex == "Female" :
    body_fat_percentage = BMI * 1.2 + 0.23 * age - 5.4
    
    if body_fat_percentage <= 15 :
        print ("Your body fat percentage is low")
        
    if 15 < body_fat_percentage < 27 :
        print ("Your body fat percentage is at the peak of health state, keep it up!")
        
    if body_fat_percentage >= 27 :
        print ("Your body fat percentage is high, you should exercise more and control your diet.")
        
print ("Your body fat percentage is", body_fat_percentage)   
