import streamlit as st

# Initialize Streamlit app
st.title("Body Health Calculator")

# Data input
col1, col2 = st.columns(2)
with col1:
    height = st.number_input("Height (cm)", min_value=0, value=170)
    weight = st.number_input("Weight (kg)", min_value=0, value=70)
    age = st.number_input("Age", min_value=0, value=25)

with col2:
    sex = st.selectbox("Sex", ["Male", "Female"])

# Calculate BMI
def calculate_bmi(weight, height):
    return weight / ((height/100)**2)

bmi = calculate_bmi(weight, height)

# Display BMI result
st.write(f"\nYour BMI is {bmi:.2f}")

# BMI interpretation
if bmi <= 18:
    st.warning("You are underweight. Consider consulting a healthcare provider about a healthier diet.")
elif 18 < bmi < 24:
    st.success("You are at a healthy weight. Keep up the good work!")
else:
    st.warning("You are overweight. Regular exercise and balanced diet are recommended.")

# Body fat percentage calculation
def calculate_body_fat(bmi, age, is_male):
    base_formula = bmi * 1.2 + 0.23 * age - 5.4
    return base_formula - 10.8 if is_male else base_formula

body_fat_percentage = calculate_body_fat(bmi, age, sex == "Male")

# Display body fat percentage
st.write(f"\nYour estimated body fat percentage is {body_fat_percentage:.1f}%")

# Body fat evaluation based on the chart
def body_fat_evaluation(age, body_fat_percentage, sex):
    if sex == "Male":
        # Body Fat Chart for Men (simplified for all age ranges)
        if age <= 20:
            if body_fat_percentage < 15:
                return "Your body fat percentage is ideal."
            elif 15 <= body_fat_percentage < 20:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif 21 <= age <= 25:
            if body_fat_percentage < 17:
                return "Your body fat percentage is ideal."
            elif 17 <= body_fat_percentage < 22:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif 26 <= age <= 30:
            if body_fat_percentage < 19:
                return "Your body fat percentage is ideal."
            elif 19 <= body_fat_percentage < 23:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif 31 <= age <= 35:
            if body_fat_percentage < 20:
                return "Your body fat percentage is ideal."
            elif 20 <= body_fat_percentage < 24:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif 36 <= age <= 40:
            if body_fat_percentage < 21:
                return "Your body fat percentage is ideal."
            elif 21 <= body_fat_percentage < 25:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif 41 <= age <= 45:
            if body_fat_percentage < 22:
                return "Your body fat percentage is ideal."
            elif 22 <= body_fat_percentage < 26:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif 46 <= age <= 50:
            if body_fat_percentage < 23:
                return "Your body fat percentage is ideal."
            elif 23 <= body_fat_percentage < 27:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif 51 <= age <= 55:
            if body_fat_percentage < 24:
                return "Your body fat percentage is ideal."
            elif 24 <= body_fat_percentage < 28:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif age >= 56:
            if body_fat_percentage < 25:
                return "Your body fat percentage is ideal."
            elif 25 <= body_fat_percentage < 29:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."

    else:
        # Body Fat Chart for Women (simplified for all age ranges)
        if age <= 20:
            if body_fat_percentage < 23:
                return "Your body fat percentage is ideal."
            elif 23 <= body_fat_percentage < 28:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif 21 <= age <= 25:
            if body_fat_percentage < 25:
                return "Your body fat percentage is ideal."
            elif 25 <= body_fat_percentage < 30:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif 26 <= age <= 30:
            if body_fat_percentage < 26:
                return "Your body fat percentage is ideal."
            elif 26 <= body_fat_percentage < 31:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif 31 <= age <= 35:
            if body_fat_percentage < 27:
                return "Your body fat percentage is ideal."
            elif 27 <= body_fat_percentage < 32:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif 36 <= age <= 40:
            if body_fat_percentage < 28:
                return "Your body fat percentage is ideal."
            elif 28 <= body_fat_percentage < 33:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif 41 <= age <= 45:
            if body_fat_percentage < 29:
                return "Your body fat percentage is ideal."
            elif 29 <= body_fat_percentage < 34:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif 46 <= age <= 50:
            if body_fat_percentage < 30:
                return "Your body fat percentage is ideal."
            elif 30 <= body_fat_percentage < 35:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif 51 <= age <= 55:
            if body_fat_percentage < 31:
                return "Your body fat percentage is ideal."
            elif 31 <= body_fat_percentage < 36:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."
        elif age >= 56:
            if body_fat_percentage < 32:
                return "Your body fat percentage is ideal."
            elif 32 <= body_fat_percentage < 37:
                return "You have an average body fat percentage."
            else:
                return "You have a higher than average body fat percentage."

# Evaluate and display body fat status
evaluation_message = body_fat_evaluation(age, body_fat_percentage, sex)
st.write(f"\n{evaluation_message}")

# Add disclaimer
st.markdown("***")
st.info("Note: These calculations are estimates. For accurate health assessments, consult a qualified healthcare professional.")
