import streamlit as st

# Title and description of the app
st.title("Health and Wellness Questionnaire")
st.write("This app collects data on your physical activity, sleep, and basic health information. Your responses will help us understand common wellness patterns and provide insights on how you might improve your health.")

# Initialize variables for storing responses
responses = {}

# Multiple Choice Questions
st.header("Multiple Choice Questions")

responses["physical_activity"] = st.radio(
    "1) How much physical activity do you get on a weekly basis?",
    ("None", "1-2 hours", "3-4 hours", "5+ hours")
)

responses["activity_intensity"] = st.radio(
    "2) What is the intensity of your physical activity?",
    ("Low", "Moderate", "High")
)

responses["processed_food_intake"] = st.radio(
    "3) What percent of your daily food intake is processed?",
    ("0-25%", "26-50%", "51-75%", "76-100%")
)

responses["sleep_duration"] = st.radio(
    "4) How much sleep do you get per night on average?",
    ("Less than 5 hours", "5-6 hours", "7-8 hours", "More than 8 hours")
)

responses["sleep_quality"] = st.radio(
    "5) How is the average quality of your sleep?",
    ("Poor", "Fair", "Good", "Excellent")
)

# Open Response Questions
st.header("Open Response Questions")

responses["name"] = st.text_input("6) What is your name?")
responses["sex"] = st.text_input("7) What is your sex?")
responses["weight"] = st.text_input("8) What is your weight?")
responses["height"] = st.text_input("9) What is your height?")
responses["email"] = st.text_input("10) What is your email?")

# Submission and response
if st.button("Submit"):
    st.write("Thank you for completing the questionnaire!")
    st.write("Here are your responses:")
    for question, answer in responses.items():
        st.write(f"{question.capitalize().replace('_', ' ')}: {answer}")
