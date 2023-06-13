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
Before we can get to the fun stuff there are a couple of things you need to have installed. Please take the time to _carefully_ go through the rinstallation processes❤️:

## Installations
### 1. Python & Pip
- [Python Installation Guide](https://realpython.com/installing-python/)
- [Pip Installation Guide](https://pip.pypa.io/en/stable/installation/)

### 2. Selenium
This is the python package that allows us to interact with the [WebDriver](#4-chromedriver) to run our code.
```python
pip install selenium
```

### 3. ChromeDriver
We will be scraping using something called a **ChromeDriver**--a type of WebDriver specifically for Chrome. A WebDriver _is an open source tool for automated testing of webapps across many browsers_[^1].

1. To download a ChromeDriver first check what `version` of Google Chrome you are currently running.
2. Then navigate [here](https://chromedriver.chromium.org/downloads) and click the download that matches the version number you just found.
3. Finally, `extract` the chromedriver.exe file and `save it in this folder`
```
TODO: add gif of walkthrough
```

### 4. SQLite3 [_(for optional feature)_](#optional-features)
If you're interested in storing the results of your scraping in a quick and simple database or csv file!
```python
pip install pysqlite3
```

<br>


# Coding Time
Alrighty, assuming that is all done, it's time to get coding! To start, go ahead and open the `scraper.py` file that came with this repository. It should look like this:
```
TODO: add image of what it should look like
```
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

- `chrome_options.add_argument("--log-level=3")` to only show me serious warnings (thank me later)
     - INFO = 0, WARNING = 1, LOG_ERROR = 2, LOG_FATAL = 3.
 
- `browser = webdriver.Chrome(options=chrome_options)` instantiates a ChromeDriver with the options we chose
- `browser.set_window_size(1080, 960)` is just for funsies and, I think, pretty self-explanatory

<br>

> **N.B.** You do not have to call your WebDriver 'browser', this is just a personal preference for me. Often when you read things online it will either be called **browser** or **driver**

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

### Finding Elements
There are several different ways to [locate elements on a webpage using selenium](https://selenium-python.readthedocs.io/locating-elements.html). Here are the 4 methods I use most frequently:

| Method                                            | Element View | Inspect Element View |
|---------------------------------------------------|--------------|----------------------|
| browser.find_element(By.ID, "id")                 |              |                      |
| browser.find_element(By.CLASS_NAME, "class name") |              |                      |
| browser.find_element(By.NAME, "name")             |              |                      |
| browser.find_element(By.XPATH, """"xpath"""")     |              |                      |


<br>

### Using Elements


<br>

# The Results

<br>

# Optional Features

<br>

# Resources
- [84 Popular Sites on the Internet that you can scrape](https://github.com/brendanbailey/Medium/blob/master/robots_txt/wikipedia_popular_sites.csv)
- [Figuring out whether or not you can scrape a site](https://medium.com/@brendangallegobailey/scraping-the-internets-most-popular-websites-a4c6f0be382d)


<br><br>

[^1]: Source: https://chromedriver.chromium.org/
