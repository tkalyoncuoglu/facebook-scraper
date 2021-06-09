from facebook_scraper import FacebookScraper



#if __name__ == "__main__":
#    scraper = FacebookScraper()
#    scraper.login("tkalyoncuoglu@gmail.com", "pelinbatu")
#    for post in scraper.get_posts("Av.MustafaKocaman", pages = 1, comments=True):
#        print("***************")
#        print(post["likes"])
#        print(post["comments"])
#        print(post["shares"])



from facebook_scraper import FacebookScraper
import datetime
import pytz




if __name__ == "__main__":
    scraper = FacebookScraper()
    scraper.login("kaan.onder@teleskop.app", "")
    # for post in scraper.get_posts("CengizErgunResmi", pages = 1, comments=True):
    #     print("***************")
    #     print(post["likes"])
    #     print(post["comments"])
    #     print(post["shares"])

    word_list = [
       #"murtaza.dayanc"
        #"tekkekoybelediye"
        #"ilkay.girginerdogan.96"
        "profile.php?id=100035360179973"
        #'story.php?story_fbid=450031812852154&id=100035360179973'
    ]

    for word in word_list:
        end_count = 0
        react = 0

        like = 0
        comment = 0
        share = 0
        video = 0
        image = 0

        # like_most = 0
        # like_most_url = 0
        exit_count = 0
        count = 0
        temp_count = 0
        username = word

        utc = pytz.UTC

        posts = scraper.get_posts(username, pages=50000, comments = True)
        for post in posts:
            print(post["time"])
            if post["time"].replace(tzinfo=utc) < datetime.datetime(2020, 12, 31, 23, 59, 59).replace(tzinfo=utc):# and count > 3:
                break
            elif post["time"].replace(tzinfo=utc) >= datetime.datetime(2020, 12, 31, 23, 59, 59).replace(tzinfo=utc) and post[
                "time"].replace(tzinfo=utc) < datetime.datetime(2021, 1, 31, 23, 59, 59).replace(tzinfo=utc):
                count = count + 1
                if post["likes"] is not None:
                    like += int(post["likes"])
                if post["comments"] is not None:
                    comment += int(post["comments"])
                if post["shares"] is not None:
                    share += int(post["shares"])

                if post["image"] is not None:
                    image += 1
                if post["video"] is not None:
                    video += 1

                print("like : {}, comment : {}, share : {}".format(post["likes"], post["comments"], post["shares"]))

        react = like + comment + share
        print(like,comment,share)
        printed = {"username": username, "react": str(react), "post_count": str(count)}
        print(printed)