import streamlit as st

st.title("🍚 Food Allocation AI Chatbot")

# Initialize session state variables to store input and output
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def predict_food_demand(population, income, month, last_demand):
    # Dummy prediction logic (replace with your ML model)
    base = 1000
    if (month == "August"):
        season_factor =1.2
    else : season_factor=1.0
    prediction = round(last_demand* season_factor * (population / 1000))
    return round(prediction)

# Input fields with session_state to remember values
population = st.number_input("Enter estimated population:", min_value=1000, value=1000, key="pop")
income = st.number_input("Enter average income in the region (₹):", min_value=0, value=3000, key="income")
month = st.selectbox("Select month of prediction:", ["January", "February", "March", "April", "May", "June", "July", "August"], key="month")
last_demand = st.number_input("Enter food needed last month (kg):", min_value=0, value=900, key="last_demand")

if st.button("Get Prediction"):
    prediction = predict_food_demand(population, income, month, last_demand)
    response = f"✅ Estimated food needed in {month}: **{prediction} kg**"
    st.session_state.chat_history.append(("Bot", response))

# Show chat history
for speaker, message in st.session_state.chat_history:
    if speaker == "Bot":
        st.markdown(message)
