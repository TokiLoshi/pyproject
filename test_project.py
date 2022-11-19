import pytest
from project import get_tech_news, get_sf_news, get_sa_news, get_africa_news, get_date_time
import requests 
from bs4 import BeautifulSoup
from datetime import datetime
from pytz import timezone
import pytz 

# Need to test each function throughly
def test_tech_news():
  tech_url = "https://techcrunch.com/"
  response = requests.get(tech_url)
  assert type(response) == requests.models.Response
  # Tutorial on checking response status codes: https://medium.com/@novyludek/custom-status-code-matcher-for-api-testing-in-python-with-pyhamcrest-43183d65475d
  assert response.status_code == 200


def test_sf_news():
  sf_url = "https://sfist.com/news/"
  response = requests.get(sf_url)
  assert type(response) == requests.models.Response
  assert response.status_code == 200

def test_sa_news():
  sa_url = "https://www.dailymaverick.co.za/section/maverick-news/"
  response = requests.get(sa_url)
  assert type(response) == requests.models.Response
  assert response.status_code == 200

def test_africa_news():
  africa_url = "https://allafrica.com/mozambique/?page=1"
  response = requests.get(africa_url)
  assert type(response) == requests.models.Response
  assert response.status_code != 500
  assert response.status_code == 200


def test_date_time():
  ...