import urllib.request

url = 'https://shared-comic.pstatic.net/thumb/webtoon/626907/thumbnail/title_thumbnail_20150407141027_t83x90.jpg'
filename = 'p293_urldownload.jpg'

result = urllib.request.urlopen(url)


data =  result.read()

print("#type: " + str(type(data)))
with open(filename, 'wb') as f:
    f.write(data)

print(filename + ' saved')