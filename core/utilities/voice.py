class Voice:

    def __init__(self, enabled=False):
        self.enabled = enabled
        self._recognizer = None
        self._micClass = None

        if self.enabled:
            try:
                import pyttsx3
                import speech_recognition as sr
                self._recognizer = sr.Recognizer()
                self._micClass = sr.Microphone
            except Exception as error:
                print(f"[Voice] Could not start voice mode ({error}). Continuing with text only.")
                self.enabled = False

    def speak(self, text):
        print(text)
        if self.enabled:
            try:
                import pyttsx3
                engine = pyttsx3.init()
                engine.say(text)
                engine.runAndWait()
                engine.stop()
            except Exception:
                pass

    def listen(self, prompt):
        if not self.enabled:
            return input(prompt).strip()

        self.speak(prompt)
        try:
            import speech_recognition as sr
            with self._micClass() as source:
                self._recognizer.adjust_for_ambient_noise(source, duration=0.3)
                print("(listening...)")
                audio = self._recognizer.listen(source, timeout=5, phrase_time_limit=5)
            heard = self._recognizer.recognize_google(audio)
            print(f'You said: "{heard}"')
            return heard.strip()
        except Exception:
            return input("I didn't catch that, please type it: ").strip()

    def askTyped(self, prompt):
        return input(prompt).strip()
