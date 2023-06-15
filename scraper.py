from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# Configuring Browser
#---------------------------------------------------------
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
browser = webdriver.Chrome(options=chrome_options)
browser.set_window_size(1080, 960)



# FILL IN THE BLANKS
#---------------------------------------------------------

def find_subreddit(subreddit):
    """Game Plan:
    - Navigates to Reddit
    - Searches for the subreddit
    - Clicks on link to subreddit

    Args:
        subreddit (str): the subreddit to be visited
    """ 

    # TODO: implement this   



def get_titles():
    """Game Plan:
    - Choose how you want to find the title elements
      - e.g by class name, tag name, xpath, etc
    - Use browser.find_elements(.........)
    - Convert each element in the list into text

    Returns:
        titles (list): a list of titles of posts found in the subreddit
    """    

    # TODO: implement this

    titles = []
    return titles



def display(titles_to_display):
    """Game Plan:
    - Display your results in a cute format <3

    Args:
        titles_to_display (list): the titles to be displayed cutely
    """    

    # TODO: optional implementation





# RUN IT
#---------------------------------------------------------

def run(subreddit):
    """Puts it all together! 
    N.B. Since our browser is a global variable we're not concerned
    about having to pass it around function to function

    Args:
        subreddit (str): the subreddit we wish to scrape
    """  
    find_subreddit(subreddit)

    subreddit_titles = get_titles()

    display(subreddit_titles)



# Uncomment when you're ready. Peer pressure is lame, so no rush <3
# run("Beans")
