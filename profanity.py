#import os
import urllib.request
import urllib.parse
"""url = "https://www.google.com"
values = {'q':'python programming tutorials'}
data = urllib.parse.urlencode(values)
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
resp_data = resp.read()
print(data)
open_file = open("/Users/mohanedmashaly/Desktop/python projects/movie_quotes/movie_quotes.txt")
reader = open_file.read()
for i in reader :
    print(reader)"""

"""try :
    x = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=ass")
    print(x.read())
except Exception as e :
    print(str(e))"""
"""try :
    url = "https://www.google.com/?"
    headers = {}
    headers['USer-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request(url,headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    saveFile = open('withHeaders.txt','w')
    saveFile.write(str(respData))
    saveFile.close()
except Exception as e :
    print(str(e))"""
open_file = open("/Users/mohanedmashaly/Desktop/python projects/movie_quotes/movie_quotes.txt")
reader = open_file.read()
y = reader.split()
for i in y:
    try :
        x = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+i)
        z = x.read()
        if z == b'true' :
            print("profanity alert ! " + i)
        else:
            print("no curse words till now")
    except Exception as e:
        print(str(e))
    
