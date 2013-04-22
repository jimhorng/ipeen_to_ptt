# for py3.2
import urllib.request
import json
import pa_html
import sys

#Configuration
workspace_dir = "C:/workspace/py/ipeen_2_ptt/"
url_file = workspace_dir + "urls.txt"
output_file = workspace_dir + "tmp.html"
#/Configuration

def get_shorturl(url):
    gogl_url = "https://www.googleapis.com/urlshortener/v1/url"    
    data = '{"longUrl": "' + url + '"}'
    data_b = data.encode()
    req = urllib.request.Request(url=gogl_url, data=data_b)
    req.add_header("Content-Type", "application/json")
    r = urllib.request.urlopen(req)
    j_dict = json.loads(r.read().decode())
    return j_dict['id']

def convert(url):
    try:    
        raw_page = urllib.request.urlopen(url)
        readable_page = raw_page.read()
        f = open(output_file, encoding='utf-8', mode='w+')
        f.write(readable_page.decode('UTF-8'))
        f.close()
        
    except Exception as ex:
        print("Err :" + ex )
        
    pa_html.main(shorturl=get_shorturl(url), html_file=output_file)
    
def main():    
    f = open(url_file, "r+")
    for line in f:        
        convert(url=line.rstrip())
    f.close()

if __name__ == "__main__":
    sys.exit(main())