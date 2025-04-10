# Amazon Review Scraping and Sentiment Analysis 🛍️🧠

This project performs web scraping of Amazon product reviews and sentiment analysis using Python-based tools including Scrapy, MongoDB, and VADER Sentiment Analyzer. It collects reviews from Amazon Canada for multiple products, stores them in a MongoDB database, and analyzes the sentiment using NLP techniques.

---
## 📁 Project Structure
```
AmazonReview_Scraping_and_SentimentAnalysis/
│
├── NLP preprocessing.ipynb                # Preprocessing of text data (not loaded)
├── NLP sentiment analysis.ipynb           # Sentiment analysis, MongoDB aggregation, visualizations
│
└── amazon_reviews_scraping/
    ├── scrapy.cfg                         # Scrapy project configuration
    ├── amazon_reviews_scraping/
    │   ├── items.py                       # (Empty) item schema placeholder
    │   ├── pipelines.py                   # Pipeline to insert scraped reviews into MongoDB
    │   ├── settings.py                    # Scrapy configuration including MongoDB setup
    │   └── spiders/
    │       └── amazon_review.py           # Spider to scrape Amazon product reviews
    └── review test.json                   # Example/test output file
```

--- 

## 🚀 Features

    Web Scraping with Scrapy:
    Extracts reviews (title, rating, text, date, user) from Amazon Canada product pages.

    MongoDB Integration:
    Scraped data is stored in a MongoDB collection (amazon_reviews_db.reviews).

    VADER Sentiment Analysis:
    Uses compound sentiment scoring to classify reviews as Positive or Negative.

    Visualizations:

        Sentiment distribution chart

        Product-wise review sentiment breakdown

        Word clouds and top words per sentiment

--- 
## 🛠️ How to Run
1. Clone the repo
```
git clone https://github.com/prayag-purohit/AmazonReview_Scraping_and_SentimentAnalysis.git
cd AmazonReview_Scraping_and_SentimentAnalysis
```

2. Set up environment
```
pip install scrapy pymongo vaderSentiment nltk matplotlib seaborn wordcloud
```

Make sure MongoDB is installed and running on localhost:27017.
3. Start Scrapy Spider
```
cd amazon_reviews_scraping
scrapy crawl amazon_reviews
```
4. Run Sentiment Analysis

Open and run the cells inside NLP sentiment analysis.ipynb after data has been collected.

> ⚠️ **Warning:** This project has `ROBOTSTXT_OBEY = False`, meaning it does not respect `robots.txt`. Do **not** scrape Amazon at scale or without permission — it may violate their terms of service.


--- 
## 📊 Sample Output

    Bar charts showing review sentiment (positive vs. negative)

    Product-wise sentiment breakdown using ASIN

    Word clouds of most common words in positive and negative reviews

    Top 15 most frequent positive and negative keywords

---
🧠 Technologies

    Python

    Scrapy

    MongoDB

    NLTK

    VADER

    Jupyter Notebooks

    Matplotlib & Seaborn

---

📎 Notes
    > ⚠️ **Warning:** This project has `ROBOTSTXT_OBEY = False`, meaning it does not respect `robots.txt`. Do **not** scrape Amazon at scale or without permission — it may violate their terms of service.


    Ensure compliance with Amazon's terms of service when scraping.

    User-agent and delay settings are configured to reduce chances of blocking.

👨‍💻 Author

Made with ❤️ by Prayag Purohit