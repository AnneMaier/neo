#!/usr/bin/env python

import threading, requests, time


class HtmlGettrer(threading.Thread):
    def __init__ (self, url):
        threading.Thread.__init__(self)
        self.url = url
    def run(self):
        resp = requests.get(self.url)
        time.sleep(1)
        print(self.url, len(resp.text), 'chars')

t = HtmlGettrer('http://google.com')
t.start()
print("### End ###")