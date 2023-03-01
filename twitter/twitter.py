import twitter.constants as const
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from twitter.tweet_filtration import TweetFiltration
from twitter.tweet_pull import TweetReport
from twitter.tweet_actions import TweetActions
from prettytable import PrettyTable

class Twitter(webdriver.Chrome):
    def __init__(self, teardown = False):
        self.teardown = teardown
        options = Options()
        options.add_argument("user-data-dir=C:\\Users\\simmo\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 10")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Twitter, self).__init__(chrome_options=options)
        self.implicitly_wait(15)
        self.maximize_window()
        print("Successfully initialised bot.")

    def __exit__(self, exc_type, exc, traceback):
        if self.teardown:
            self.quit()
            print("Successfully shut down bot.")

    def land_first_page(self):
        self.get(const.BASE_URL)
        print("Successfully landed first page.")

    def apply_filtrations(self, content=None, words=None, retweets='exclude', author='all', mentioning_user=None):
        filtration = TweetFiltration(driver=self)
        filtration.options_toggle(first=True)
        filtration.content_toggle()
        filtration.filter_tweet_content(content)
        filtration.match_words(words)
        filtration.filter_retweets(retweets)
        filtration.content_toggle()
        filtration.authors_toggle(first=True)
        filtration.tweet_by(author)
        filtration.mentioning(mentioning_user)
        filtration.authors_toggle()
        filtration.options_toggle()

    def pull_tweets(self):
        tweet_container = self.find_element(By.CSS_SELECTOR,
            'div[class="js-chirp-container chirp-container"]'
        )
        report = TweetReport(tweet_container)
        tweets_elements = report.pull_tweets()
        report.pull_tweets_attributes()

        return tweets_elements

    
    def lcr_all_tweets(self, active_accounts=['MiniGhostMG']):
        random.shuffle(active_accounts)
        tweets_elements = Twitter.pull_tweets(self)
        for active_account in active_accounts:
            for tweet_element in tweets_elements:
                TweetActions.like_tweet(self, tweet_element, active_account)
                TweetActions.retweet_tweet(self, tweet_element, active_account, '')
                TweetActions.comment_on_tweet(self, tweet_element, active_account, 'Wen Moon!')


        

