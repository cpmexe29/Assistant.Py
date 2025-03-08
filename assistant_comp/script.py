import speech_recognition  # распознавание пользовательской речи (Speech-To-Text)
import pyttsx3  # синтез речи (Text-To-Speech)
import os  # работа с файловой системой
import webbrowser # работа с браузером

class VoiceAssistant:
    """
    Настройки голосового ассистента, включающие имя, пол, язык речи
    """
    name = ""
    sex = ""
    speech_language = ""
    recognition_language = ""

def setup_assistant_voice():
    """
    Установка голоса по умолчанию (индекс может меняться в
    зависимости от настроек операционной системы)
    """
    voices = ttsEngine.getProperty("voices")

    if assistant.speech_language == "en":
        assistant.recognition_language = "en-US"
        if assistant.sex == "female":
            # Microsoft Zira Desktop - English (United States)
            ttsEngine.setProperty("voice", voices[1].id)
        else:
            # Microsoft David Desktop - English (United States)
            ttsEngine.setProperty("voice", voices[2].id)
    else:
        assistant.recognition_language = "ru-RU"
        # Microsoft Irina Desktop - Russian
        ttsEngine.setProperty("voice", voices[0].id)


def play_voice_assistant_speech(text_to_speech):
    """
    Проигрывание речи ответов голосового ассистента (без сохранения аудио)
    :param text_to_speech: текст, который нужно преобразовать в речь
    """
    ttsEngine.say(str(text_to_speech))
    ttsEngine.runAndWait()


def record_and_recognize_audio(*args: tuple):
    """
    Запись и распознавание аудио
    """
    with microphone:
        recognized_data = ""

        # регулирование уровня окружающего шума
        recognizer.adjust_for_ambient_noise(microphone, duration=2)

        try:
            print("Listening...")
            audio = recognizer.listen(microphone, 5, 5)

            with open("microphone-results.wav", "wb") as file:
                file.write(audio.get_wav_data())

        except speech_recognition.WaitTimeoutError:
            print("Can you check if your microphone is on, please?")
            return

        # использование online-распознавания через Google
        # (высокое качество распознавания)
        try:
            print("Started recognition...")
            recognized_data = recognizer.recognize_google(audio, language="ru").lower()

        except speech_recognition.UnknownValueError:
            pass

        return recognized_data


def search_google(query):
    """
    Открывает браузер с результатами поиска в Google.
    :param query - поиск запрос
    """
    # Формируем URL для поиска в Google
    url = f"https://www.google.com/search?q={query}"

    # Открываем URL в браузере
    webbrowser.open(url)

    # Возвращаем ответ пользователю
    return f"Ищу информацию по запросу: {query}"

def goodbye():
    """
    Прощание и завершение работы программы.
    """
    play_voice_assistant_speech("До свидания! Удачи!")
    exit()  # завершение программы


def shutdown_pc():
    """
    Выключает компьютер.
    """
    os.system("shutdown /s /t 10")

def restart_pc():
    """
    Перезагружает компьютер.
    """
    os.system("shutdown /r /t 10")  # /r — перезагрузка, /t 0 — задержка 0 секунд

def search_youtube(query):
    """
    Открывает браузер с результатами поиска в YouTube.
    :param query - поиск запрос
    """
    # Формируем URL для поиска в Google
    url = f"https://www.youtube.com/results?search_query={query}"

    # Открываем URL в браузере
    webbrowser.open(url)

    # Возвращаем ответ пользователю
    return f"Ищу информацию по запросу: {query}"



if __name__ == "__main__":
    # инициализация инструментов распознавания и ввода речи
    recognizer = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()

    # инициализация инструмента синтеза речи
    ttsEngine = pyttsx3.init()

    # настройка данных голосового помощника
    assistant = VoiceAssistant()
    assistant.name = "Alice"
    assistant.sex = "female"
    assistant.speech_language = "ru"

    # установка голоса по умолчанию
    setup_assistant_voice()

    while True:
        # старт записи речи
        voice_input = record_and_recognize_audio()

        # проверка, что voice_input не равен None
        if voice_input:
            os.remove("microphone-results.wav")  # удаление временного файла
            print("Вы сказали:", voice_input)

            # обработка команды
            voice_input = voice_input.split(" ")
            command = voice_input[0]  # берём первое слово как команду

            if command == "привет":
                play_voice_assistant_speech("Здравствуй")
            elif command in ["пока", "стоп", "выход"]:
                goodbye()  # завершение работы программы
            elif command == "выключи" and "компьютер" in voice_input:
                play_voice_assistant_speech("Выключаю компьютер.")
                shutdown_pc()
            elif command == "найди":
                # Извлекаем поисковый запрос (всё, что после команды "найди")
                query = " ".join(voice_input[1:])
                play_voice_assistant_speech(search_google(query))
            elif command == "видео":
                # Извлекаем поисковый запрос (всё, что после команды "видео")
                query = " ".join(voice_input[2:])
                play_voice_assistant_speech(search_youtube(query))
            else:
                play_voice_assistant_speech("Я не поняла команду. Попробуйте ещё раз.")
        else:
            print("Не удалось распознать речь. Пожалуйста, повторите.")