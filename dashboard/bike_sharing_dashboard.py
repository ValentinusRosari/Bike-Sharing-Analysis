import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

hourly_data = pd.read_csv("hour.csv")

st.title("Bike Sharing Data Analysis Dashboard")

st.sidebar.title("Options")
analysis_type = st.sidebar.selectbox(
    "Select Analysis Type:", ["Rentals by Hour", "Rentals vs. Weather"]
)


# Function to plot Rentals by Hour
def plot_rentals_by_hour(data):
    hourly_rentals = data.groupby("hr")["cnt"].sum().reset_index()
    hourly_rentals = hourly_rentals.sort_values(by="hr")

    plt.figure(figsize=(10, 6))
    plt.plot(hourly_rentals["hr"], hourly_rentals["cnt"], marker="o", color="orange")
    plt.title("Total Bike Rentals by Hour of the Day", fontsize=14)
    plt.xlabel("Hour of the Day", fontsize=12)
    plt.ylabel("Total Rentals", fontsize=12)
    plt.grid(True)
    st.pyplot(plt)

    st.write(
        """
    **Explanation:**
    This graph shows the total bike rentals for each hour of the day. 
    There are two clear peaks: one in the morning around 8 AM, and another in the evening around 5 PM. 
    These peaks likely correspond to commuter rush hours, indicating that a significant portion of bike usage is for commuting.
    """
    )


# Function to plot Rentals vs. Weather Situation
def plot_rentals_vs_weather(data):
    plt.figure(figsize=(8, 6))
    sns.boxplot(x="weathersit", y="cnt", data=data)
    plt.title("Bike Rentals vs. Weather Situation", fontsize=14)
    plt.xlabel("Weather Situation", fontsize=12)
    plt.ylabel("Total Rentals", fontsize=12)
    plt.xticks(
        ticks=[0, 1, 2, 3],
        labels=["Clear", "Mist", "Light Rain/Snow", "Heavy Rain/Snow"],
    )
    st.pyplot(plt)

    st.write(
        """
    **Explanation:**
    This boxplot illustrates how different weather situations affect bike rentals. 
    In clear weather conditions, bike rentals are the highest, as expected. 
    As weather conditions worsen (moving from clear to heavy rain/snow), the number of bike rentals decreases significantly. 
    This shows the direct influence of weather on bike-sharing demand.
    """
    )


# Display the corresponding analysis
if analysis_type == "Rentals by Hour":
    plot_rentals_by_hour(hourly_data)
elif analysis_type == "Rentals vs. Weather":
    plot_rentals_vs_weather(hourly_data)
