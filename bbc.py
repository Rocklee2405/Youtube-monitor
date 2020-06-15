#!/bin/bash
import requests
import ffmpy
from bs4 import BeautifulSoup
import time
import os
import sys
import logging
import youtube_dl
from random  import randint
from time import sleep

links_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'links_bbc.txt')
headers = {
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}
YOUTUBE_LINK = "https://www.youtube.com"
url = "https://www.youtube.com/watch?v=PZPOhy-WKag&list=PLxKLMN7WdG5CHfeZ1UnctPFPBY4zOsc1R"
# url = "https://www.youtube.com/watch?v=L1ZcI-gRF5M&list=PLQQvviScWAtjZkyWoV8lVe-vtV4E53wC1"
# url = "https://www.youtube.com/watch?v=COVe3amiX58&list=PLziN5TdT0bhSpADE9Sa6HOWpw2mJB149w"
# url = os.environ.get('LINK', None)


def get_current_link():
    source_code = requests.request("GET", url, headers=headers).content
    soup = BeautifulSoup(source_code, 'html.parser')
    links = []
    for a in soup.findAll('a', attrs={'class':'yt-uix-tile-link'}):
        links.append(a.get('href'))
    link_set = set()
    if os.path.exists(links_file):
        with open(links_file) as file_data:
            link_set_handled = file_data.read().split('\n')
    else:
        link_set_handled = []
    for link in links:
        link_set.add(link)
    link_need_handle = link_set - set(link_set_handled)
    save_links_handled = (list(link_need_handle) + link_set_handled)[:10000]
    with open(links_file, 'w') as file_data:
            file_data.writelines("\n".join(save_links_handled))
    return link_need_handle


def get_audio_file():
    link_need_handle = get_current_link()
    output = []
    for link_video in link_need_handle:
        link_download =  YOUTUBE_LINK + link_video
        options = {
            'continue' : 'continue',
            'ignoreerrors': True,
            'nooverwrites' : 'nooverwrites',
            'outtmpl' : '/temp' + '/%(id)s.%(ext)s',
            'format' : 'bestaudio[ext=webm]',
            'merge_ouput_format': 'webm',
        }
        with youtube_dl.YoutubeDL(options) as ydl:
            try:
                meta = ydl.extract_info(link_download, download=False)
                ydl.download([link_download])
                output.append('/temp/' + meta['id'] + '.wav')
            except:
                continue
            #yield ('/temp/' + meta['title'] + '.wav')
        sleep(randint(3, 5))
    return output

