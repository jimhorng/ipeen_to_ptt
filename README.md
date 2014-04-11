ipeen_to_ptt
============
This is a simple tool used to crawl ipeen's article and transform to ptt's food board's format. <br/>
Prereq:
<ul>
    <li> lxml (precompiled: http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml)
</ul>
Usage:
<ol>
    <li> Configure directory setting @ #configuration ~ #/configuration
    <li> Enter url for ipeen's article @ urls.txt
    <li> Run get_html.py
    <li> All articles under urls.txt will be transform to ptt format articles in /output directory
</ol>
