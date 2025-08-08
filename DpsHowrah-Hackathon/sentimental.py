from textblob import TextBlob
from enum import Enum

class Feeling(Enum):
    SAD = -1
    NEUTRAL = 0
    HAPPY = 1

def analyze_sentiment(text: str) -> Feeling:
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    
    # Increase the thresholds to make them more selective
    if polarity > 0.3:
        return Feeling.HAPPY
    elif polarity < -0.3:
        return Feeling.SAD
    else:
        return Feeling.NEUTRAL
    
text=input("Enter a text: ")
print("Sentiment: ",analyze_sentiment(text).name)