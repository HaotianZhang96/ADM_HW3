from bs4 import BeautifulSoup
import requests

home_page = 'https://www.goodreads.com'

""" save the all the 300*100 url of the books in a file """
def save_books_url(filename):
    main_link = "https://www.goodreads.com/list/show/1.Best_Books_Ever?page="
    
    link_list = [] # list of all links 
    for i in range(1,301):
        page_link = main_link + str(i)
        page = requests.get(page_link)        
        soup = BeautifulSoup(page.content, 'lxml')
        
        link_list += list(map(lambda x: home_page + x.get('href'), soup.find_all("a", class_="bookTitle")))

    #stored on file 
    with open(filename, 'w') as file_handler:
        for item in link_list:
            file_handler.write("{}\n".format(item))     
        
""" return a list of strings from a file reading line by line """
def get_url_list(filename):
    with open(filename, 'r') as inputFile:
        urls = inputFile.read().splitlines()
        return urls
        

if __name__ == "__main__":
    #save_books_url('bookurls.txt') commented because the urls have already been stored
    urls = get_url_list('bookurls.txt') 
    