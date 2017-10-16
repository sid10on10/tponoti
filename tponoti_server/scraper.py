import requests
from bs4 import BeautifulSoup as bs
import warnings
import hashlib


def write_file(list_hash):
    file1 = open('hashes.txt', 'w')
    for hash_ in list_hash:
        file1.write(hash_ + ",")

def search_hash(hash_):
    file1 = open('hashes.txt', 'r')
    string_hash = " ".join(file1.readlines())
    found = string_hash.find(hash_)
    if found==-1:
        return False
    else:
        return True

log_url = "http://placement.iitbhu.ac.in/accounts/login"

def return_list():
    # Creating session
    sess = requests.session()
    cook_extract = sess.get(log_url)

    #Loading login config files
    ft = open('login.config', 'r')
    lines = ft.readlines()
    username = lines[0]
    password = lines[1]
    my_csrf_token = cook_extract.cookies['csrftoken']
    loggen_in_session = sess.post(log_url, data={'login':username, 'password': password, 'csrfmiddlewaretoken':my_csrf_token}, headers=dict(referer=log_url))
    #Getting noticeboard
    noticeboard_url = "https://www.placement.iitbhu.ac.in/forum/c/notice-board/2017-18/"
    noticeboard = sess.get(noticeboard_url, headers=dict(referer=noticeboard_url))
    #Converting into soup
    soup = bs(noticeboard.text)
    #Searching for posts
    td_rows = soup.findAll("td", {"class": "topic-name"})
    #Extracting post texts
    posts_list = []
    new_post = []
    for post in td_rows:
        a_data = post.find('a')
        a_text = a_data.text
        a_hash = hashlib.sha256(a_text)
        message_digest = a_hash.hexdigest()
        if not search_hash(message_digest):
            new_post.append(a_text)
        posts_list.append(message_digest)
    write_file(posts_list)
    if new_post:
        return new_post
    else:
        return []
