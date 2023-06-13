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
  SOME CODE GOES HERE
  ```
</details>

🌟 With that all sorted let's set up our webdriver.
<br><br>

### WebDriver


<br>

### Navigating to URLs

<br>

### Interacting with UI

<br>

#### Finding Elements


<br>

# The Results

<br>

# Optional Features

<br>

# Resources


<br><br>

[^1]: Source: https://chromedriver.chromium.org/
