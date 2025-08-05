import streamlit as st

st.title("💪 FitBuddy AI")
st.write("Get a workout and diet plan based on your fitness goal.")

name = st.text_input("Enter your name")
goal = st.selectbox("Select your goal", ["Weight Loss", "Muscle Gain", "General Fitness"])

def recommend_workout(goal):
    if goal == "Weight Loss":
        return ["Treadmill - 30 mins", "HIIT - 20 mins", "Light weights - 15 mins"]
    elif goal == "Muscle Gain":
        return ["Heavy weight training - 45 mins", "Protein-rich meals"]
    else:
        return ["Brisk walk - 20 mins", "Full-body workout - 30 mins"]

def recommend_diet(goal):
    if goal == "Weight Loss":
        return ["Oats & fruits", "Grilled chicken salad", "Green tea"]
    elif goal == "Muscle Gain":
        return ["Eggs & toast", "Chicken & rice", "Protein shake"]
    else:
        return ["Balanced meals", "Lots of water"]

if st.button("Get My Plan"):
    if name:
        st.subheader(f"Hello {name}, here’s your plan:")
        st.write("### 🏋 Workout Plan")
        for w in recommend_workout(goal):
            st.write(f"- {w}")
        st.write("### 🥗 Diet Plan")
        for d in recommend_diet(goal):
            st.write(f"- {d}")
    else:
        st.warning("Please enter your name first!")
