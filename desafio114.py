from urllib import request

try:
    request.urlopen("https://www.facebook.com/")
except:
    print('Site insdisponivel no momento, tente mais tarde!')
else:
    print('Site Online')

