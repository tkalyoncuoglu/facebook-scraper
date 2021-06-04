from facebook_scraper import FacebookScraper



if __name__ == "__main__":
    scraper = FacebookScraper()
    scraper.login("tkalyoncuoglu@gmail.com", "")
    for post in scraper.get_posts("Av.MustafaKocaman", pages = 1, comments=True):
        print("***************")
        print(post["likes"])
        print(post["comments"])
        print(post["shares"])