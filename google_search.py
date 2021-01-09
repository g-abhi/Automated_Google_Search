from googlesearch import search
import time
from selenium import webdriver

class GoogleSearch():
    def __init__(self):
        super().__init__()
    def google_query(self):
        while True:
            google_query = input("Google Search:\n")
            return google_query
    def google_search_results(self, google_query):
        while True:
            searches = search(google_query, lang="en")
            search_results = []
            for item in searches:
                search_results.append(str(item))
            if len(search_results) == 0:
                continue
            else:
                return search_results
    def google_search_results_stats(self, google_query):
        options = webdriver.ChromeOptions()
        options.add_argument('-headless')
        options.add_argument('-no-sandbox')
        options.add_argument('-disable-dev-shm-usage')

        browser = webdriver.Chrome('chromedriver',options=options)
        url = 'https://google.com'
        browser.get(url)
        time.sleep(1)
        name = 'q'
        search_el = browser.find_element_by_name("q")
        search_el.send_keys(google_query)

        submit_btn_el = browser.find_element_by_css_selector("input[type='submit']")
        time.sleep(1)
        submit_btn_el.click()

        search_result_stats = browser.find_element_by_id("result-stats")
        inner_html_search_result_stats = search_result_stats.get_attribute('innerHTML')
        split_inner_html_search_result_stats = inner_html_search_result_stats.split("<", 1)
        count_search_results = split_inner_html_search_result_stats[0]
        time_search_results = split_inner_html_search_result_stats[1].split(" ", 1)[1].split("&", 1)[0]
        return (count_search_results, time_search_results)

    def google_search(self):
        search_query = self.google_query()
        search_results = self.google_search_results(search_query)
        search_stats = self.google_search_results_stats(search_query)
        print()
        print(search_stats[0])
        print(search_stats[1])
        print()
        i = 1
        for result in search_results:
            if not(i > 10 or "/search?q=" in result):
              print(result)
              print()
              i+=1