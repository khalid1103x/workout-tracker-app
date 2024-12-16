import streamlit as st

# Title
st.title("Weekly Workout Plan")

# Introduction
st.markdown("""
### Track Your Weekly Workouts 💪  
Use this app to follow your workout plan, log progress, and stay motivated!
""")

# Weekly Schedule Section
st.header("Your Weekly Schedule")
st.markdown("""
- **Monday**: Full Body Strength Training  
- **Tuesday**: Hike (Zone 2 Cardio, 1–2 hours)  
- **Wednesday**: Running (Steady/Intervals, 20–45 min)  
- **Thursday**: Full Body Strength Training (Variation)  
- **Friday**: Elliptical (30–45 min Intervals/Steady)  
- **Saturday**: Rowing (20–30 min Moderate/Intervals)  
- **Sunday**: Rest / Active Recovery (Yoga, Walking)
""")

# Workout Log Section
st.header("Workout Log")

# Input Fields to Log Exercises
day = st.selectbox("Select Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
exercise = st.text_input("Exercise Name")
sets = st.number_input("Sets", min_value=0, max_value=10, step=1)
reps = st.number_input("Reps", min_value=0, max_value=100, step=1)
duration = st.text_input("Duration (e.g., 30 min)")
notes = st.text_area("Notes (Optional)")

# Log Confirmation
if st.button("Save Workout Log"):
    st.success(f"✅ Workout Log Saved for **{day}**: {exercise} - {sets} sets x {reps} reps - {duration}")

# Progress Section
st.header("Weekly Progress")
st.markdown("Track your progress over time to stay consistent and motivated!")
st.info("📊 Weekly Progress Charts Coming Soon!")
