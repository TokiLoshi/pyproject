# ***B's Briefing***
#### ***Video Demo***: <URL"https://www.youtube.com/watch?v=7ElUKyqHJAg">
#### Description: A Flask Web app built in Python and deployed on Heroku to display the news headlines from four publications collected using a script built in Python using the Beautiful Soup Library. 

![Headlines](/static/cs50p_news_headlines.png)

#### Project Layout: 
B's briefing consists of 4 main files: project.py, app.py, helpers.py, and test_project.py. Project.py contains the bulk of the code and is the part of the app that does the scraping. project.py presents the URLs from "TechCrunch" (https://techcrunch.com/), "SFist" (https://sfist.com/news/), "All Africa" (https://allafrica.com/mozambique/?page=1),  and South Africa's Daily Maverick (https://www.dailymaverick.co.za/section/maverick-news/). Main passes the respective URLs into a specific function, get_tech_news(), get_sf_news(), get_africa_news(), and get_sa_news(). As each webpage is structured differently, I extracted the headlines and links with BeautifulSoup in separate functions and returned them independently. 

I wanted to view the headlines and links from my phone for my use case and decided to create a simple, lightweight flask app. In app.py, I set out the routes for a home page, about page, login page, and news page. The @news route in app.py calls all the functions from project.py and passes the response into the jinja template to display. As news is constantly evolving and several publications update throughout the day, I thought it would be a better use case to scrape those sites with a GET request and display them rather than setting up a Cron script. I considered setting up a Cron script and pulling the news at particular times of the day but chose not to as I felt triggering the scraping functions when the page reloads would better suit my browsing needs and would also be a simpler implementation of this app. My get_date_time() function uses the pytz library and the datetime library to return the date and current time for Pacific Standard Time, Eastern Standard Time, European Central Time, and South Africa Standard Time. The South African Development Communities (SADC) region shares South African Standard Time and thus would show me the times for both South Africa and Mozambique. My flask app shows these dates and times for San Francisco, New York, Zurich, and Mozambique, respectively. I was grateful to find this library as the problem sets in this course gave me a sneak peek into the challenges of working with time zones. 

![First Part of News Page](/static/cs50p_newspage_times.png)

In helpers.py, I have a single function from CS50x finance that I similarly used in my CS50x Final project that allows login-required routes. The @news route, where I display the headlines and links, is the only route that requires a login. I reasoned that it would be prudent to hide this page behind a login route to safeguard against the number of calls my scraper would make to those sites. In app.py, I use a .env file that I have git-ignored, and I have stored the credentials for two users, one for admin and one for visitors who request to see the site. The management of sessions and user_ids in app.py is based on pset9 in CS50x, which worked well in this application and my final project. The only difference is that I am hardcoding the visitor and admin ids to simplify the implementation. Depending on how my use of this app evolves, I may look at storing these sessions more dynamically later.

I started with an SQLite database imported from the CS50 library and transferred to PostgreSQL to be compatible with Heroku. I am currently only storing URLs in that database. This could have been handled adequately in a simple .txt file. Still, I chose to implement a database for future features that I am considering, such as to-do lists, weather snapshots, and randomized trivia games. 

In test_project.py, I have a function to test each news and date function using the mock library. This section of the project was the part I found most challenging. It was also my first time using the mock library. I have a lot of room for improvement, and as I build on the app, I hope to keep improving my testing skills. 

## Why this project? 
I'm relatively new to coding and wanted to learn a new skill for my final project for CS50P. Web scraping is a handy skill to add to one's tool kit. This project was the ideal opportunity to get acquainted with the BeautifulSoup library and solve a personal pain point, my news consumption. 

## What problem does it solve? 
Every morning I open my inbox and skim it for anything important, as well as any headlines that jump out at me. However, between the marketing emails and multiple emails per day from Bloomberg, Washington Post, and various other publications, my inbox has snowballed into an atrocious 84,207 unread emails (at the time of writing this). I enjoy Apple News but find it often leads me to doom scrolling through the news, and even then, I still need to navigate to other applications to view the publications I like to keep up-to-date on. B's briefing helps me solve this personal pain point by taking some of the sites I get the most emails from that are not aggregated on Apple News and displaying them on my news dashboard. Limiting it to 4 publications allows me to get a briefing of news that I wouldn't get on Apple News and that I often miss out on in my inbox.

![mobile friendly](/static/cs50p_news_mobile_1.jpg)

Given that I consume most of my news on mobile, it was vital for me to make this mobile responsive, and I used the Bootstrap framework to achieve this. I use Pexels.com for many of my projects because I appreciate the quality of photos and that artists are willing to let people use them for free. I created my demo video using screen recording on my iPhone and QuickTime on my Mac and edited them together using Final Cut Pro. I added the initial graphic and music on Canva.com and am hosting it as an embedded iframe on my app's homepage. I used Font Awesome for icons and got the bumblebee favicon and header image from Twemoji Twitter Icons.

## Credits:
-Red-Framed eyeglasses on newspapers - photo by Suzy Hazelwood: https://www.pexels.com/photo/red-framed-eyeglasses-on-newspapers-3886870/
-Laptop with news on-screen - photo by Jane Doan: https://www.pexels.com/photo/laptop-with-news-on-the-screen-723072/
-321 let's go imaginary text Photo by SevenStorm JUHASZIMRUS: https://www.pexels.com/photo/123-let-s-go-imaginary-text-704767/
-White ceramic mug on top of newspaper - photo by cottonbro studio: https://www.pexels.com/photo/white-ceramic-mug-on-top-of-a-newspaper-3944425/
- Contact Form Template from Canva.com
- Icons from Twemoji Twitter Icons Copyright 2020 Twitter Inc Licensed under CC-BY 4.0 International (CC BY 4.0) https://favicon.io/emoji-favicons/honeybee/
- Frenchie photo by Anna Shvets: https://www.pexels.com/photo/white-and-black-french-bulldog-4587991/
- Panda and Coffee mug photo by Quang Anh Ha Nguyen: https://www.pexels.com/photo/panda-printed-paper-coffee-cup-on-table-885021/
- Golden Gate Bridge photo by Tae Fuller https://www.pexels.com/photo/golden-gate-bridge-san-francisco-california-1141853/
- Code projected over woman photo by ThisIsEngineering from Pexels: https://www.pexels.com/photo/code-projected-over-woman-3861969/.
- Two Rhinos on gray field photo by Frans van Heerden: https://www.pexels.com/photo/two-rhino-on-gray-field-631292/
- Baobab tree under starry sky photo by Harry Cunningham @harry.digital: https://www.pexels.com/photo/tree-under-starry-sky-3347324/

## Additional Photos
![News headlines mobile](/static/cs50p_news_mobile_3.jpg)
![home menu dropdown](/static/cs50p_menu_mobile.jpg)
![mobile login](/static/cs50p_login_mobile.jpg)
![homescreen](/static/cs50p_home_general.png)
![about carousel 1](/static/cs50p_about_page_1.png)
![about carousel 2](/static/cs50p_about_page_2.png)
![about carousel 3](/static/cs50p_about_page_3.png)
## License:
Open Sourced.