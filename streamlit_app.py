import streamlit as st
import csv
import datetime

# Title
st.title("My  :red[Expenses] :sunglasses:")

# Sidebar
st.sidebar.title("About the project")
st.sidebar.text("This project is about me making a\nlog of all the expenses I make\nduring a month.")
st.sidebar.markdown("[Click here for the code](https://fantastic-space-happiness-97q955pgvqxxfx945.github.dev/)")

def main():
    # Expense category selection
    status = st.radio("Select Reason: ", ("Canteen", "Mess", "Home", "Travel", "Utility"))

    # Date input
    name = st.date_input("Enter the date")
    
    # Amount input
    amount = st.text_input("Enter the Amount", "")
    
    if amount.strip().isdigit():  # Ensure the input is a valid number
        if st.button("Submit"):
            date_str = str(name)  # Convert date to string
            result = f"Date: {date_str}, Amount: {amount}, Category: {status}"
            st.success(result)

            # Append to expenses.csv (single file for all categories)
            with open("expenses.csv", "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["date", "amount", "category"])
                if file.tell() == 0:  # Write header only if file is empty
                    writer.writeheader()
                writer.writerow({"date": date_str, "amount": amount, "category": status})
    
    else:
        st.warning("Please enter a valid amount.")

if __name__ == "__main__":
    main()

            
        



