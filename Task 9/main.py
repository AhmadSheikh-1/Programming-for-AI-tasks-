from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
    sid_obj = SentimentIntensityAnalyzer()
    sentiment_dict = sid_obj.polarity_scores(sentence)

    if sentiment_dict['compound'] >= 0.05:
        return "Positive"
    elif sentiment_dict['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

print( )
print("Welcome to Sentiment Analyzer")
if __name__ == "__main__":
    sentence = input("Enter a sentence to analyze its sentiment: ")
    sentiment = sentiment_scores(sentence)
    print("Sentiment: ", sentiment)
