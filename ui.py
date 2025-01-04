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

st.header("Explore Dataset")

# Create a dropdown menu with column options
column_to_view = st.selectbox(
    "Select a column to filter by:",
    options=["All Data"] + list(df.columns),
)

# Slider to select dataset row number view
num_rows = st.slider(
    "Number of rows to display:",
    min_value=5, 
    max_value=len(df), 
    value=10,
    step=5
)

if column_to_view == "All Data":
    st.write("Showing the entire dataset:")
    st.dataframe(df.head(num_rows))
else:
    st.write(f"Showing data for column: {column_to_view}")
    st.dataframe(df[[column_to_view]].head(num_rows))


# Sentiment distribution bar chart
st.header("Sentiment Distribution")
sentiment_counts = df["Sentiment_Category"].value_counts()
st.bar_chart(sentiment_counts)

# Heatmap
import seaborn as sns
import matplotlib.pyplot as plt

st.header("Feature Correlation Heatmap")
correlation = df[["Score", "Comments", "Sentiment"]].corr()

fig, ax = plt.subplots()
sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)


# Word Cloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.header("Word Cloud")

# Word Cloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = " ".join(title for title in df["Title"])
wordcloud = WordCloud(width=1100, height=100, background_color="white").generate(text)

fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")

st.pyplot(fig)


