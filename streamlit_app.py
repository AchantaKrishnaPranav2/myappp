import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Google Sheets Authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("your-credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("MyExpenses").sheet1  # Replace with your sheet name

st.title("My :red[Expenses] :sunglasses:")

def main():
    status = st.radio("Select Reason:", ("Canteen", "Mess", "Home", "Travel", "Utility"))
    date = st.date_input("Enter the date")
    amount = st.text_input("Enter the Amount", "")

    if amount.strip().isdigit():
        if st.button("Submit"):
            row = [str(date), amount, status]
            sheet.append_row(row)  # Adds data to Google Sheets
            st.success(f"Added: {row}")

if __name__ == "__main__":
    main()

            
        



