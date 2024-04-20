import requests
import json
from dotenv import load_dotenv
from la_hacks.sentiment import analyzeSentiment
import os

# Load environment variables
load_dotenv()

def fetch_esg_data(company_name, tries=0):
    if tries > 3:
        return "I GIVE UP ):"
    url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent'
    headers = {
        'Content-Type': 'application/json',
    }
    params = {
        'key': os.getenv("GEMINI_API_KEY")
    }
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"Please give me ESG data for {company_name}. I need this to be returned in json format, with two fields: esgGood, esgBad. Please emphasize environmental and ethical factors! For the esgGood field, it will be a list of concise bullet points about good things that the company is doing, with the most important ones first. For the bad fields, it will be the same, but with bad things."
                    }
                ]
            }
        ]
    }

    # Send the POST request
    response = requests.post(url, headers=headers, json=data, params=params)
    
    # Check if the response was successful
    if response.status_code == 200:
        response_data = json.loads(response.json()["candidates"][0]["content"]["parts"][0]["text"][7:-3])

        print(response_data)
        # Ensure the response matches the expected format
        if "esgGood" in response_data and "esgBad" in response_data:
            return response_data
        else:
            # return response_data
            return fetch_esg_data(company_name, tries+1)
    else:
        return f"Failed to fetch data: {response.status_code} - {response.text}"

# Usage
if __name__ == "__main__":
    company = "Nestle"
    esg_data = fetch_esg_data(company)
    print(json.dumps(esg_data, indent=2))
    print(analyzeSentiment(esg_data['esgGood'], esg_data['esgBad']))
    # print(os.getenv("GEMINI_API_KEY"))
