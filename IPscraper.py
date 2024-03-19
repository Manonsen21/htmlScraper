"""
Description: Parsing xhtml
Author: Mitchell Anonsen
Section Number:251409
Date Created: March 15th,2024

Updates:
"""

from html.parser import HTMLParser
import urllib.request

class MyHTMLParser(HTMLParser):

    def __init__(self,*, convert_charrefs: bool = ...) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.body = False
        self.ip = ''

    def handle_starttag(self, tag, attr):
        if tag == 'body':
            self.body = True

    def handle_endtag(self, tag):
        if tag == 'body':
            self.body = False

    def handle_data(self, data):
        if self.body is True:
            self.ip = data

def get_ip():
    myparser = MyHTMLParser()
    with urllib.request.urlopen('http://checkip.dyndns.org/') as response:
        html = response.read().decode('utf-8')
    myparser.feed(html)
    return myparser.ip

if __name__ == "__main__":
    print(get_ip())