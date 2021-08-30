# Flik, a Python Package for Film Buffs

Currently, flik heavily depends on [OMDb](https://www.omdbapi.com/) API. You should first [get](https://www.omdbapi.com/apikey.aspx) your API key. A free subscription is available for up to 1000 requests per day.

To get full information of a title use `fetchinfo` function:

```python
import flik

flik.fetchinfo('se7en', OMDB_API_KEY)
```
The returned object is a python dictionary containing all information about requested title:

```json
{
   "Actors":"Morgan Freeman, Brad Pitt, Kevin Spacey",
   "Awards":"Nominated for 1 Oscar. 29 wins & 42 nominations total",
   "BoxOffice":"$100,125,643",
   "Country":"United States",
   "DVD":"19 Dec 2000",
   "Director":"David Fincher",
   "Genre":"Crime, Drama, Mystery",
   "Language":"English",
   "Metascore":"65",
   "Plot":"Two detectives, a rookie and a veteran, hunt a serial killer who ""uses the seven deadly sins as his motives.",
   "Poster":"https://m.media-amazon.com/images/M/MV5BOTUwODM5MTctZjczMi00OTk4LTg3NWUtNmVhMTAzNTNjYjcyXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg",
   "Production":"New Line Cinema",
   "Rated":"R",
   "Ratings":[
      {
         "Source":"Internet Movie Database",
         "Value":"8.6/10"
      },
      {
         "Source":"Metacritic",
         "Value":"65/100"
      }
   ],
   "Released":"22 Sep 1995",
   "Response":"True",
   "Runtime":"127 min",
   "Title":"Se7en",
   "Type":"movie",
   "Website":"N/A",
   "Writer":"Andrew Kevin Walker",
   "Year":"1995",
   "imdbID":"tt0114369",
   "imdbRating":"8.6",
   "imdbVotes":"1,499,684"
}
```
