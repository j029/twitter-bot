from twitter.twitter import Twitter

with Twitter(teardown = False) as bot:

    try:
        bot.land_first_page()

        # Filter tweets.
        bot.apply_filtrations(content="all", words="MoonGhost", retweets='include', author='MoonGhostNFT', mentioning_user=None)

        # Takes a list of accounts to be used ['KingGhostMG','MiniGhostMG','minionghostmg']
        bot.lcr_all_tweets(['KingGhostMG'])

        # Select tweet.

        # Like retweet and comment on all of the collection tweets.

        """
        bot.decline_cookies()
        # bot.select_currency(currency='GBP')
        bot.select_destination('New York')
        bot.select_dates(check_in_date='2022-10-10', check_out_date='2022-10-13')
        bot.select_guest_and_room_amount()
        bot.search()
        bot.decline_cookies()
        bot.apply_filtrations()
        bot.refresh()
        bot.report_results()
        """

    except Exception as e:
        if 'in PATH' in str(e):
            print('Path error')
        else:
            raise