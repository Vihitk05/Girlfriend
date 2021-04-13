import pyttsx3
import PyPDF2
import datetime


def read_book():
    book = open('CN Unit1.pdf', 'rb')
    pdf_reader = PyPDF2.PdfFileReader(book)
    pages = pdf_reader.getNumPages()
    print(pages)
    engine = pyttsx3.init()
    for count in range(0, pages):
        page = pdf_reader.getPage(1)
        text = page.extractText()
        engine.say(text)
        engine.runAndWait()


def greet():
    engine = pyttsx3.init()
    time = int(datetime.datetime.now().hour)
    if 6 <= time <= 12:
        print('Good Morning! My Love!')
        engine.say('Good Morning! My Love!')
        engine.runAndWait()
    elif 12 <= time <= 18:
        print('Good Afternoon! My Love!')
        engine.say('Good Afternoon! My Love!')
        engine.runAndWait()
    elif 18 <= time <= 22:
        print('Good Evening!My Love!')
        engine.say('Good Evening!My Love!')
        engine.runAndWait()
    else:
        print('Good Night! My Love!')
        engine.say('Good Night! My Love!')
        engine.runAndWait()
