

import streamlit as st
import datetime

# Title
st.title("My :red[Expenses] :sunglasses:")

# Sidebar
st.sidebar.title("About the project")
st.sidebar.text("This project is about me making a\nlog of all the expenses I make\nduring a month.")
st.sidebar.markdown("[Click here for the code](https://fantastic-space-happiness-97q955pgvqxxfx945.github.dev/)")

# Initialize session state for expenses
if "expenses" not in st.session_state:
    st.session_state["expenses"] = []

def main():
    # Expense category selection
    status = st.radio("Select Reason:", ("Canteen", "Mess", "Home", "Travel", "Utility"))

    # Date input
    date = st.date_input("Enter the date")

    # Amount input
    amount = st.text_input("Enter the Amount", "")

    # Check for valid input
    if amount.strip().isdigit():
        if st.button("Submit"):
            expense_entry = {"date": str(date), "amount": amount, "category": status}
            
            # Store in session state
            st.session_state["expenses"].append(expense_entry)
            st.success("Added successfully!")

    else:
        st.warning("Please enter a valid numeric amount.")

    # Show all saved expenses
    if st.session_state["expenses"]:
        st.subheader("Expense History")
        for expense in st.session_state["expenses"]:
            st.write(f"📅 {expense['date']} | 💰 ₹{expense['amount']} | 🏷️ {expense['category']}")

if __name__ == "__main__":
    main()

            
        



