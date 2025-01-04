import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("processed_reddit_ai_posts.csv")

# Page settings
st.set_page_config(layout="wide")

# Title
st.title("Reddit Sentiment Analysis Dashboard")

# Adding sentiment_category column to the df
def categorize_sentiment(score):
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    else:
        return "Neutral"

# Add Sentiment_Category column
df["Sentiment_Category"] = df["Sentiment"].apply(categorize_sentiment)


# Key Metrics
st.header("Key Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Posts", len(df))
with col2:
    st.metric("Average Score", round(df["Score"].mean(), 2))
with col3:
    st.metric("Average Sentiment", round(df["Sentiment"].mean(), 2))

# Dataset Overview
st.header("Dataset Overview")
st.write("A quick look at the dataset:")
st.dataframe(df.head())

# Sentiment distribution bar chart
st.header("Sentiment Distribution")
sentiment_counts = df["Sentiment_Category"].value_counts()
st.bar_chart(sentiment_counts)

# Word Cloud
from wordcloud import WordCloud

text = " ".join(title for title in df["Title"])
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

