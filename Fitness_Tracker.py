import streamlit as st

class Workout:
    def __init__(self, date, exercise_type, duration, calories_burned):
        self.date = date
        self.exercise_type = exercise_type
        self.duration = duration
        self.calories_burned = calories_burned

    def __str__(self):
        return f"{self.date}: {self.exercise_type} for {self.duration} minutes, {self.calories_burned} calories burned"

class User:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.workouts = []

    def add_workout(self, workout):
        self.workouts.append(workout)

    def view_workouts(self):
        for workout in self.workouts:
            st.write(workout)

    def save_data(self, filename):
        with open(filename, 'w') as file:
            for workout in self.workouts:
                file.write(f"{workout.date},{workout.exercise_type},{workout.duration},{workout.calories_burned}\n")

    def load_data(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                date, exercise_type, duration, calories_burned = line.strip().split(',')
                workout = Workout(date, exercise_type, int(duration), int(calories_burned))
                self.workouts.append(workout)

def add_workout(user):
    st.subheader("Add a New Workout")
    date = st.text_input("Enter the date (YYYY-MM-DD):")
    exercise_type = st.text_input("Enter the exercise type:")
    duration = st.number_input("Enter the duration (minutes):", min_value=0)
    calories_burned = st.number_input("Enter the calories burned:", min_value=0)
    if st.button("Add Workout"):
        workout = Workout(date, exercise_type, duration, calories_burned)
        user.add_workout(workout)
        st.success("Workout added successfully!")

def view_workouts(user):
    st.subheader("View Workouts")
    st.write(f"{user.name}'s Workouts:")
    user.view_workouts()

def save_data(user):
    st.subheader("Save Data")
    filename = st.text_input("Enter the filename to save data:")
    if st.button("Save Data"):
        user.save_data(filename)
        st.success("Data saved successfully!")

def load_data(user):
    st.subheader("Load Data")
    filename = st.text_input("Enter the filename to load data:")
    if st.button("Load Data"):
        user.load_data(filename)
        st.success("Data loaded successfully!")

def main():
    st.title("🏋️‍♀️ Fitness Tracker App")
    st.sidebar.title("Navigation")
    
    name = st.text_input("Enter your name:")
    age = st.number_input("Enter your age:", min_value=0)
    weight = st.number_input("Enter your weight:", min_value=0.0)
    
    user = User(name, age, weight)

    menu = ["Add Workout", "View Workouts", "Save Data", "Load Data", "Exit"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Workout":
        add_workout(user)
    elif choice == "View Workouts":
        view_workouts(user)
    elif choice == "Save Data":
        save_data(user)
    elif choice == "Load Data":
        load_data(user)
    elif choice == "Exit":
        st.write("Exiting...")

if __name__ == "__main__":
    main()


