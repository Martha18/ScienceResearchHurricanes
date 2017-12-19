import threading
import time
##import urllib2

start = time.time()
urls = ["http://www.google.com", "http://www.apple.com"]

def fetch_url(url):
    urlHandler = urllib2.urlopen(url)
    html = urlHandler.read()
    print ("%s\' fetched in %ss" % (url, (time.time()- start)))

threads = [threading.Thread(target=fetch_url, args = (url, )) for url in urls]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print ("Elapsed Time:%s" % (time.time() - start))
