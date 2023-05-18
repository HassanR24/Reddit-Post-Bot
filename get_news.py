from GoogleNews import GoogleNews


class GetNews():

    def __init__(self):
        self.all_news = []
        gn = GoogleNews()
        # type in your required search query below
        gn.get_news('search query')
        self.search_result = gn.result()

    def get_news(self):
        for news in self.search_result:
            # replace Specific with the required keyword below
            if "specific" in news['title']:
                news_title = news['title']
                news_subtitle = f"https://{news['link']}"
                new_dict = {news_title: news_subtitle}
                self.all_news.append(new_dict)
