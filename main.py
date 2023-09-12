import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from gensim.summarization import summarize, keywords
from newspaper import Article
import pyttsx3

class NewsAggregator:
    def __init__(self):
        self.NEWS_SOURCES = {
            'BBC': 'https://www.bbc.co.uk/news',
            'CNN': 'https://edition.cnn.com/',
            'The Guardian': 'https://www.theguardian.com/international',
            'The New York Times': 'https://www.nytimes.com/',
            'Al Jazeera': 'https://www.aljazeera.com/'
        }

    def scrape_news_articles(self, source):
        if source in self.NEWS_SOURCES:
            url = self.NEWS_SOURCES[source]
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            articles = soup.find_all('article')
            news_articles = []

            for article in articles:
                title = article.find('h3').text.strip()
                author = article.find('span', class_='byline').text.strip()
                publication_date = article.find('time').text.strip()
                content = article.find('div', class_='summary').text.strip()

                news_articles.append({
                    'title': title,
                    'author': author,
                    'publication_date': publication_date,
                    'content': content
                })

            return news_articles
        else:
            return []

    @staticmethod
    def analyze_sentiment(text):
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        if sentiment > 0:
            return 'positive'
        elif sentiment < 0:
            return 'negative'
        else:
            return 'neutral'

    @staticmethod
    def extract_keywords(text):
        return keywords(text)

    @staticmethod
    def summarize_article(text):
        return summarize(text)

    @staticmethod
    def display_news_feed(news_articles):
        for article in news_articles:
            print("\nTitle:", article['title'])
            print("Author:", article['author'])
            print("Publication Date:", article['publication_date'])
            print("Content:", article['content'])

    def search_news(self, keyword):
        # Search news implementation
        pass

    def save_article(self, article_id):
        # Save article implementation
        pass

    def customize_preferences(self, user_id, preferences):
        # Customization implementation
        pass

    @staticmethod
    def text_to_speech_conversion(text):
        engine = pyttsx3.init()
        engine.save_to_file(text, 'summary.mp3')
        engine.runAndWait()

    def user_interface(self):
        while True:
            print("\n1. View News Feed")
            print("2. Search News")
            print("3. Save Article")
            print("4. Customize Preferences")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                selected_source = input(
                    "Select news source (BBC, CNN, The Guardian, The New York Times, Al Jazeera): ")
                news_articles = self.scrape_news_articles(selected_source)
                self.display_news_feed(news_articles)

            elif choice == "2":
                keyword = input("Enter keyword to search: ")
                self.search_news(keyword)

            elif choice == "3":
                article_id = input("Enter article ID to save: ")
                self.save_article(article_id)

            elif choice == "4":
                user_id = input("Enter user ID: ")
                preferences = input("Enter preferences: ")
                self.customize_preferences(user_id, preferences)

            elif choice == "5":
                break


if __name__ == '__main__':
    aggregator = NewsAggregator()
    aggregator.user_interface()