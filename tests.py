from classes.site import Site
from classes.request import Request
from classes.crawler import Crawler

site = Site()

def test_list_sites():
    assert type(site.available_sites()) == type(list())

def test_find_url_site_passing_number():
    assert type(site.find_url_site(0)) == type(str())

def test_find_url_site_passing_string():
    assert type(site.find_url_site('asdasd')) == type(str())

def test_content_page():
    request = Request('http://www.vagalume.com.br', 'michael jackson')
    assert type(request.content_page()) == type(str())

def test_content_page_error():
    request = Request('http://www.testee.com.br', 'michael jackson')
    assert request.content_page() == False

def test_find_musics():
    request = Request('http://www.vagalume.com.br', 'michael jackson')
    crawler = Crawler(request.content_page(), 20)
    assert type(crawler.find_musics()) == type(list())

def test_number_songs():
    request = Request('http://www.vagalume.com.br', 'michael jackson')
    crawler = Crawler(request.content_page(), 20)
    musics = crawler.find_musics()
    total = crawler.number_songs(musics)
    assert type(total) == type(int())
