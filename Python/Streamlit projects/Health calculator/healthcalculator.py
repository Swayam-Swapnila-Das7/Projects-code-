import streamlit as st
import numpy as np

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to calculate BMR
def calculate_bmr(weight, height, age, gender):
    if gender == 'Male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

# Function to calculate 1RM
def calculate_1rm(weight, reps):
    return weight * (1 + reps / 30)

# Function to calculate Body Fat Percentage
def calculate_body_fat(age, waist_circumference, neck_circumference, hip_circumference, height, gender):
    if gender == 'Male':
        return 86.01 * np.log(waist_circumference - neck_circumference) - 70.041 * np.log(height) + 36.76
    else:
        return 163.205 * np.log(waist_circumference + hip_circumference - neck_circumference) - 97.684 * np.log(height) - 78.387

# Streamlit App
st.title("Health Calculator App")

# Images and Introduction
st.image("images.jpeg", width=250)
st.header("Welcome to the Health Calculator App!")
st.write("""
This app helps you calculate various health metrics, including BMI, BMR, 1RM, and Body Fat Percentage. 
These calculations can help you understand your health status better and guide you toward your fitness goals.
""")

# Calculator mode selection
mode = st.selectbox("Select Calculator", ["BMI", "BMR", "1RM", "Body Fat Percentage"])

if mode == "BMI":
    st.header("BMI Calculator")
    weight = st.number_input("Weight (kg)", min_value=0.0)
    height = st.number_input("Height (m)", min_value=0.0)

    if st.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            st.markdown("<p style='color:red;'>Underweight</p>", unsafe_allow_html=True)
            suggestion = "Consider increasing your caloric intake with nutrient-dense foods."
        elif 18.5 <= bmi < 24.9:
            st.markdown("<p style='color:green;'>Normal weight</p>", unsafe_allow_html=True)
            suggestion = "Great job! Maintain a balanced diet and regular exercise."
        elif 25 <= bmi < 29.9:
            st.markdown("<p style='color:red;'>Overweight</p>", unsafe_allow_html=True)
            suggestion = "Consider adopting a healthier lifestyle with regular physical activity."
        else:
            st.markdown("<p style='color:red;'>Obesity</p>", unsafe_allow_html=True)
            suggestion = "Consult a healthcare provider for personalized advice."

elif mode == "BMR":
    st.header("BMR Calculator")
    weight = st.number_input("Weight (kg)", min_value=0.0)
    height = st.number_input("Height (cm)", min_value=0.0)
    age = st.number_input("Age (years)", min_value=0)
    gender = st.selectbox("Gender", ["Male", "Female"])

    if st.button("Calculate BMR"):
        bmr = calculate_bmr(weight, height / 100, age, gender)
        st.write(f"Your BMR is: {bmr:.2f} calories/day")
        st.success("This is the number of calories you need to maintain your current weight.")

elif mode == "1RM":
    st.header("1RM Calculator")
    weight = st.number_input("Weight Lifted (kg)", min_value=0.0)
    reps = st.number_input("Reps", min_value=1)

    if st.button("Calculate 1RM"):
        one_rm = calculate_1rm(weight, reps)
        st.write(f"Your estimated 1RM is: {one_rm:.2f} kg")
        st.success("This is an estimate of your one-rep max.")

elif mode == "Body Fat Percentage":
    st.header("Body Fat Percentage Calculator")
    age = st.number_input("Age (years)", min_value=0)
    waist_circumference = st.number_input("Waist Circumference (cm)", min_value=0.0)
    neck_circumference = st.number_input("Neck Circumference (cm)", min_value=0.0)
    hip_circumference = st.number_input("Hip Circumference (cm)", min_value=0.0)
    gender = st.selectbox("Gender", ["Male", "Female"])
    height = st.number_input("Height (cm)", min_value=0.0)

    if st.button("Calculate Body Fat Percentage"):
        body_fat = calculate_body_fat(age, waist_circumference, neck_circumference, hip_circumference, height, gender)
        st.write(f"Your Body Fat Percentage is: {body_fat:.2f}%")
        if body_fat < 18:
            st.markdown("<p style='color:green;'>Healthy range</p>", unsafe_allow_html=True)
            suggestion = "Keep up the good work!"
        else:
            st.markdown("<p style='color:red;'>Consult a health professional</p>", unsafe_allow_html=True)
            suggestion = "Consider discussing your body composition with a healthcare provider."

# Suggestions and Resources
st.markdown("## Suggestions:")
st.write(suggestion)
st.write("### Additional Resources:")
st.write("""
- [Nutritional Guidelines](https://www.health.gov)
- [Exercise Recommendations](https://www.cdc.gov/physicalactivity)
- [Healthy Living Tips](https://www.who.int/health-topics/healthy-living)
""")
