__author__ = 'michael'

import requests, datetime, argparse, bs4


def hitLinks(page): #hits and saves all links in a page
    allPages = []
    base = "http://sandiego.craigslist.org"
    soup = bs4.BeautifulSoup(page)
    rows = soup.find_all("p", "row")
    links = [base + tag.contents[1]['href'] for tag in rows if tag.contents is not None]
    for link in links:
        allPages.append(requests.get(link).content)
    return allPages




def fetch_search_results(query=None, minAsk=None, maxAsk=None, bedrooms=None):
    search_params = {
        key: val for key, val in locals().items() if val is not None
    }
    if search_params:
        base = 'http://sandiego.craigslist.org/search/apa'
        resp = requests.get(base, params=search_params, timeout=3)
        resp.raise_for_status()  # <- no-op if status==200
        return resp.content



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="download craigslist results from a search query and filters")
    parser.add_argument("--query", help="cl search query string")
    parser.add_argument("--minAsk", help = "cl search query minimum asking price")
    parser.add_argument("--maxAsk", help="cl search query maximum asking price")
    parser.add_argument("--bedrooms", help="the number of desired bedrooms for apartment listings")
    args = parser.parse_args()
    timestamp = datetime.datetime.now().strftime("cl_results_%H%m%d.html")
    search = fetch_search_results(args.query, args.minAsk, args.maxAsk, args.bedrooms)
    results = hitLinks(search)
    with open(timestamp, 'w') as outFile:
        for line in results:
            try:
                outFile.write(line)
            except:
                pass
    print "search saved to " + timestamp

