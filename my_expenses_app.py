import streamlit as st
import datetime
import pandas as pd
import plotly.express as px
from io import StringIO

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
    # Input form
    status = st.radio("Select Reason:", ("Canteen", "Mess", "Home", "Travel", "Utility"))
    date = st.date_input("Enter the date", datetime.date.today())
    amount = st.text_input("Enter the Amount (in ₹)", "")

    if amount.strip().isdigit():
        if st.button("Submit"):
            st.session_state["expenses"].append({
                "date": str(date),
                "amount": int(amount),
                "category": status
            })
            st.success("Added successfully!")
    elif amount:
        st.warning("Please enter a valid numeric amount.")

    # Show all saved expenses
    if st.session_state["expenses"]:
        st.subheader("📊 Expense History")
        df = pd.DataFrame(st.session_state["expenses"])
        df['date'] = pd.to_datetime(df['date'])

        # Show raw table
        st.dataframe(df)

        # Total amount by month
        st.subheader("📅 Monthly Totals")
        monthly = df.copy()
        monthly['month'] = monthly['date'].dt.to_period('M')
        month_totals = monthly.groupby('month')['amount'].sum().reset_index()
        month_totals['month'] = month_totals['month'].astype(str)
        st.table(month_totals)

        # Pie chart: Category breakdown
        st.subheader("🍕 Category Breakdown")
        pie_chart = px.pie(df, names='category', values='amount', title='Expenses by Category')
        st.plotly_chart(pie_chart)

        # Bar chart: Category totals
        st.subheader("📊 Bar Chart of Spending by Category")
        bar_chart = px.bar(df.groupby('category')['amount'].sum().reset_index(), x='category', y='amount')
        st.plotly_chart(bar_chart)

        # CSV Export
        st.subheader("⬇️ Export Your Expenses")
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name='my_expenses.csv',
            mime='text/csv',
        )

if __name__ == "__main__":
    main()
