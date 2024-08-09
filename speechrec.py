import pyautogui
import speech_recognition

rec=speech_recognition.Recognizer()
mic=speech_recognition.Microphone()

with mic as source:
    print('listening')
    rec.adjust_for_ambient_noise(source)
    audio=rec.listen(source)
try:
    if("yeah" in rec.recognize_google(audio) or "woo" in rec.recognize_google(audio) or "woohoo" in rec.recognize_google(audio) or "ya" in rec.recognize_google(audio)):
        print('Excitement Recognized')
        pyautogui.press('num9')

    print(' You just said: '+rec.recognize_google(audio))
except speech_recognition.UnknownValueError:
    print('Could not recognize')
except speech_recognition.RequestError as e:
    print('Error'.format(e))
