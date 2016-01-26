#!/usr/bin/python3
import json
import urllib.request, urllib.parse
import webbrowser
# 

search_phrase = input('Search for: ')


def showsome(searchfor):
    query = urllib.parse.urlencode({'q': searchfor})
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % query
    search_response = urllib.request.urlopen(url)
    search_results = search_response.read().decode("utf8")
    results = json.loads(search_results)
    data = results['responseData']
    # print('Total results: %s' % data['cursor']['estimatedResultCount'])
    hits = data['results']
    print('Top %d hits:' % len(hits))
    for h in hits:
        print(' ', h['url'])
    print(hits['url'])

    # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(str(h[0]))

    # for h in reversed(hits): webbrowser.open(str(h['url']))
    # print('For more results, see %s' % data['cursor']['moreResultsUrl'])

    # print(d)


showsome(search_phrase)
