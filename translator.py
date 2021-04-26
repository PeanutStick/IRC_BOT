from googletrans import Translator
def main(text):
    translator = Translator()
    result = translator.translate(text, dest='en')
    return result
if __name__ == "__main__":
    main(text)
