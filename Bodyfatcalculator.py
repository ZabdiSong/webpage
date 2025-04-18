import streamlit as st

# Initialize Streamlit app
st.title("Body Health Calculator")

# progress
if "progress_value" not in st.session_state:
    st.session_state.progress_value = 0

st.markdown("Your progress")
progress_display = st.progress(st.session_state.progress_value)

if st.button("keep going"):
    if st.session_state.progress_value < 100:
        st.session_state.progress_value += 1
        progress_display.progress(st.session_state.progress_value)

milestones = {
    10: "A",
    30: "B"
}
if st.session_state.progress_value in milestones:
    st.success(milestones[st.session_state.progress_value])
    user_input = st.text_input(" Record your thoughts or relections:")
    if user_input:
        st.write("You wrote", user_input)

if st.session_state.progress_value == 100:
    st.balloons()
    st.success("Congratulations!")

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

# Interpret body fat percentage
if sex == "Male":
    if body_fat_percentage <= 15:
        st.warning("Your body fat percentage is very low. Consult a healthcare provider.")
    elif 15 < body_fat_percentage < 25:
        st.success("Your body fat percentage is optimal!")
    else:
        st.warning("Your body fat percentage is higher than normal. Consider regular exercise.")
else:
    if body_fat_percentage <= 23:
        st.warning("Your body fat percentage is very low. Consult a healthcare provider.")
    elif 23 < body_fat_percentage < 33:
        st.success("Your body fat percentage is optimal!")
    else:
        st.warning("Your body fat percentage is higher than normal. Consider regular exercise.")

# Add disclaimer
st.markdown("***")
st.info("Note: These calculations are estimates. For accurate health assessments, consult a qualified healthcare professional.")
