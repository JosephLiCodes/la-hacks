import requests
import json
from dotenv import load_dotenv
import os
import math

# Load environment variables
load_dotenv()

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sigmoid_ethics_score(sentiment_score):
        k = 4  # Steepness of the sigmoid curve
        return int(100 / (1 + math.exp(-k * sentiment_score)))

def analyze_sentiment(esgGood, esgBad):        
    analyzer = SentimentIntensityAnalyzer()
    text_good = " ".join(esgGood)
    text_bad = " ".join(esgBad)
    scores_good = analyzer.polarity_scores(text_good)
    scores_bad = analyzer.polarity_scores(text_bad)

    return scores_good['pos'] - scores_bad['neg']*1.5


def fetch_esg_data(company_name, tries=0):
    # return [
    #     ["hi"],
    #     ["bye", "byebye bye byeasdfasDG FASDGAS DGIHJA' DSPDO UJIP OI","bye","bye","bye","bye","bye",],
    #     50
    # ]
    print(tries, company_name)
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
    print('about to send this piece of request') # Send the POST request
    response = requests.post(url, headers=headers, json=data, params=params)
    print("LFG! REQEUST SENT!")
    # Check if the response was successful
    if response.status_code == 200:
        try:
            print(response.json())
            response_data = json.loads(response.json()["candidates"][0]["content"]["parts"][0]["text"][7:-3])
            # Ensure the response matches the expected format
            if "esgGood" in response_data and "esgBad" in response_data:
                return [
                    response_data["esgGood"],
                    response_data["esgBad"],
                    sigmoid_ethics_score(analyze_sentiment(response_data["esgGood"], response_data["esgBad"]))
                ]
            else:
                # return response_data
                return fetch_esg_data(company_name, tries+1)
        except:
            return fetch_esg_data(company_name, tries+1)
    else:
        return f"Failed to fetch data: {response.status_code} - {response.text}"

# Usage
if __name__ == "__main__":
    company = "Kirkland Signature"
    esg_data = fetch_esg_data(company)
    print(company, esg_data)