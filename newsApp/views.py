from operator import ne
from django.shortcuts import render
from newsapi import NewsApiClient


def index(request):
    newsApi = NewsApiClient(api_key="c74a92a23a7b468fb8b0848c7635d984")
    headlines = newsApi.get_everything(sources='bbc-news, cnn',
                                       language='en',
                                       page=3)
    articles = headlines['articles']
    desc = []
    news = []
    image = []
    url = []
    source = []

    for i in range(len(articles)):
        article = articles[i]
        desc.append(article['description'])
        news.append(article['title'])
        image.append(article['urlToImage'])
        source.append(article['source'])
        url.append(article['url'])
    mylist = zip(desc, news, image, url, source)
    context = {'mylist': mylist}

    return render(request, 'newsApp/index.html', context)
