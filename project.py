import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import html5lib
import lxml
import re 
from datetime import datetime, timedelta
from pytz import timezone
import pytz

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

def main():
  # Reference tutorial https://realpython.com/beautiful-soup-web-scraper-python/
  # only_a_tags = SoupStrainer("a")
  # only_tags_with_span_abstract = SoupStrainer("fourPack--item-headline hdn-analytics")
  
  # Tech crunch get tech news:
  tech_url = "https://techcrunch.com/"
  tech_news = get_tech_news(tech_url)

  # San Francisco News
  sf_url = "https://sfist.com/news/"
  sf_news = get_sf_news(sf_url)

  # Africa news
  africa_url = "https://allafrica.com/mozambique/?page=1"
  africa_news = get_africa_news(africa_url)

  # SA news
  sa_url = "https://www.dailymaverick.co.za/section/maverick-news/"
  sa_news = get_sa_news(sa_url)

  # current_european_time, current_african_time
  current_sf, current_eastcoast, current_time_europe, current_time_africa = get_date_time()

  # Return to app so it can render
  return tech_news, sf_news, africa_news, sa_news

def get_tech_news(tech_url):
  # Tech crunch 
  url = tech_url
  print("URL We're trying in tech news function", tech_url)
  try_url = requests.get(tech_url)
  tech_soup = BeautifulSoup(try_url.content, "lxml")
  tech_headline_soup = tech_soup.find_all("h2")
  tech_headlines = []
  count = 0
  for headline in tech_headline_soup:
    tech_headlines.append(headline)
  tech_news = []
  count = 0
  for story in tech_headline_soup:
    for i in story.stripped_strings:
      techcr_headlines = repr((i))
      tech_news.append(techcr_headlines)

  tech_news_links = []
  for story in tech_headline_soup:
    headlines = story.find_all("a")
    for items in headlines:
      into_headlines = items["href"]
      tech_news_links.append(into_headlines)
    
  techie_news = [item for sublist in zip(tech_news, tech_news_links) for item in sublist]
  
  return techie_news

def get_sf_news(sf_url):
    # Local News for San Francisco: 
    sf_results = requests.get(sf_url)
    sf_soup = BeautifulSoup(sf_results.content, "lxml")
    headlines = sf_soup.find_all("h2")
    headlines_list = []
    for element in headlines:
      headlines_list.append(element.text)
    links = sf_soup.find_all(class_="post-card-image-link")
    article_links = []
    for element in links: 
      link = "https://sfist.com/" + element.attrs["href"]
      article_links.append(link)

    sf_headlines_combined = [i for sublist in zip(headlines_list, article_links) for i in sublist]
    return sf_headlines_combined

def get_sa_news(sa_url):

    # Pulling headlines from daily Maverick 
    scrape_news = requests.get(sa_url)
    news_soup = BeautifulSoup(scrape_news.content, "lxml")
    headlines_soup = news_soup.find(class_="media-item")
    headlines_link = (headlines_soup.find("a")).attrs['href']
    
    # Get headlines and timestamps
    headline_one = headlines_soup.find("h1").text
    time_stamp = headlines_soup.find(class_="date").text
    
    # Get all the media links: 
    media_links = news_soup.find_all(class_="media-item")
    list_of_headlines = []
    cleaned_headlines = []
    for element in media_links:
      headline_test = element.find_all("h1")
      list_of_headlines.append(headline_test)
      author_test = element.find_all(class_="author")
      list_of_headlines.append(author_test)

    for headline in list_of_headlines:
      for element in headline:
        cleaned_headlines.append(element.text)
    
    headlines_no_space = []
    for i in cleaned_headlines:
      headlines_no_space.append(i.strip())

    link_maybe = news_soup.find_all(class_="media-item")
    article_links = []
    for element in link_maybe:
      article_links.append(element.find("a")['href'])

    # Article on combining two lists in python in alternating fashion https://datagy.io/python-combine-lists/
    combined_list = [item for sublist in zip(headlines_no_space, article_links) for item in sublist]

    # for element in combined_list:
    #   print(element)
    # print(combined_list)
    return combined_list


def get_africa_news(africa_url):
  get_moz = requests.get(africa_url)
  moz_soup = BeautifulSoup(get_moz.content, "lxml")
  moz_headlines = moz_soup.find_all(class_="stories")
  stories = []
  for element in moz_headlines:
    story = element.find_all("a")
    stories.append(story)
  
  africa_news = []
  count = 0

  for story in stories:
    for i in story:
      africa_title = story[count]["title"]
      africa_news.append(africa_title)
      africa_summary = story[count].find(class_="summary")
      africa_news.append(africa_summary.text)
      africa_link = "https://allafrica.com/" + story[count]["href"]
      africa_news.append(africa_link)
      count += 1

  return africa_news

def get_date_time():
  # Get today's date using the freecodecamp tutorial https://www.freecodecamp.org/news/how-to-get-the-current-time-in-python-with-datetime/#:~:text=You%20can%20get%20the%20current%20time%20in%20a%20particular%20timezone,with%20another%20module%20called%20pytz%20.&text=You%20can%20then%20check%20for,all%20timezones%20of%20the%20world.
  # documents library https://pytz.sourceforge.net/
  utc = pytz.utc
  utc.zone
  pacific_standardtime = timezone('America/Los_Angeles')
  east_coast = timezone('America/New_York')
  europe_time = timezone('Europe/Zurich')
  moz_time = timezone('Africa/Maputo')
  sftime = datetime.now(pacific_standardtime)
  east_coast_time = datetime.now(east_coast)
  european_time = datetime.now(europe_time)
  africa_time = datetime.now(moz_time)
  current_sf_time = sftime.strftime("%Y-%m-%d %H:%M")
  current_east_time = east_coast_time.strftime("%Y-%m-%d %H:%M")
  current_european_time = european_time.strftime("%Y-%m-%d %H:%M")
  current_african_time = africa_time.strftime("%Y-%m-%d %H:%M")
  return current_sf_time, current_east_time, current_european_time, current_african_time


if __name__ == main():
  main()