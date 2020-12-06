# ADM_HW3 - Which book would you recomend?
ADM homework3 finished by Sanduni, Alessandra and Haotian Zhang

## Goal

The repository contains the files used to the Homework 3 of Algorithmic Methods of Data Mining.

Academic year 2020–2021.

The goal of the project is retrieve informations from the web, in particular from the [goodread data](https://www.goodreads.com/), clean up the data properly, apply text analysis tools such as IDTFT, and creating three different search engines.

## Contents

1) web_scapring.py

The script used to retrieve web pages from the site of [Good Reads](https://www.goodreads.com/).

The script creates 30 000 files tsv organized in 300 folders. Each tsv file contain the html of the page on one book. 



2) scapring_from_html.ipynb

The notebook, using BeautifulSoap, parse the informations from the html web page and write these informations in tsv files.

The informations retrived are:

- title

- author

- series

- Ratings

- Number of givent ratings 

- Number of reviews 

- The entire plot

- Number of pages (to save as NumberofPages)

- Publishing Date 

- Characters

- Setting

- Url

In more detail, it reads each file specified in the previous point and obtains the information to be saved in as many files.


3) main.py 

The notebook perform the analysis and build the three search engines.
