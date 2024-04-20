import nltk

nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

text_good = '"Walmart has set ambitious sustainability goals, aiming for zero emissions in its operations by 2040.","They are investing in renewable energy sources, such as wind and solar power, to reduce their reliance on fossil fuels.","The company is actively working to reduce waste and improve recycling in its stores and supply chain."'

text_bad = '"Walmart has faced criticism for its labor practices, including low wages, inadequate benefits, and allegations of worker exploitation.","The companys large size and global reach have raised concerns about its environmental impact, particularly in terms of carbon emissions and waste generation.", "Walmart has been accused of contributing to the decline of small businesses and local communities due to its competitive pricing and market dominance.", "There have been concerns about the sourcing of products, with allegations of using suppliers with poor labor and environmental practices."'

scores_good = analyzer.polarity_scores(text_good)
scores_bad = analyzer.polarity_scores(text_bad)

print('wtf', scores_good, scores_bad)

print('Walmart', scores_good['compound'] + scores_bad['compound'])

text_good = '"Nestlé has committed to achieving net-zero greenhouse gas emissions by 2050, setting interim targets for its operations and supply chain.", "They actively pursue sustainable sourcing of ingredients like cocoa and coffee, aiming to improve farmer livelihoods and protect ecosystems.","Nestlé works to reduce water usage and improve water efficiency and stewardship in its operations and supply chain.","The company has initiatives for reducing packaging waste and increasing recycled materials usage."'
text_bad = '"Nestlé has faced controversies regarding its baby formula marketing in developing countries, raising ethical
concerns about its impact on breastfeeding.","The company has been criticized for its water management practices, especially in regions with water scarcity.","Nestlés large-scale operations and global supply chain pose challenges in ensuring ethical sourcing and labor practices across all suppliers.","Concerns remain about deforestation and its impact on biodiversity within Nestlés supply chain, particularly for commodities like palm oil." '

scores_good = analyzer.polarity_scores(text_good)
scores_bad = analyzer.polarity_scores(text_bad)

print('wtf', scores_good, scores_bad)

print('Nestlé', scores_good['compound'] + scores_bad['compound'])