import pandas as pd

excelLnageName = []

language_name = {'re':'Re-Translate', 'en':'English', 'zh-CN':'Chinese', 'ja':'Japanese', 'es':'Spanish', 'fr':'French', 'de':'German', 'vi':'Vietnamese', 'id':'Indonesian', 'lo':'Lao', 'th':'Thai', 'ru':'Russian', 'pt':'Portuguese', 'zh-TW':'Taiwanese'}
arr = [(['a', 'b'], 0, 're'), (['c', 'd'], 1, 'ja'), (['e', 'f'], 2, 'vi')]
dataFrame_dict = {}

for i in arr:
    for key, val in language_name.items():
        if i[2] == key:
           excelLnageName.append(val)

print(excelLnageName)

for i in range(len(arr)):
    dataFrame_dict[excelLnageName[i]] = arr[i][0]

print(dataFrame_dict)

df = pd.DataFrame(dataFrame_dict)
df.to_excel('input_sentence.xlsx', sheet_name='new_name', index=False, header=True)

'''
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> for key in a:
...     print(key)
... 
alice
bob
tony
suzy
'''

'''>>> for val in a.values():
...     print(val)
... 
[1, 2, 3]
20
15
30   
'''

'''
dict = { 'one' : 1, 'two' : 2 }
dict['three'] = 3

출처: https://devinside.tistory.com/161 [개발개발개발]
'''