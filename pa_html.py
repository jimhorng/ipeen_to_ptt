# for py3.2
from lxml import etree
from io import StringIO
import re
import sys

workspace_dir = "C:/workspace/py/ipeen_2_ptt/"
input_file = workspace_dir + "tmp.html"    
output_dir = workspace_dir + "output/"   

def main(shorturl, html_file):
    dict_xpath = {
        'title' : { 'xpath' : "//h2[@class='cmmtopic']/text()", 'tag' : '標題：'},
        'shop_name' : { 'xpath' : "//div[@class='cmmtop']//a[@class='a38'][1]/text()", 'tag' : '餐廳名稱：'},
        'shop_time' : { 'xpath' : "//span[@class='time'][1]/text()", 'tag' : '消費時間：'},
        'addr' :      { 'xpath' : "//ul[@class='sdata']//li[contains(b,'店址')]/span/text()", 'tag' : '地址：'},
        'price' : { 'xpath' : "//div[@class='cmmtop']//ul//li[1]/b/text()", 'tag' : '每人平均價位：'},
        'recommended' : { 'xpath' : "//div[@class='cmmtop']//ul//li[4]//a[@class='a37'][1]/text()", 'tag' : '推薦菜色：'},
        'content' : { 'xpath' : "//div[@class='cmmcon'][1]//text()", 'tag' : '本文：'},
    }
    
    dict_all = {
        'shorturl' : { 'tag' : '圖文並茂網誌版：'},
        'title' : { 'tag' : '標題：'},
        'shop_name' : { 'tag' : '餐廳名稱：'},
        'shop_time' : { 'tag' : '消費時間：'},
        'addr' :      { 'tag' : '地址：'},
        'price' : { 'tag' : '每人平均價位：'},
        'recommended' : { 'tag' : '推薦菜色：'},
        'content' : { 'tag' : '本文：'},
    }    

    if shorturl == "":
        shorturl = ""
    if html_file == "":
        html_file = input_file
    
    dict_all['shorturl']['value'] = shorturl   
    
    # for sequencing
    list = ['shorturl', 'title', 'shop_name', 'shop_time', 'addr', 'price', 'recommended', 'content']
    
    try:    
        f = open(html_file, encoding='utf-8', mode='r+')
        content = f.read()
        f.close()
        parser = etree.HTMLParser()
        tree   = etree.parse(StringIO(content), parser)       
            
        for k, v in dict_xpath.items():
            r = tree.xpath(dict_xpath[k]['xpath'])
            dict_all[k]['value'] = ''.join(str(n) for n in r)
        
        decorate(dict_all)
        
        f = open(output_dir + dict_all['title']['value'] + ".txt", encoding='utf-8', mode='w+')    
        for k in list:
            f.write(dict_all[k]['tag'] + dict_all[k]['value'])    
            f.write("\n")            
        f.close()
        
    except Exception as ex:
        print("Err :" + ex )   

def decorate(dict):
    dict['shop_time']['value'] = re.sub("\d+:\d+:\d+",'',dict['shop_time']['value']) 
    
    whole = dict['content']['value']
    whole_list = whole.splitlines(True)
    whole_after = "\n\n"
    line_length = 30
    for l in whole_list:
        l = l.lstrip()
        if len(l) > line_length :
            for i in range(0,len(l),line_length):
                whole_after = whole_after + l[i:i+line_length] + "\n"
        elif len(l) <= 2:
            pass
        else:
            whole_after = whole_after + l + "\n"
    dict['content']['value'] = whole_after
    
if __name__ == "__main__":
    main("","")