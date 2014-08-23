# for py2.x
# -*- coding: utf-8 -*-
import urllib2
import json
import pa_html
import sys
import os
from io import open
import config

def get_shorturl(url):
    gogl_url = "https://www.googleapis.com/urlshortener/v1/url"    
    data = '{"longUrl": "' + url + '"}'
    data_b = data.encode()
    req = urllib2.Request(url=gogl_url, data=data_b)
    req.add_header("Content-Type", "application/json")
    r = urllib2.urlopen(req)
    j_dict = json.loads(r.read().decode())
    return j_dict['id']

def convert(url):

    raw_page = urllib2.urlopen(url)
    readable_page = raw_page.read()
    f = open(config.output_file, encoding='utf-8', mode='w+')
    f.write(readable_page.decode('UTF-8'))
    # f.write(readable_page)
    f.close()
        
    pa_html.main(shorturl=get_shorturl(url), html_file=config.output_file)

def initialize():
    if not os.path.exists(config.output_dir):
        os.makedirs(config.output_dir)
    
def main():

    initialize()

    f = open(config.url_file, "r+")
    for line in f:
        convert(url=line.rstrip())
    f.close()

if __name__ == "__main__":
    sys.exit(main())