import requests
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import html5lib
import lxml
import re 

# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

def main():
  # Reference tutorial https://realpython.com/beautiful-soup-web-scraper-python/
  # only_a_tags = SoupStrainer("a")
  # only_tags_with_span_abstract = SoupStrainer("fourPack--item-headline hdn-analytics")
  
  html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
  # Testing Beautiful Soup Tutorial 
  # soup = BeautifulSoup(html_doc, "lxml")
  
  # Testing Real Python Tutorial https://realpython.com/beautiful-soup-web-scraper-python/
  # url = "https://realpython.github.io/fake-jobs/"
  # second_url = "https://realpython.github.io/fake-jobs/jobs/senior-python-developer-0.html"
  # page = requests.get(second_url)
  # salad = BeautifulSoup(page.content, "lxml")
  # get_content = salad.find(id="ResultsContainer")
  # title = get_content.find(class_="box")
  # role = title.find("h1")
  # company = (title.find("h2")).text
  # job_description = (title.find("p")).text

  # Trying it out with a website
  # maverick_url = "https://www.dailymaverick.co.za/"
  # page_to_scrape = requests.get(maverick_url)
  # maverick_soup = BeautifulSoup(page_to_scrape.content, "lxml")
  # get_headline = maverick_soup.find(class_="media-left")
  # main_headline = maverick_soup.find("h4").text
  # print("Main Headline: ", main_headline)
  # print("Img alt: ", get_img_alt)
  # print(type(get_img_alt))
  # print("Headline: ", get_img_alt.attrs['alt'])
  # print("Hopefully this is a url: ", get_img_alt.attrs["src"])
  # print(get_headline)
  # print("Alt: ", get_img_alt)

  # Let's try with the article
  # maverick_url_one = "https://www.dailymaverick.co.za/"
  # lets_scrape = requests.get(maverick_url_one)
  # article_soup = BeautifulSoup(lets_scrape.content, "lxml")
  # get_article_items = article_soup.find(class_="wp-block-column no border")
  # get_first_article_url = (article_soup.find(class_="article-0")).attrs['href']

  # This is the code we're keeping:
  # Pulling headlines from daily Maverick 
  # maverick_url_two = "https://www.dailymaverick.co.za/section/maverick-news/"
  # scrape_news = requests.get(maverick_url_two)
  # news_soup = BeautifulSoup(scrape_news.content, "lxml")
  # headlines_soup = news_soup.find(class_="media-item")
  # headlines_link = (headlines_soup.find("a")).attrs['href']
  
  # Get headlines and timestamps
  # headline_one = headlines_soup.find("h1").text
  # time_stamp = headlines_soup.find(class_="date").text
  
  # Get all the media links: 
  # media_links = news_soup.find_all(class_="media-item")
  # list_of_headlines = []
  # cleaned_headlines = []
  # for element in media_links:
  #   headline_test = element.find_all("h1")
  #   list_of_headlines.append(headline_test)
  #   author_test = element.find_all(class_="author")
  #   list_of_headlines.append(author_test)

  # for headline in list_of_headlines:
  #   for element in headline:
  #     cleaned_headlines.append(element.text)
  
  # headlines_no_space = []
  # for i in cleaned_headlines:
  #   headlines_no_space.append(i.strip())

  # link_maybe = news_soup.find_all(class_="media-item")
  # article_links = []
  # for element in link_maybe:
  #   article_links.append(element.find("a")['href'])

  # Article on combining two lists in python in alternating fashion https://datagy.io/python-combine-lists/
  # To do:
  # Let's modify this a bit
  # combined_list = [item for sublist in zip(headlines_no_space, article_links) for item in sublist]

  # for element in combined_list:
  #   print(element)
  # print(combined_list)

  # Local News for San Francisco: 
  # url = "https://sfist.com/news/"
  # sf_results = requests.get(url)
  # sf_soup = BeautifulSoup(sf_results.content, "lxml")
  # headlines = sf_soup.find_all("h2")
  # headlines_list = []
  # for element in headlines:
  #   headlines_list.append(element.text)
  # links = sf_soup.find_all(class_="post-card-image-link")
  # article_links = []
  # for element in links: 
  #   link = "https://sfist.com/" + element.attrs["href"]
  #   article_links.append(link)

  # sf_headlines_combined = [i for sublist in zip(headlines_list, article_links) for i in sublist]
  # for element in sf_headlines_combined:
  #   print(element)

  # Mozambique News: 
  # url = "https://allafrica.com/mozambique/?page=1"
  # get_moz = requests.get(url)
  # moz_soup = BeautifulSoup(get_moz.content, "lxml")
  # moz_headlines = moz_soup.find_all(class_="stories")
  # stories = []
  # for element in moz_headlines:
  #   story = element.find_all("a")
  #   stories.append(story)
  
  # africa_news = []
  # count = 0

  # for story in stories:
  #   for i in story:
  #     africa_title = story[count]["title"]
  #     africa_news.append(africa_title)
  #     africa_summary = story[count].find(class_="summary")
  #     africa_news.append(africa_summary.text)
  #     africa_link = "https://allafrica.com/" + story[count]["href"]
  #     africa_news.append(africa_link)
  #     count += 1

  # for headline in africa_news:
  #   print(headline)

# Tech crunch 
# tech_url = "https://techcrunch.com/"
# try_url = requests.get(tech_url)
# tech_soup = BeautifulSoup(try_url.content, "lxml")
# tech_headline_soup = tech_soup.find_all("h2")
# tech_headlines = []
# count = 0
# for headline in tech_headline_soup:
#   tech_headlines.append(headline)
# tech_news = []
# count = 0
# for story in tech_headline_soup:
#   for i in story.stripped_strings:
#     techcr_headlines = repr((i))
#     tech_news.append(techcr_headlines)

# tech_news_links = []
# for story in tech_headline_soup:
#   headlines = story.find_all("a")
#   for items in headlines:
#     into_headlines = items["href"]
#     tech_news_links.append(into_headlines)
  
# sf_headlines_combined = [i for sublist in zip(headlines_list, article_links) for i in sublist]
# techie_news = [item for sublist in zip(tech_news, tech_news_links) for item in sublist]
# for item in techie_news:
#   print(item)

def function_one():
  ...

def function_two():
  ...

def function_three():
  ...

def function_four():
  ...

if __name__ == main():
  main()