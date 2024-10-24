import streamlit as st
import numpy as np

# Function to calculate BMI
def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive numbers")
    return weight / (height ** 2)

# Function to calculate BMR
def calculate_bmr(weight, height, age, gender):
    if weight <= 0 or height <= 0 or age <= 0:
        raise ValueError("Weight, height, and age must be positive numbers")
    if gender not in ["Male", "Female"]:
        raise ValueError("Invalid gender")
    if gender == 'Male':
        return 10 * weight + 6.25 * height - 5 * age + 5
    else:
        return 10 * weight + 6.25 * height - 5 * age - 161

# Function to calculate 1RM
def calculate_1rm(weight, reps):
    if weight <= 0 or reps <= 0:
        raise ValueError("Weight and reps must be positive numbers")
    return weight * (1 + reps / 30)

# Function to calculate Body Fat Percentage
def calculate_body_fat(age, waist_circumference, neck_circumference, hip_circumference, height, gender):
    if age <= 0 or waist_circumference <= 0 or neck_circumference <= 0 or hip_circumference <= 0 or height <= 0:
        raise ValueError("All measurements must be positive numbers")
    if gender not in ["Male", "Female"]:
        raise ValueError("Invalid gender")
    if gender == 'Male':
        return 86.01 * np.log(waist_circumference - neck_circumference) - 70.041 * np.log(height) + 36.76
    else:
        return 163.205 * np.log(waist_circumference + hip_circumference - neck_circumference) - 97.684 * np.log(height) - 78.387

# Streamlit App
st.title("Health Calculator App")

# Images and Introduction
try:
    st.image("images.jpeg", width=250)
except FileNotFoundError:
    st.error("Image not found. Please ensure 'images.jpeg' is in the correct directory.")

st.header("Welcome to the Health Calculator App!")
st.write("""
This app helps you calculate various health metrics, including BMI, BMR, 1RM, and Body Fat Percentage. 
These calculations can help you understand your health status better and guide you toward your fitness goals.
""")

# Calculator mode selection
mode = st.selectbox("Select Calculator", ["BMI", "BMR", "1RM", "Body Fat Percentage"])

# Initialize suggestion
suggestion = ""

if mode == "BMI":
    st.header("BMI Calculator")
    weight = st.number_input("Weight (kg)", min_value=0.0)
    height = st.number_input("Height (m)", min_value=0.0)

    if st.button("Calculate BMI"):
        try:
            bmi = calculate_bmi(weight, height)
            st.write(f"Your BMI is: {bmi:.2f}")
            if bmi < 18.5:
                st.warning("You are Underweight, try to gain weight in a healthy way.")
                suggestion = "Consider increasing your caloric intake with nutrient-dense foods."
            elif 18.5 <= bmi < 24.9:
                st.success("Normal weight. You are in good condition, maintain it.")
                suggestion = "Great job! Maintain a balanced diet and regular exercise."
            elif 25 <= bmi < 29.9:
                st.warning("You are Overweight.")
                suggestion = "Consider adopting a healthier lifestyle with regular physical activity."
            else:
                st.error("Obesity.")
                suggestion = "Consult a healthcare provider for personalized advice."
        except ValueError as e:
            st.error(str(e))

elif mode == "BMR":
    st.header("BMR Calculator")
    weight = st.number_input("Weight (kg)", min_value=0.0)
    height = st.number_input("Height (cm)", min_value=0.0)
    age = st.number_input("Age (years)", min_value=0)
    gender = st.selectbox("Gender", ["Male", "Female"])

    if st.button("Calculate BMR"):
        try:
            bmr = calculate_bmr(weight, height / 100, age, gender)
            st.write(f"Your BMR is: {bmr:.2f} calories/day")
            st.success("This is the number of calories you need to maintain your current weight.")
        except ValueError as e:
            st.error(str(e))

elif mode == "1RM":
    st.header("1RM Calculator")
    weight = st.number_input("Weight Lifted (kg)", min_value=0.0)
    reps = st.number_input("Reps", min_value=1)

    if st.button("Calculate 1RM"):
        try:
            one_rm = calculate_1rm(weight, reps)
            st.write(f"Your estimated 1RM is: {one_rm:.2f} kg")
            st.success("This is an estimate of your one-rep max.")
        except ValueError as e:
            st.error(str(e))

elif mode == "Body Fat Percentage":
    st.header("Body Fat Percentage Calculator")
    age = st.number_input("Age (years)", min_value=0)
    waist_circumference = st.number_input("Waist Circumference (cm)", min_value=0.0)
    neck_circumference = st.number_input("Neck Circumference (cm)", min_value=0.0)
    hip_circumference = st.number_input("Hip Circumference (cm)", min_value=0.0)
    gender = st.selectbox("Gender", ["Male", "Female"])
    height = st.number_input("Height (cm)", min_value=0.0)

    if st.button("Calculate Body Fat Percentage"):
        try:
            body_fat = calculate_body_fat(age, waist_circumference, neck_circumference, hip_circumference, height / 100, gender)
            st.write(f"Your Body Fat Percentage is: {body_fat:.2f}%")
            if body_fat < 18:
                st.success("You are in a healthy range, maintain it.")
                suggestion = "Keep up the good work!"
            else:
                st.warning("Consult a health professional; you have more fat.")
                suggestion = "Consider discussing your body composition with a healthcare provider."
        except ValueError as e:
            st.error(str(e))

# Suggestions and Resources
st.markdown("## Suggestions:")
st.write(suggestion)
st.write("### Additional Resources:")
st.write("""
- [Nutritional Guidelines](https://www.health.gov)
- [Exercise Recommendations](https://www.cdc.gov/physical-activity)
- [Healthy Living Tips](https://www.who.int/health-topics/healthy-living)
""")
