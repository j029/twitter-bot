import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement


class TweetActions:

    def __init__(self, driver:WebDriver):
        self.driver = driver
    
    # OLD

    # def like_tweet(self, tweet_element: WebElement):
    #     active_account = 'KingGhostMG' # self.driver.find_element(By)
    #     try:
    #         tweet_element.find_element(By.CSS_SELECTOR, f'a[title="   Unlike from {active_account}  "]')
    #         print(f"Tweet already liked by {active_account}.")
    #     except:
    #         like_element = tweet_element.find_element(By.CSS_SELECTOR, f'a[rel="favorite"]')
    #         like_element_clickable = like_element.find_element(By.XPATH, "..")
    #         like_element_clickable.click()

    #     rand_wait = random.randrange(0,1)
    #     print(f"Waiting for {rand_wait} seconds.")
    #     time.sleep(rand_wait)

    def open_actions_menu(self, tweet_element: WebElement):
        actions_menu_element = tweet_element.find_element(By.CSS_SELECTOR, 'a[rel="actionsMenu"]')
        actions_menu_element_clickable = actions_menu_element.find_element(By.XPATH, "..")
        actions_menu_element_clickable.click()

        return actions_menu_element_clickable

    def close_modal(self):
        dissmiss_element = self.find_element(By.CLASS_NAME, 'js-dismiss')
        dissmiss_element.click()

    def like_tweet(self, tweet_element: WebElement, active_account='MiniGhostMG'):

        actions_menu_element_clickable:WebElement = TweetActions.open_actions_menu(self, tweet_element)

        dropdown_element = actions_menu_element_clickable.find_element(By.CSS_SELECTOR, 'a[data-action="favoriteOrUnfavorite"]')
        dropdown_element_clickable = dropdown_element.find_element(By.XPATH, "..")
        dropdown_element_clickable.click()

        modal_element = self.find_element(By.CSS_SELECTOR, 'div[class="js-modal-inner mdl margin-v--20 s-fluid s-narrow s-fluid-height padding-b--12"]')
        account_name_elements = modal_element.find_elements(By.CLASS_NAME, 'from-handle')

        for account_name_element in account_name_elements:
            if str(account_name_element.get_attribute('innerHTML')).strip() == f'@{active_account}':
                    active_account_name_element = account_name_element
                    account_cell_element = active_account_name_element.find_element(By.XPATH, '../..')

                    like_element = account_cell_element.find_element(By.CLASS_NAME, 'btn-fav-fav-text')

        try:
            like_element.click()
            print(f'{active_account} liked a tweet.')

        except:
            print(f'Teweet is already liked by {active_account}')
            TweetActions.close_modal(self)
                    


        rand_wait = random.randrange(4,15)
        print(f"Waiting for {rand_wait} seconds.")
        time.sleep(rand_wait)

    def retweet_tweet(self, tweet_element: WebElement, active_account='MiniGhostMG', retweet_comment=''):

        retweet_icon_element = tweet_element.find_element(By.CLASS_NAME, 'js-icon-retweet')
        retweet_icon_element.click()

        account_selector_container = self.find_element(By.CSS_SELECTOR, 'div[class="js-account-selector-container"]')
        
        active_account_selector = account_selector_container.find_element(By.CSS_SELECTOR, f'img[alt="{active_account}\'s avatar"]')
        active_account_selector.click()

        retweet_modal = self.find_element(By.XPATH, '//*[@id="actions-modal"]/div')

        if retweet_comment != '':
            retweet_with_comment_button = self.find_element(By.CSS_SELECTOR, 'button[data-action="quote"]')
            retweet_with_comment_button.click()

            comment_text_area = self.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div/div/div[1]/div[7]/textarea')
            comment_text_area.click()
            comment_text_area.send_keys(Keys.CONTROL + "a")
            comment_text_area.send_keys(Keys.DELETE)
            comment_text_area.send_keys(retweet_comment)
            comment_text_area.send_keys(Keys.CONTROL + Keys.RETURN)

            print(f'Retweeted tweet with comment by {active_account}')

            
        else:
            retweet_button = self.find_element(By.CSS_SELECTOR, 'button[data-action="retweet"]')
            retweet_button.click()

            try:
                retweet_modal.find_element(By.CLASS_NAME, 'mdl-dismiss')
                print(f'Tweet is already retweeted by {active_account}')

            except:
                print(f'Retweeted tweet with no comment by {active_account}')

        rand_wait = random.randrange(4,15)
        print(f"Waiting for {rand_wait} seconds.")
        time.sleep(rand_wait)

    def comment_on_tweet(self, tweet_element: WebElement, active_account='MiniGhostMG', comment_text='Wen Moon!'):

        comment_icon_element = tweet_element.find_element(By.CLASS_NAME, 'icon-reply')
        comment_icon_element.click()

        comment_accont_selector_element = self.find_element(By.CLASS_NAME, 'compose-account-img')
        comment_accont_selector_element.click()

        compose_comment_section = self.find_element(By.CLASS_NAME, 'js-compose-scroller')

        active_account_selector = compose_comment_section.find_element(By.CSS_SELECTOR, f'img[alt="{active_account}\'s avatar"]')
        active_account_selector.click()

        comment_text_area = compose_comment_section.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div/div/div[1]/div[7]/textarea')
        comment_text_area.click()
        comment_text_area.send_keys(Keys.CONTROL + "a")
        comment_text_area.send_keys(Keys.DELETE)
        comment_text_area.send_keys(comment_text)
        comment_text_area.send_keys(Keys.CONTROL + Keys.RETURN)

        rand_wait = random.randrange(4,15)
        print(f"Waiting for {rand_wait} seconds.")
        time.sleep(rand_wait)







