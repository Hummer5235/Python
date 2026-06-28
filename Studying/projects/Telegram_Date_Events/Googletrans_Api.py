from googletrans import Translator

translator = Translator()


def get_translate(text):
    text = translator.translate(text, dest='ru').text
    return text
