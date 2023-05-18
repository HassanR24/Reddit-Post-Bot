from get_news import GetNews
from post_reddit import Reddit


news = GetNews()
news.get_news()

reddit = Reddit()
reddit.login()


# change the number 3 below to set the maxiumum number of news to post, you can remove this to post all the news found. it can be in 100s.
for news in news.all_news[:3]:
    for key, value in news.items():
        reddit.post(title=key, message=value)
