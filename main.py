from flask import Flask, request, render_template
app = Flask(__name__)
from bs4 import BeautifulSoup
import urllib2
import cgi
from collections import Counter

def process_soup(soup):
    # base case
    if type(soup) != bs4.element.Tag:
        return str(soup)
    res = []
    res.append({'class': soup.name})
    for c in soup.children:
        res.append({'class':s})

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/api/website', methods=['POST'])
def get_website():
    print "Request form" + str(request.form)
    url = request.form['website']
    try:
        response = urllib2.urlopen(url)
    except:
        return "Bad URL. Please try again"
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    c = Counter([t.name for t in soup.findAll()])
    print c

    # process the soup contents

    attributes = {
            'soup': soup,
            'url': url,
            'counter': list(c.items()),
            'source': soup.prettify(),
            'source_split': soup.prettify().split('\n')
            }
    return render_template('web.html', **attributes)


if __name__ == '__main__':
    app.run(debug=True)


