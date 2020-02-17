import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://nur.kz/"
html = urlopen(url).read()
print(html)
soup = BeautifulSoup(html)
print(soup)

# убить все элементы скрипта и стиля
for script in soup(["script", "style"]):
    script.extract()    # rip it out

print(soup)
text = soup.get_text()
print(text)

# разбить линии и убрать начальные и конечные пробелы в каждой
lines = (line.strip() for line in text.splitlines())
# разбить несколько заголовков в строке каждый
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# пустые строки
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)
# скачать и распечатать стоп-слова для казахского языка
# nltk.download('stopwords')
stop_words = set(stopwords.words('kazakh'))
print(stop_words)

# токенизировать набор данных
words = word_tokenize(text)
print(words)

# удаляет знаки препинания и цифры
wordsFiltered = [word.lower() for word in words if word.isalpha()]
print(wordsFiltered)

# удалить стоп-слова из набора токенизированных данных
filtered_words = [
    word for word in wordsFiltered if word not in stopwords.words('kazakh')]
print(filtered_words)

wc = WordCloud(max_words=1000, margin=10, background_color='black',
               scale=3, relative_scaling=0.5, width=500, height=400,
               random_state=1).generate(' '.join(filtered_words))

plt.figure(figsize=(20, 10))
plt.imshow(wc)
plt.axis("off")
plt.show()
# wc.to_file("/wordcloud.png")
