from googletrans import Translator
from langdetect import detect
from textblob import TextBlob

def main(text):
    text = text.lower()
    if "]:" in text:# because we work with akuma, and he translate psedos from discord
        text = text.split("]:")[1]# I have a problem like this [bleu]: ¯\_(ツ)_/¯


    sameletter = text.count(text[0]) == len(text)# if somewone say hhh he will not translate

    if text[0] == " ": # if the first character is a space
        text = text[1:] # them remoove it
# I nee to remoove the space to check if the translation is identical as the text
        
    test_list = ['q(≧▽≦q)', '¯\_(ツ)_/¯','ω',"Σ","д","Д","yo","rz","thx :D","kek"," bish "," np"]# To see if it's an emoji
    emoji = [ele for ele in test_list if(ele in text)]# he don't have to disable the translator for this, I should remoove the emoji and add it again
    

    lang = detect(text)
    b = TextBlob(text)
    textblob = b.detect_language()
    if lang != "en" and textblob!= "en" and bool(emoji)!=1 and bool(sameletter)!=1 : # I use 2 detectors, if one of them is "en" I don't translate, I also don't translate emoji. We heve too much weebs 
        translator = Translator()
        result = translator.translate(text, dest='en').text# I pick the translated text 
        if result != text: # If the translated word is not the same as the original
            print(result+":"+text)
            return result

if __name__ == "__main__":
    main(text)
