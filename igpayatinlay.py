#pig latin:
#for each word that starts with a consonant
#move consonant to the end
#add "ay"
#if word starts with a vowel
#add "way" to the end
#dont change words like "or", "the", "on", etc


exemptwords = ['or', 'the', 'in', 'on', 'at', 'is', 'and', 'a', 'i']
vowel = "aeiouAEIOU"

#print(vowel)
englishwords = input("""Welcome to the PIG LATIN encoder
Please provide a message to translate.
""")

englishwords1 = englishwords.split(" ")

#print(englishwords1)

translation = ""
for i in englishwords1:
    if i in exemptwords:
        translation += i+' '
    elif i[0] in vowel:
        translation += i+"way "
    else:
        i += i[0].lower()
        i = i[1:]
        #i.replace(i[0], '')
        translation += i+"ay "

print(translation)
