from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import csv


class BookCrawl:
    def __init__(self, url):
        super()
        self.url = url
        self.browser = webdriver.Chrome(executable_path='./chromedriver')

    def init_csv(self, filename='book.csv'):
        fields = ['title', 'author', 'price']
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
        return (csvwriter, csvfile)

    def get_all_book(self, selector):
        return self.browser.find_elements_by_class_name(selector)

    def get_book_title(self, parent, selector):
        return parent.find_element_by_class_name(selector).text

    def get_book_author(self, parent, selector):
        return parent.find_element_by_class_name(selector).text

    def get_book_price(self, parent, selector):
        return parent.find_element_by_class_name(selector).text

    def crawl(self, filename='book.csv'):
        self.browser.get(self.url)
        sleep(2)
        i = 2
        fields = ['title', 'author', 'price']
        with open(filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            while True:
                all_books = self.get_all_book('content__item-infor')
                for book in all_books:
                    try:
                        book_title = self.get_book_title(
                            book, 'item__infor-title')
                        book_author = self.get_book_author(
                            book, 'item__infor-category')
                        book_price = self.get_book_price(
                            book, 'item__infor-price')
                        if book_title and book_author and book_price:
                            csvwriter.writerow(
                                [book_title, book_author, book_price])
                    except:
                        pass
                if i >= 163:
                    break
                per_link = f'https://www.nxbxaydung.com.vn/sach-noi-bat?lang=vi&page={i}'
                self.browser.get(per_link)
                i += 1
        csvfile.close()
        self.browser.close()


if __name__ == '__main__':
    url = 'https://www.nxbxaydung.com.vn/sach-noi-bat'
    book_crawl = BookCrawl(url)
    book_crawl.crawl()
