import streamlit as st
import pandas as pd
import datetime
import re
import csv
import random
import emoji
import numpy as np
import time
import base64


# Specify the image file and its extension
main_bg = "pexels-egos68-1906658.jpg"
main_bg_ext = "jpg"

# Encode the image to base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Get the base64 of the image
base64_image = get_base64_of_bin_file(main_bg)

# Set the background image using the encoded base64 string
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/{main_bg_ext};base64,{base64_image}");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True
)


st.title("My Expenses")
st.sidebar.title( "About the project")
st.sidebar.text("This project is about me making a\n log of all the expenses I make\n during a month.")

st.sidebar.link_button("click here for the code", 'https://fantastic-space-happiness-97q955pgvqxxfx945.github.dev/')




def main():
    status = st.radio(
        "Select Reason: ", ("Canteen", "Mess", "Home", "Travel", "Utility")
    )


    mylist = [
        emoji.emojize(":red_heart:"),
        emoji.emojize(":thumbs_up:"),
        emoji.emojize(":raised_hand:"),
        emoji.emojize(":angry_face:"),
    ]
    k = random.choice(mylist)
    name = st.date_input("Enter the date")
    amount = st.text_input("Enter the Amount", "")
    if amount.isdigit():
        if st.button("Submit"):
            result = f"{name},{amount}"

            st.success(result, icon=k)
            with open(f"{status}_expenses.csv", "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["date", "amount"])
                writer.writerow({"date": name, "amount": amount})
            name = f"{status} {name}"
            with open("expenses.csv", "a", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["canteen", "amount"])
                writer.writerow({"canteen": name, "amount": amount})
            
            
        


if __name__ == "__main__":
    main()
