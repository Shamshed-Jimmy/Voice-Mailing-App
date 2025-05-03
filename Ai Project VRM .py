import speech_recognition as sr
import yagmail

recognizer = sr.Recognizer()
with sr.Microphone() as source:
    print('Clearing Background Noise...')
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Wating for Your Massage...")
    recordedaudio = recognizer.listen(source)
    print('Done recording...!')
    try:
        print('Printing the massage...')
        text = recognizer.recognize_google(
            recordedaudio, language='en=US')
        print('Your Massage:{}'.format(text))

    except Exception as ex:
        print(ex)
    # This is a comment

# automaited mails:

reciever = 'shamjimmy72@gmail.com'
massage = text
sender = yagmail.SMTP('jimmyshamshed@gmail.com')
sender.send(to=reciever, subject='This is a automated mail', contents=massage)
