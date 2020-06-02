# Imports
import requests
from bs4 import BeautifulSoup
from gensim.summarization import summarize
from nltk.chat.util import Chat, reflections

# Retrieve page text
url = 'https://t2conline.com/what-can-you-do-with-python/'
page = requests.get(url).text

# Turn page into BeautifulSoup object to access HTML tags
soup = BeautifulSoup(page, 'lxml')

# Get headline
headline = soup.find('h1').get_text()

# Get text from all <p> paragraph tags.
p_tags = soup.find_all('p')

# Get the text from each of the “p” tags and strip surrounding whitespace.
p_tags_text = [tag.get_text().strip() for tag in p_tags]

# Filter out sentences that contain newline characters '\n' or don't contain periods.
sentence_list = [sentence for sentence in p_tags_text if not '\n' in sentence]
sentence_list = [sentence for sentence in sentence_list if '.' in sentence]

# Combine list items into string.
article = ' '.join(sentence_list)

# Summary ratio
summary = summarize(article, ratio=0.3)

# Word pairing
pairs = [
    [
        r"What is the Coronavirus",
        [summary, ]
    ],
    [
        r"How will it affect us?",
        ["I can't see the future", ]
    ],
    [
        r"How log will it last",
        ["No one knows", ]
    ],
    [
        r"Should we be social distancing?",
        ["Yes, this is the best way to slow the spread down so medical entities can keep up with", ]
    ],
    [
        r"What should I be doing right now?",
        ["Try to stay how as much as possible.", ]
    ],
]


def chatty():
    print(
        "Hi, I'm Chatty and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ")  # default message at the start


chat = Chat(pairs, reflections)
chat.converse()
if __name__ == "__main__":
    chatty()