import requests
import bs4
import os
import sys
url = "http://www.imdb.com/search/title?release_date=2016&sort=user_rating,desc&ref_=adv_nxt&page="

titles_data = [] 
ratings_data = []
generes_data = []

def scrapData():
	title_class = ".lister-item-header"
	rating_class = ".ratings-bar"
	genre_class = ".genre"

	print "fetching..."
	for num in range(1,3):

		r = requests.get(url+str(num))
		rsoup = bs4.BeautifulSoup(r.text,from_encoding='utf-8')
		titles = rsoup.select(title_class)
		ratings = rsoup.select(rating_class)
		genres = rsoup.select(genre_class)
		[titles_data.append(titles[i].find('a').getText()) for i in range(len(titles))]
		[generes_data.append(genres[i].getText().replace('\n','')) for i in range(len(genres))]
		[ratings_data.append(ratings[i].find('strong').getText()) for i in range(len(ratings))]
		print "Received...",len(titles_data),len(ratings_data),len(generes_data)
	print len(titles_data)
	with open('imdb_database.txt','w') as f:
		for i in range(len(titles_data)):
			f.write(str(titles_data[i].encode('utf-8'))+","+str(ratings_data[i].encode('utf-8'))+","+str(generes_data[i].encode('utf-8'))+"\n")

scrapData()