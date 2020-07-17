#! /usr/bin/env python3
#
# Markus Reinert, 2020-07-17
#
# Create a synthesis of the charts of several movie databases
#
# Current state: searches for matches between the top 250 movies on IMDb
# and the top 100 movies on Rotten Tomatoes

import requests
from bs4 import BeautifulSoup


movies = {}

print("Requesting IMDb")
url_IMDb = "https://www.imdb.com/chart/top"
r = requests.get(url_IMDb, headers={"accept-language": "en-US"})
soup = BeautifulSoup(r.text, "html.parser")

print("Parsing IMDb")
for rank, entry in enumerate(soup.find_all("tr")):
    if rank == 0:
        # Skip the first row; it contains only the table header
        continue
    title = None
    team = None
    year = None
    rating = None
    for i, data in enumerate(entry.find_all("td")):
        if i == 0:
            # Parse metadata
            for info in data.find_all("span"):
                name = info.get("name")
                value = info.get("data-value")
                if name == "rk":
                    # Check rank
                    assert value == str(rank)
                elif name == "ir":
                    rating = float(value)
        elif i == 1:
            # Parse data
            info = data.find("a")
            team = info.get("title")
            title = info.get_text()
            # Remove the brackets around the year and make it an integer
            year = int(data.find("span").get_text()[1:-1])
        else:
            # No more information to parse
            break
    # If a movie with the same title was already found, add so many
    # asterisks to the title until it is unique
    while title in movies:
        print("Title", title, "exists already!  Adding an asterisk (*) to the title.")
        title += "*"
    movies[title] = {"year": year, "team": team, "rank_IMDb": rank, "rating_IMDb": rating}


print("Requesting Rotten Tomatoes")
url_RT = "https://www.rottentomatoes.com/top/bestofrt/"
r = requests.get(url_RT, headers={"accept-language": "en-US"})
soup = BeautifulSoup(r.text, "html.parser")

print("Parsing Rotten Tomatoes")
rank = 1
for entry in soup.find_all("tr"):
    # Find the entry with the current rank
    table_data = entry.find("td")
    if table_data and table_data.get_text() == "{}.".format(rank):
        # Parse movie title and year (the year is in brackets separated
        # by a space from the name)
        name_and_year = entry.find("a").get_text().strip()
        assert name_and_year[-1] == ")"
        assert name_and_year[-7:-5] == " ("
        year = int(name_and_year[-5:-1])
        title = name_and_year[:-7]
        # Parse the score in percent
        score = None
        for span in entry.find_all("span"):
            if span.get("class")[0] == "tMeterScore":
                score = span.get_text()
                assert score[0] == "\xa0"
                assert score[-1] == "%"
                score = int(score[1:-1])
                break
        # Check if the movie is already in the dictionary
        if title in movies and movies[title]["year"] == year:
            # Add its RT rating to the dictionary item
            movies[title]["rank_RT"] = rank
            movies[title]["score_RT"] = score
        else:
            # If this title is already in the list (but with a different
            # year), add so many asterisks to the title until it is unique
            while title in movies:
                print("Title", title, "exists already!  Adding an asterisk (*) to the title.")
                title += "*"
            # Add the title to the movie list
            movies[title] = {"year": year, "rank_RT": rank, "score_RT": score}
        rank += 1

print("\nMovies appearing in the charts of IMDb and Rotten Tomatoes:")
for title, movie in movies.items():
    if "rank_IMDb" in movie and "rank_RT" in movie:
        print(f"IMDb {movie['rank_IMDb']:>3}. ({movie['rating_IMDb']:.1f}) RT {movie['rank_RT']:>2}. ({movie['score_RT']:>3} %) {movie['year']}: {title} ({movie['team']})")
    
