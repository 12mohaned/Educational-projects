import urllib.request
import urllib.parse
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
