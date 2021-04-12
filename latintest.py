str = 'ạ ị ư'
print(str)
encoded = str.encode('utf-8')

print(encoded)

a = encoded.decode('cp1252')
print(a)

#encoded = str.encode('euc-kr')
#print(encoded)


#cp1258

#참고사이트
#https://guzene.tistory.com/150
#https://docs.python.org/2.4/lib/standard-encodings.html
#https://utf8-chartable.de/unicode-utf8-table.pl?start=7808&number=128&names=-&utf8=string-literal

#https://docs.python.org/ko/3.8/howto/unicode.html