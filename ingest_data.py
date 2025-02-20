# ingest_data.py
import requests
import pandas as pd

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching", api_url, "Status code:", response.status_code)
        return None

# Base URL for simulated API (adjust the port as needed)
base_url = "http://127.0.0.1:5002/api"

clubs = fetch_data(f"{base_url}/clubs")
members = fetch_data(f"{base_url}/members")
transactions = fetch_data(f"{base_url}/transactions")
referrals = fetch_data(f"{base_url}/referrals")

clubs_df = pd.DataFrame(clubs) if clubs else pd.DataFrame()
members_df = pd.DataFrame(members) if members else pd.DataFrame()
transactions_df = pd.DataFrame(transactions) if transactions else pd.DataFrame()
referrals_df = pd.DataFrame(referrals) if referrals else pd.DataFrame()

print("Clubs Data:")
print(clubs_df)
print("\nMembers Data:")
print(members_df)
print("\nTransactions Data:")
print(transactions_df)
print("\nReferrals Data:")
print(referrals_df)
