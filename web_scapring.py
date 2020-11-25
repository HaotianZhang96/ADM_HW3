from bs4 import BeautifulSoup
import requests
import os

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


def save_page_in_folder(page_urls, start_page_number, path):
    
    page_directory_list = [] #list of paths

    #create directories if don't exist 
    for page_number in range(len(page_urls)):
        page_directory = os.path.join('data','page_' +  str(start_page_number + page_number + 1))
        page_directory_list.append(page_directory)
        if not os.path.exists(page_directory):
            os.makedirs(page_directory)

    #get all the books html and save in folders 
    for page_number in range(len(page_urls)):
        book_list = page_urls[page_number]
        page_folder = page_directory_list[page_number]
        for book_number in range(len(book_list)):
            book_file_path = os.path.join(page_folder, 'content_' +
             str(100*(start_page_number + page_number) + 1 + book_number) + '.txt')

            book_web = requests.get(book_list[book_number])

            with open(book_file_path, 'w', encoding="utf-8") as output_file:
                output_file.write(book_web.text)


if __name__ == "__main__":
    
    #save_books_url('bookurls.txt') commented because the urls have already been stored

    source_path = os.path.dirname(__file__) 
    
    all_urls = get_url_list(os.path.join(source_path, 'bookurls.txt'))    
    
    pages_urls = [all_urls[i:i + 100] for i in range(0, len(all_urls), 100)] # split list in 300 sublists of 100 items   
    
    
    save_page_in_folder([pages_urls[83]], 83, source_path) #first 100 pages
    
    #save_page_in_folder(pages_urls[100:200], 100, source_path) #from page 101 to 200 pages
    
    #save_page_in_folder(page_urls[200:300], 200, source_path)) #from page 101 to 300 pages