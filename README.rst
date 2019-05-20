Sanitizer
######################

This project is supposed to preprocess the collected news in csv files.
The following steps are done by the project:
1- Read csv file row by row.
2- Remove extra tags like script, style, html, ... in huffingtonPost
3- Convert all words to lower case.
4- Covert all apostrophes into standard lexicons.
5- Remove single quotes, double quotes and other extra characters.
6- Remove all punctuations.
7- Convert numbers to words (cardinal and ordinal)
8- Save in new csv file.

Run
=============
To run this project you have to run main.py in pycharm.

Open Issues
=============
1- Spell correction with JamSpell
2- Grammer check