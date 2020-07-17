# Reliable Movie Ranking

Reliable Movie Ranking is a short Python code to compare the top movie
lists of several databases and to create a reliable ranking from this.
In its current state, the code parses the top 250 list of IMDb and the
top 100 list of Rotten Tomatoes.  It then prints out the movies which
appear in both lists.

The idea is that the ranking of a single movie database might not be
considered reliable, so having a synthesis of several hit lists might
reflect better the movies that are generally considered as top.  This
software is provided as a (hopefully) easy-to-read Python code, so that
everyone can check that the code does not bias the results.

Since the websites of IMDb and Rotten Tomates might change over time, it
cannot be guaranteed that the code will always work as it is provided
right now.  It works at the time of writing (July 2020), and I hope that
you can update the code if you are reading this in the future and my
parser does not work anymore.

Feel free to extend the functionality of Reliable Movie Ranking to make
it suit your needs.

*Bon film!*


## Results as of 17 July 2020

*The first number is the ranking on IMDb, in brackets is the
 corresponding rating.  The second number is the ranking on Rotten
 Tomatoes, in brackets is the corresponding score.  Then comes the year
 of the movie, its title, and a list of people associated with it
 (usually the producer and two main actors).*

```
Movies appearing in the charts of IMDb and Rotten Tomatoes:
IMDb   2. (9.1) RT 32. ( 98 %) 1972: The Godfather (Francis Ford Coppola (dir.), Marlon Brando, Al Pacino)
IMDb  39. (8.5) RT 24. (100 %) 1936: Modern Times (Charles Chaplin (dir.), Charles Chaplin, Paulette Goddard)
IMDb  40. (8.5) RT 71. ( 96 %) 1960: Psycho (Alfred Hitchcock (dir.), Anthony Perkins, Janet Leigh)
IMDb  49. (8.4) RT 13. ( 99 %) 1942: Casablanca (Michael Curtiz (dir.), Humphrey Bogart, Ingrid Bergman)
IMDb  51. (8.4) RT 95. ( 99 %) 1954: Rear Window (Alfred Hitchcock (dir.), James Stewart, Grace Kelly)
IMDb  52. (8.4) RT 59. ( 98 %) 1979: Alien (Ridley Scott (dir.), Sigourney Weaver, Tom Skerritt)
IMDb  65. (8.4) RT 14. ( 97 %) 2018: Spider-Man: Into the Spider-Verse (Bob Persichetti (dir.), Shameik Moore, Jake Johnson)
IMDb  72. (8.3) RT  2. ( 94 %) 2019: Avengers: Endgame (Anthony Russo (dir.), Robert Downey Jr., Chris Evans)
IMDb  75. (8.3) RT 31. ( 97 %) 2017: Coco (Lee Unkrich (dir.), Anthony Gonzalez, Gael García Bernal)
IMDb  93. (8.3) RT 77. (100 %) 1931: M (Fritz Lang (dir.), Peter Lorre, Ellen Widmann)
IMDb  97. (8.3) RT  8. (100 %) 1941: Citizen Kane (Orson Welles (dir.), Orson Welles, Joseph Cotten)
IMDb 100. (8.2) RT 79. ( 99 %) 1959: North by Northwest (Alfred Hitchcock (dir.), Cary Grant, Eva Marie Saint)
IMDb 104. (8.2) RT 37. (100 %) 1952: Singin' in the Rain (Stanley Donen (dir.), Gene Kelly, Donald O'Connor)
IMDb 108. (8.2) RT 99. ( 98 %) 1962: Lawrence of Arabia (David Lean (dir.), Peter O'Toole, Alec Guinness)
IMDb 112. (8.2) RT 76. ( 97 %) 1927: Metropolis (Fritz Lang (dir.), Brigitte Helm, Alfred Abel)
IMDb 121. (8.2) RT 90. ( 98 %) 2009: Up (Pete Docter (dir.), Edward Asner, Jordan Nagai)
IMDb 139. (8.2) RT 40. ( 99 %) 1950: All About Eve (Joseph L. Mankiewicz (dir.), Bette Davis, Anne Baxter)
IMDb 151. (8.1) RT 84. ( 91 %) 2017: Three Billboards Outside Ebbing, Missouri (Martin McDonagh (dir.), Frances McDormand, Woody Harrelson)
IMDb 154. (8.1) RT 98. ( 99 %) 1974: Chinatown (Roman Polanski (dir.), Jack Nicholson, Faye Dunaway)
IMDb 159. (8.1) RT 22. ( 98 %) 2015: Inside Out (Pete Docter (dir.), Amy Poehler, Bill Hader)
IMDb 176. (8.1) RT 25. ( 99 %) 1949: The Third Man (Carol Reed (dir.), Orson Welles, Joseph Cotten)
IMDb 202. (8.1) RT 63. ( 95 %) 2013: 12 Years a Slave (Steve McQueen (dir.), Chiwetel Ejiofor, Michael Kenneth Williams)
IMDb 203. (8.1) RT 15. ( 97 %) 2015: Mad Max: Fury Road (George Miller (dir.), Tom Hardy, Charlize Theron)
IMDb 219. (8.0) RT 41. ( 93 %) 2017: Logan (James Mangold (dir.), Hugh Jackman, Patrick Stewart)
IMDb 226. (8.0) RT 33. ( 97 %) 2015: Spotlight (Tom McCarthy (dir.), Mark Ruffalo, Michael Keaton)
IMDb 231. (8.0) RT 78. (100 %) 1940: Rebecca (Alfred Hitchcock (dir.), Laurence Olivier, Joan Fontaine)
IMDb 235. (8.0) RT 27. ( 98 %) 1934: It Happened One Night (Frank Capra (dir.), Clark Gable, Claudette Colbert)
```
