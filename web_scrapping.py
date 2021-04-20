from bs4 import BeautifulSoup
import requests
from googletrans import Translator

word = 'labile'

source = requests.get('https://mnemonicdictionary.com/?word=' + word).text

soup = BeautifulSoup(source, 'lxml')

meaning = soup.find('div', class_ = 'media-heading')
#print(meaning.prettify())

true_mean = meaning.find_next_sibling('div')
lst = true_mean.text.split()
definition = ""
for i in lst:
    #print(i)
    if i == 'Synonyms' or i == 'Example':
        break
    
    elif i == 'Definition':
        definition+=i
        definition+=" : "
    
    else:
        definition += i
        definition += ' '

print(definition)

print('\n\n\t\t\t\t\tMnemonics\n')

mnemonic_slide = soup.find('div', class_ = 'mnemonics-slides')
mnemonic_track = mnemonic_slide.find('div')
#mnemonic_active = mnemonic_track.find_all('div', class_ = 'slick-active')
mnemonic_div = mnemonic_track.find_all('div')
#print(mnemonic_div)
lst1 = []
for mnemonics in mnemonic_div:
    mnemonic = mnemonics.find('p')
    try:
        mnemonic = mnemonic.text
        mnemonic.rstrip()
        mnemonic.lstrip()
        lst1.append(mnemonic)
    
    except:
        pass

lst1 = list(dict.fromkeys(lst1))

for i in lst1:
    print(i)

translator = Translator(service_urls=[
    'translate.google.com',
])
marathi_word = translator.translate(word, dest='mr')
print(marathi_word)
