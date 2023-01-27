from slovar_rusoanglisko_slova import words

def eng():
    ewords=dict([[v, k] for k,v in words.items()])
    x=input('Enter word: ')
    ans='No such word'
    for i, e in ewords.items():
        if i==x:
            ans=e
    print(ans)

def rus():
    #words=dict([[v, k] for k,v in words.items()])
    x=input('Enter word: ')
    ans='No such word'
    for i, e in words.items():
        if i==x:
            ans=e
    print(ans)
while True:
    x=input('Translate to Rus or Eng???    ')
    if x=='Eng':
        eng()
    elif x=='Rus':
        rus()
    else :
        print('I did not understand, type "Eng" or "Rus", please')
            
    
    
