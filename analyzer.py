import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


nltk.download("vader_lexicon")


def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()

    sentiment_scores = sia.polarity_scores(text)
    compound_score = sentiment_scores["compound"]

    if compound_score >= 0.05:
        return "Someone's in a good mood!"
    elif compound_score <= -0.05:
        return "Not exactly throwing a party, huh?"
    else:
        return "Just vibing in the middle."
