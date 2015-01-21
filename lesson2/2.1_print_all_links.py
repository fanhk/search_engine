__author__ = 'fhk'

# page = contents of a web page
page = '<html xmlns="http://www.w3.org/1999/xhtml"><head><title>Udacity</title></head><body><h1>Udacity</h1><p><b>Udacity</b> is a private institution of<a href="http://www.wikipedia.org/wiki/Higher_education">higher education founded by</a> <a href="http://www.wikipedia.org/wiki/Sebastian_Thrun">Sebastian Thrun</a>, David Stavens, and Mike Sokolsky with the goal to provide university-level education that is "both high quality and low cost".</p>   <p> It is the outgrowth of a free computer science class offered in 2011 through Stanford University. Currently, Udacity is working on its second course on building a search engine. Udacity was announced at the 2012 <a href="http://www.wikipedia.org/wiki/Digital_Life_Design">Digital Life Design</a> conference.</p></body></html>'

def get_next_target(s):
    start_link = s.find('<a href=')
    if start_link == -1:
        return None, 0
    start_qoute = s.find('"', start_link)
    end_qoute = s.find('"', start_qoute + 1)
    url = s[start_qoute + 1 : end_qoute]
    return url, end_qoute

def print_all_links(page):
    while page:
        url, end_pos = get_next_target(page)
        if url:
            print url
            page = page[end_pos:]
        else:
            break

print_all_links(page)