import speech_recognition as sr
import json


def record_sentence():
    r = sr.Recognizer()
    m = sr.Microphone()

    try:
        with m as source:
            r.adjust_for_ambient_noise(source)
        with m as source:
            audio = r.listen(source)
        try:
            value = r.recognize_google(audio)
            return value
        except sr.UnknownValueError:
            return "Error"
        except sr.RequestError as e:
            return "Google Speech Recognition Service Down"
    except:
        pass

    return value


def process_sentence():

    classes = None
    with open('classes.json') as json_file:
        classes = json.load(json_file)

    sentence = record_sentence()
    sentence = sentence.split()
    keywords = []
    for word in sentence:
        for key in classes.keys():
            if word in classes[key]:
                keywords.append(word)
                continue

    keywords = list(set(keywords))
    return keywords

keywords = process_sentence()
print(keywords)