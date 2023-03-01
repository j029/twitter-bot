import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys

class TweetFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def options_toggle(self, first=False):

        # extra steps required due to stale referance error
        options_toggle_path = '//*[@id="container"]/div/section[1]/div/div[1]/header/div/div[2]/a'
        options_toggle_element = self.driver.find_element(By.XPATH, options_toggle_path)
        
        if first:
            time.sleep(0.5)

        options_toggle_element = self.driver.find_element(By.XPATH, options_toggle_path)
        options_toggle_element.click()


    def content_toggle(self):
            content_toggle_element = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/section[1]/div/div[1]/div[1]/div[1]/div[1]/form/div/div/div[1]/div[1]')
            content_toggle_element.click()

    def filter_tweet_content(self, content):
        
        """
        for star_value in star_values:
            star_element_parent = self.driver.find_element(By.CSS_SELECTOR, f'div[data-filters-item="class:class={star_value}"]')
            star_element_label = star_element_parent.find_element(By.CSS_SELECTOR, f'label[class="efeda70352"]')
            star_element_label.click()
        """

        if content:

            # Use inner HTML
            if content == "all":
                content_inner_html = "all Tweets"
            elif content == "images":
                content_inner_html = "Tweets with images"
            elif content == "videos":
                content_inner_html = "Tweets with videos"
            elif content == "gifs":
                content_inner_html = "Tweets with GIFs"
            elif content == "media":
                content_inner_html = "Tweets with any media"
            elif content == "links":
                content_inner_html = "Tweets with links"
            else:
                print(f"Incorrect content filtration: {content}")


            showing_list_element = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/section[1]/div/div[1]/div[1]/div[1]/div[1]/form/div/div/div[1]/div[2]/div/div[1]/div/select')
            showing_child_elements = showing_list_element.find_elements(By.CSS_SELECTOR, '*')

            for showing_element in showing_child_elements:
                if str(showing_element.get_attribute('innerHTML')).strip() == content_inner_html:
                    showing_element.click()

            print(f"Successfully applied content filter to '{content}'.")
        
        else:
            print("No content filtrations to apply.")

    def match_words(self, words):
        
        if words:
            words_input_element = self.driver.find_element(By.CSS_SELECTOR, 'input[class="js-matching search-input"]')
            words_input_element.click()
            words_input_element.send_keys(Keys.CONTROL + "a")
            words_input_element.send_keys(Keys.DELETE)
            words_input_element.send_keys(words)
            words_input_element.send_keys(Keys.RETURN)
            print(f"Successfully matching for: '{words}'.")

        else:
            print("No words to match.")
    
    def filter_retweets(self, retweets='exclude'):

        retweet_list_element = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/section[1]/div/div[1]/div[1]/div[1]/div[1]/form/div/div/div[1]/div[2]/div/div[4]/div/select')
        retweet_child_elements = retweet_list_element.find_elements(By.CSS_SELECTOR, '*')

        if retweets == 'exclude':
            retweet_inner_html = 'excluded'
        elif retweets == 'include':
            retweet_inner_html = 'included'

        for retweet_element in retweet_child_elements:
            if str(retweet_element.get_attribute('innerHTML')).strip() == retweet_inner_html:
                retweet_element.click()

        print(f"Successfully applied filter to '{retweets}' retweets.")
        
    def authors_toggle(self, first=False):

        if first:
            time.sleep(0.5)

        authors_toggle_element = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/section[1]/div/div[1]/div[1]/div[1]/div[1]/form/div/div/div[2]/div[1]')
        authors_toggle_element.click()
    
    def tweet_by(self, author='all'):

        tweet_by_list_element = self.driver.find_element(By.CSS_SELECTOR, 'select[data-title="tweets_from"]')
        tweet_by_list_element.click()
        tweet_by_child_elements = tweet_by_list_element.find_elements(By.CSS_SELECTOR, '*')

        if author == 'all':
            tweet_by_inner_html = 'all users'
        elif author == 'me':
            tweet_by_inner_html = 'me…'
        elif author == 'verified':
            tweet_by_inner_html = 'verified users'
        else:
            tweet_by_inner_html = 'specific user…'

        for tweet_by_element in tweet_by_child_elements:
            if str(tweet_by_element.get_attribute('innerHTML')).strip() == tweet_by_inner_html:
                tweet_by_element.click()

                print(f"Successfully applied author to '{author}'.")

                if tweet_by_inner_html == 'specific user…':
                    username_input_element = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/section[1]/div/div[1]/div[1]/div[1]/div[1]/form/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/input')
                    username_input_element.click()
                    username_input_element.send_keys(Keys.CONTROL + "a")
                    username_input_element.send_keys(Keys.DELETE)
                    username_input_element.send_keys(author)
                    username_input_element.send_keys(Keys.RETURN)
                

    def mentioning(self, mentioning_user=None):

        mentioning_list_element = self.driver.find_element(By.CSS_SELECTOR, 'select[data-title="mentioning"]')
        mentioning_list_element.click()
        mentioning_child_elements = mentioning_list_element.find_elements(By.CSS_SELECTOR, '*')

        if mentioning_user == None:
            mentioning_inner_html = '-'
        elif mentioning_user == 'me':
            mentioning_inner_html = 'me…'
        else:
            mentioning_inner_html = 'specific user…'


        for mentioning_element in mentioning_child_elements:
            if str(mentioning_element.get_attribute('innerHTML')).strip() == mentioning_inner_html:
                mentioning_element.click()

                print(f"Successfully filtered for tweets mentioning '{mentioning_user}'.")

                if mentioning_inner_html == 'specific user…':
                    username_input_element = self.driver.find_element(By.CSS_SELECTOR, 'input[data-title="mentioning_user"]')
                    username_input_element.click()
                    username_input_element.send_keys(Keys.CONTROL + "a")
                    username_input_element.send_keys(Keys.DELETE)
                    username_input_element.send_keys(mentioning_user)
                    username_input_element.send_keys(Keys.RETURN)
                    