import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def analyzeSentiment(esgGood, esgBad):        
    analyzer = SentimentIntensityAnalyzer()
    text_good = " ".join(esgGood)
    text_bad = " ".join(esgBad)
    scores_good = analyzer.polarity_scores(text_good)
    scores_bad = analyzer.polarity_scores(text_bad)

    print('wtf', scores_good['pos'], scores_bad['neg'])
    print('result', scores_good['pos'] - scores_bad['neg'])

    # print('Nestlé', scores_good['compound'] + scores_bad['compound'])