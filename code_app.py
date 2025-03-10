import streamlit as st

st.write("import streamlit as st
import pandas as pd
import datetime
import re
import csv
import random
import numpy as np
import time



st.title("My Expenses")
st.sidebar.title( "About the project")
st.sidebar.text("This project is about me making a\n log of all the expenses I make\n during a month.")

st.sidebar.link_button("click here for the code", 'https://fantastic-space-happiness-97q955pgvqxxfx945.github.dev/')




def main():
    status = st.radio(
        "Select Reason: ", ("Canteen", "Mess", "Home", "Travel", "Utility")
    )


    name = st.date_input("Enter the date")
    amount = st.text_input("Enter the Amount", "")
    if amount.isdigit():
        if st.button("Submit"):
            result = f"{name},{amount}"

            st.success(result)
            with open(f"{status}_expenses.csv", "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["date", "amount"])
                writer.writerow({"date": name, "amount": amount})
            name = f"{status} {name}"
            with open("expenses.csv", "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["canteen", "amount"])
                writer.writerow({"canteen": name, "amount": amount})
            
            
        


if __name__ == "__main__":
    main()")
