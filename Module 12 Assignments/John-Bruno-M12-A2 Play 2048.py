#!/usr/bin/env python
# coding: utf-8

# # Automated 2048
# Using ```selenium```, write code that does the following:
# * Starts an instance of Chrome
# * Navigates to https://play2048.co/
# * Plays 10 consecutive games of 2084 and indicates when it is starting each game
# * Print the score of each game it has finished
# * Completes all games without human intervention
# * Prints the best score for the 10 games
# * All of this should be done in a method named **play_2048()**

# A hint is available, but will cost you 5 points. One of the difficult parts of this exercise is determining when the game is over. I have one way to do it that I will share with you for 5 points. If you want the hint and agree not to share it with others, contact one of the TA's.

# Submit this assignment as a .PY file on BB
# 
# As always, your code should be reasonably efficient, utilize error handling, and docstrings where needed.

# In[2]:


#Write your Python code here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

def play_2048():
    """This function opens a website for the game 2048 and plays it 10 times. This requires chromedriver
       in the directory of the script. It outputs the game you are on, that game's score, and the highscore
       out of the 10 games."""
    browser = webdriver.Chrome()
    browser.get('https://play2048.co/')
    htmlElem = browser.find_element_by_tag_name('html')
    i = 0
    while True:
        if i == 10:
                print("GAME OVER.......")
                print("Your high score is:")
                hs = browser.find_element_by_class_name("best-container")
                hs = hs.text
                print(hs)
                break
        htmlElem.send_keys(Keys.RIGHT)
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.LEFT)
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.DOWN)
        try:
            retry = browser.find_element_by_link_text('Try again')
        except NoSuchElementException as no_element_err:
            continue
                
        else:
            print('Playing game' + " " + str(i))
            i = i + 1
            score = browser.find_element_by_class_name("score-container")
            score = int(score.text)
            print('Game' + " " + str(i-1) + " " + 'score:' + " " + str(score))
            time.sleep(2)
            retry.click()
        

if __name__ == '__main__':
    play_2048()

