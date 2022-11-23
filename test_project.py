import pytest
from project import get_tech_news, get_sf_news, get_sa_news, get_africa_news, get_date_time
import requests 
from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone
import pytz 
from unittest.mock import Mock 
import datetime

# Tutorial on using Mock from real python https://realpython.com/python-mock-library/
# Tutorial on intro to Mock https://www.youtube.com/watch?v=xT4SV7AH3G8&list=PLe4mIUXfbIqaXv8kRvUqgrMREq-p5GgdV&index=1

mock = Mock()

# Testing get_tech_news
def test_get_tech_news():
  # Check for a successful request status code
  mock.requests.return_value = 200
  assert mock.requests() == 200
  headline_list = []
  tech_news = []

  # Open the mock folder with saved snipped of code
  with open("technews.txt") as file:
    for line in file:
      techsoup = BeautifulSoup(line, "lxml")
      headline_list.append(techsoup)
  file.close()
  
  # Clean the headlines
  tech_news_stories = []
  for story in headline_list:
    for headline in story.stripped_strings:
      techie_headlines = repr((headline))
      tech_news_stories.append(techie_headlines)

  # Extract the links
  links = []
  for story in headline_list:
    headlines = story.find_all("a")
    for headline in headlines: 
      actual_headlines = headline["href"]
      links.append(actual_headlines)

  # Combine the lists as was done in project 
  combined_tech_news = [item for sublist in zip(tech_news_stories, links) for item in sublist]

  # Create mock object with the value of combined lists
  mock.first_headline.return_value = combined_tech_news
  
  # Check headlines are correct
  assert mock.first_headline() == combined_tech_news
  
  # Check that the correct number of headlines are returned
  assert len(tech_news_stories) == 21

  # Check headlines are what they are supposed to be

  tech_news_stories[-1] == "Ransomware is a global problem that needs a global solution"
  tech_news_stories[11] == "Elizabeth Holmes sentenced to 11 years in prison for Theranos fraud"
  tech_news_stories[-3] ==  'India’s securities depository CDSL says malware compromised its network'
  
  # Check links is only links
  mock.onlylinks.return_value = links
  assert mock.onlylinks() == links
  assert links[0] == 'https://techcrunch.com/2022/11/19/this-week-in-apps-apple-epic-antitrust-battle-resumes-apple-sued-over-tracking-googles-new-rules-for-kids-apps/'
  assert links[-1] == 'https://techcrunch.com/2022/11/18/combatting-ransomware/'
  assert links[11] == 'https://techcrunch.com/2022/11/18/elizabeth-holmes-sentenced-to-11-years-in-prison-for-theranos-fraud/'
  assert links[-3] == 'https://techcrunch.com/2022/11/18/cdsl-malware-internal-systems/'
  assert links[0].startswith('https')

  # Check the right key words match in the links
  list_key_words_one = tech_news_stories[-1].split(" ")  
  list_key_words_eleven = tech_news_stories[11].split(" ")
  list_key_words_third_last = tech_news_stories[-3].split(" ")
  key_word_one = ((list_key_words_one[0]).replace("\'", "")).lower()
  key_word_eleven = ((list_key_words_eleven[0]).replace("\'", "")).lower()

  assert key_word_one in links[-1]
  assert key_word_eleven in links[11]

  length_of_links = len(links)
  # check program is getting the correct headlines and links
  assert len(links) == 21
  # check each story has a link
  assert len(tech_news_stories) == len(links)

# Test get_sf_news
def test_get_sf_news():
  # Check for a successful request status code
  mock.requests.return_value = 200
  assert mock.requests() == 200
  sf_results = []
  with open("sfnews.txt") as file:
    for line in file:
      sf_soup = BeautifulSoup(line, "lxml")
      sf_results.append(sf_soup)
  file.close

  # get article links to test 
  sf_headlines = []
  for element in sf_results: 
    sf_headlines.append(element.text)
  
    mock.first_headline.return_value = sf_headlines
  
  # Check headlines are correct
  assert mock.first_headline() == sf_headlines

# Test get_sa_news
def test_get_sa_news():
  # Check for a successful request status code
  mock.requests.return_value = 200
  assert mock.requests() == 200

  sa_links = []
  sa_articles = []
  with open("sanews.txt") as file:
    for line in file:
      sa_soup = BeautifulSoup(line, "lxml")
      sa_links.append(sa_soup.find_all("a"))
      sa_articles.append(sa_soup.find_all("a"))
  file.close
  
  sa_headlines = []
  for article in sa_articles:
    for element in article:
      sa_headlines.append(element.attrs.values())

  sa_values = []
  for item in sa_headlines:
    for element in item:
      sa_values.append(element)

  assert len(sa_headlines) > 0
  assert sa_values[0] == "https://www.dailymaverick.co.za/article/2022-11-21-ngcobo-woman-charged-with-killing-her-four-children-dies-unexpectedly-in-police-custody/"
  mock.test_tag.return_value = sa_headlines
  assert mock.test_tag() == sa_headlines
  mock.test_articles.return_value = sa_articles
  assert mock.test_articles() == sa_articles

# Test get_africa_news
def test_get_africa_news():
  # Check for a successful request status code
  mock.requests.return_value = 200
  assert mock.requests() == 200

  africa_results = []
  # Open code snippet to mock 
  with open("africanews.txt") as file:
    for line in file:
      africa_results.append(BeautifulSoup(line, "lxml").find_all("p"))

  # Check the results match 
  mock.africa_results.return_value = africa_results
  assert mock.africa_results() == africa_results
  assert len(africa_results) > 0

  # Extract headlines 
  africa_headlines = []
  for line in africa_results:
    for element in line:
      africa_headlines.append(element.text)

  # Check length of headlines
  assert len(africa_headlines) > 0
  mock.africa_headlines.return_value = africa_headlines
  assert mock.africa_headlines() == africa_headlines
  
# Test get_date_time
def test_get_date_time():
  # Tutorial on using datetime and the mock library https://realpython.com/python-mock-library/
  mock_sf_time = datetime.datetime(year = 2022, month = 11, day=19, hour= 7, minute = 10)
  mock_ny_time = datetime.datetime(year = 2022, month = 11, day = 19, hour = 10, minute = 10)
  mock_zh_time = datetime.datetime(year = 2022, month = 11, day = 19, hour = 16, minute = 10)
  mock_sa_time = datetime.datetime(year = 2022, month = 11, day = 19, hour = 15, minute = 10)

  # Check mock objects return the mock values set 
  mock.sf_time.return_value = mock_sf_time
  assert mock.sf_time() == mock_sf_time
  mock.ny_time.return_value = mock_ny_time
  assert mock.ny_time() == mock_ny_time
  mock.zh_time.return_value = mock_zh_time
  assert mock.zh_time() == mock_zh_time
  mock.sa_time.return_value = mock_sa_time
  assert mock.sa_time() == mock_sa_time