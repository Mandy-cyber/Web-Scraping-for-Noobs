# Web Scraping for Noobs

### Table of Contents
| [Introduction](#introduction) | [Setting Up](#setting-up) | [Coding Time](#coding-time) | [The Results](#the-results) | [Optional Features](#optional-features) | [Resources](#resources) |
|-------------------------------|---------------------------|-----------------------------|-----------------------------|-----------------------------------------|-------------------------|

_haha, get it, it's an actual table 🤭_
<br><br>

# Introduction
Hey there party people 👋! 

How is everyone? That's a rhetorical question, I can't hear you... Anywho, I have put together a fun little **template repository** to help introduce the topic of **`Web Scraping in Python🐍`**! We will go through the different requirements and installations to get started, how to go about laying out your code, actually coding, common mistakes, etc, etc.

_Ready... Set..._ **GO!**

<br>

# Setting Up
Before we can get to the fun stuff there are a couple of things you need to have installed. Please take the time to _carefully_ go through the installation processes❤️:

## Installations
### 1. Python & Pip
- [Python Installation Guide](https://realpython.com/installing-python/)
- [Pip Installation Guide](https://pip.pypa.io/en/stable/installation/)

### 2. Selenium
This is the python package that allows us to interact with the [WebDriver](#4-chromedriver) to run our code.
```python
pip install selenium      # or pip3 install selenium
```

### 3. ChromeDriver
We will be scraping using something called a **ChromeDriver**--a type of WebDriver specifically for Chrome. A WebDriver _is an open source tool for automated testing of webapps across many browsers_[^1].

1. To download a ChromeDriver first check what `version` of Google Chrome you are currently running.
2. Then navigate [here](https://chromedriver.chromium.org/downloads) and click the download that matches the version number you just found.
3. Finally, `extract` the chromedriver.exe file and save it in the **same** folder as your code

<div align="center">
  <img src="https://github.com/Mandy-cyber/Web-Scraping-for-Noobs/assets/67931161/e4a1f12e-7fed-486e-b92f-567ffc6bb0c7" height="400px"/>
</div>

### 4. SQLite3 [_(for optional feature)_](#optional-features)
If you're interested in storing the results of your scraping in a quick and simple database or csv file!
```python
pip install pysqlite3      # or pip3 install pysqlite3
```

<br>


# Coding Time
Alrighty, assuming that is all done, it's time to get coding! To start, go ahead and open the `scraper.py` file that came with this repository.

<details>
  <summary>A breakdown of what each of the imports does</summary>
  
  ```python
  from selenium import webdriver                           # so we can instantiate a WebDriver
  from selenium.webdriver.common.keys import Keys          # let's us 'type' things in the browser (i.e. in the searchbar)
  from selenium.webdriver.chrome.options import Options    # so we can configure our WebDriver settings (e.g. how verbose it should be)
  from selenium.webdriver.common.by import By              # to let selenium find elements *by* different identifiers (e.g. by class)
  ```
</details>

With that all sorted let's set up our webdriver.
<br><br>

## 1. Configuring the WebDriver
Most of the time the following code won't change from project-to-project so don't feel bad just copy-pasting it whenever you need it!
```python
# SETTING UP BROWSER
#-----------------------
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
browser = webdriver.Chrome(options=chrome_options)
browser.set_window_size(1080, 960)
```


**The Breakdown**
<br>
- `chrome_options = Options()` allows you to configure your WebDriver to suit your needs. There are a gazillion-and-one different [option arguments](https://peter.sh/experiments/chromium-command-line-switches/) you can add and experiment with.

- `chrome_options.add_argument("--headless")` makes sure that when you run the code, the actual chrome browser doesn't pop up. Comment this out for now 🤓

- `chrome_options.add_argument("--log-level=3")` to only show you important warnings (thank me later)
     - INFO = 0, WARNING = 1, LOG_ERROR = 2, LOG_FATAL = 3.
 
- `browser = webdriver.Chrome(options=chrome_options)` instantiates a ChromeDriver with the options we chose
- `browser.set_window_size(1080, 960)` is just for funsies and, I think, pretty self-explanatory

<br>

> **N.B.** You do not have to call your WebDriver 'browser', this is just my personal preference. Often, when you read things online, it will either be called either **browser** or **driver**

<br>

## 2. Navigating to URLs
For the sake of this 'tutorial', we will be navigating to, and scraping from, **Reddit** as it is and, should continue to be, legal to scrape from. Please always make sure you double check the rules different sites have on web-scraping **_before_** you start a project! 
```python
# TO REDDIT WE GO
#-----------------------
reddit_url = "https://www.reddit.com"
browser.get(reddit_url)
```

<br>

## 3. Interacting with the UI
But, quite frankly, it's not enough to just _go_ to a website, we also want to be able to _interact_ with it, right? Trick question: Right! Interacting with a website could mean:
- Clicking on a button
- Typing in a searchbar or comment section
- Pressing enter
- Scrolling 
- etc

To keep things simple we'll just be focusing on the first three... but before we can do that we need to know how to **find** the elements we want to interact with. How do we find a button to click? Or a searchbar to type in? Check below!

<br>

### Finding Elements
There are several different ways to [locate elements on a webpage using selenium](https://selenium-python.readthedocs.io/locating-elements.html). Here are the 4 methods I use most frequently:

| Method                                            | Element View Example               | Inspect Element View Example               |
|---------------------------------------------------|------------------------------------|--------------------------------------------|
| browser.find_element(By.ID, "id")                 | <img src="images/ID.png"/>         | <img src="images/ID_INSPECT.png"/>         |
| browser.find_element(By.CLASS_NAME, "class name") | <img src="images/CLASS_NAME.png"/> | <img src="images/CLASS_NAME_INSPECT.png"/> |
| browser.find_element(By.NAME, "name")             | <img src="images/NAME.png"/>       | <img src="images/NAME_INSPECT.png"/>       |
| browser.find_element(By.XPATH, """"xpath"""")     | <img src="images/XPATH.png"/>      | <img src="images/XPATH_INSPECT.png"/>      |

<br>

So, going back to our Reddit example: We have navigated to the Reddit website, but now we want to **find** the searchbar so we can look for a specific subreddit.
```python
# N.B. you tend to find that most searchbars' name is just 'q'
searchbar = browser.find_element(By.NAME, "q")
```

<br>

### Using Elements
Again, however, there is more to be done! Finding an element is _not_ the same as using that element. We can **find** a button but not necessarily **use** that button. Worry not though, using elements tends to be super easy! For our purposes, we will focus on:

- If we want to click on something (e.g. a button):
```python
button = browser.find_element(By.ID, "some button id")
button.click()
```

- If we want to type into something (e.g. a searchbar):
```python
searchbar = browser.find_element(By.NAME, "q")
searchbar.send_keys("this is something i want to type in the searchbar")
searchbar.send_keys(Keys.RETURN) # presses 'Enter' (the same as clicking the search button)
```

<br>

## 4. Putting it all together
**Trust me** with the above skills we just covered you are 90% of the way to launching your own scraper! Let's just put the final few pieces together. Here's the plan:
1. Search for "Beans" in the searchbar on Reddit's homepage
2. Click the `r/Beans` subreddit
3. Get a list of all the post titles in the subreddit[^2]
4. Print it out to our terminal or [*insert optional feature here*](#optional-feature)

Give those steps a try by yourself if you think you can, Step 3 is a little harder so don't feel shy taking a peek at my sample code below
```python
TODO: add sample code here
```

## 5. Running It
Okay so who _actually_ waits till the very end to start running their code?? Don't be afraid to try run your code even before it's fully-functional, just to see what's going on.
```python
python scraper.py     # or python3 scraper.py
```

<br>

# The Results
Your final product should (*fingers crossed*) look a bit like this:
```
TODO: add gif of it all running here
```

<br>


## FAQs and Common Mistakes

<details>
  <summary>🤔Which method of finding an element should I use?</summary>
  <br>
  
  > id -> name -> class name -> xpath
  
  <br>
  
Great question! There's a hierarchy of element identification that we typically follow when trying to locate an element, and an element's **id** takes the number one spot. Wherever possible, try to use an element's id as it is _unique_ to it and only it! In cases where that is not possible, next try **name**, then **class name**, and only if nothing else works should you go to **xpath**. 
  
  <br>
  
  The great thing about xpath is it is almost always going to work... if the elements on a webpage do not move (i.e. they remain static). This is especially helpful for older, less responsive, websites. However, several modern-day websites move their elements all around whether it be for responsiveness or even sometimes to fight back bots! This is not to say that you should never use xpath, but instead for you to use it with due caution😅
</details>

<br>

<details>
  <summary>🤔Why do I keep getting Chromedriver-related errors?</summary>
  <br>
  
Trust me, I have been there and **done that**. This is usually because:
  - you have not stored your chromedriver in the *same folder as your code*
  - you accidentally downloaded the wrong chromedriver version
  - between now and the last time you ran your code a couple of days/weeks/months ago, your chromedriver got updated...
  
  
</details>

<br>

# Optional Features
If you are actually reading this section, you are a nerd and I deeply appreciate you for it ❤️.
```
TODO: do this section later
```



<br>

# Resources
- [84 Popular Sites on the Internet that you can scrape](https://github.com/brendanbailey/Medium/blob/master/robots_txt/wikipedia_popular_sites.csv)
- [Figuring out whether or not you can scrape a site](https://medium.com/@brendangallegobailey/scraping-the-internets-most-popular-websites-a4c6f0be382d)
- [My homemade SubRedditScraper python pip package😊](https://pypi.org/project/sreddit/) -- fixing this rn it's so old so reviewers ignore for now LOL


<br><br>

[^1]: Source: https://chromedriver.chromium.org/
[^2]: I say 'all' very loosely. What I really mean is all the ones on the page you see before dynamic-rendering kicks in and makes it a pain to scrape! So you'll get probably get around 10 titles.
