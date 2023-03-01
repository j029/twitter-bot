from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class TweetReport:
    def __init__(self, boxes_section_element:WebElement):

        self.tweets_section_element = boxes_section_element
        self.tweets = self.pull_tweets()

    def pull_tweets(self):

        print('Found tweets')
        return self.tweets_section_element.find_elements(By.CSS_SELECTOR, 'article[class="stream-item js-stream-item  is-draggable  is-actionable "]')

    def pull_tweets_attributes(self):

        collection = []
        
        for tweet in self.tweets:
            
            author_name = tweet.find_element(By.CSS_SELECTOR, 'b[class="fullname link-complex-target"]').get_attribute('innerHTML').strip()
            
            collection.append([author_name])

        return collection
