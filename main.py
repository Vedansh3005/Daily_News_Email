import requests
from send_email import send_email

topic = "tesla"
api_key = "08ae34ad0758475996a61469ee2d0a0b"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-03-03&" \
      "sortBy=publishedAt&" \
      "apiKey=08ae34ad0758475996a61469ee2d0a0b&" \
      "language=en"

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and description
email_content = """"""
for article in content['articles'][:20]:
      if article['title'] and article['description'] is not None:
            email_content = email_content + article['title'] + '\n' + article['description'] + '\n' + article['url'] + 2*'\n'

email_message = f"""\
Subject: Today's NEWS

{email_content}
"""
email_message = email_message.encode('utf-8')
send_email(email_message)
