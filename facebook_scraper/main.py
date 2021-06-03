from facebook_scraper import FacebookScraper



if __name__ == "__main__":
    scraper = FacebookScraper()
    scraper.login("tkalyoncuoglu@gmail.com", "cbr600aktar12")
    for post in scraper.get_posts("CengizErgunResmi", pages = 1, comments=True):
        print("***************")
        print(post["likes"])
        print(post["comments"])
        print(post["shares"])