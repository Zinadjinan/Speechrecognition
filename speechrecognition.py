import streamlit as st
import speech_recognition as sr

def transcribe_speech():
    r = sr.Recognizer()
    mic = sr.Microphone()

    st.write("Click the 'Start' button and speak into your microphone to transcribe speech.")
    st.write("You can pause and resume the transcription process using the buttons below.")

    paused = False
    text = ""

    with mic as source:
        while True:
            if st.button("Start"):
                st.write("Speak something...")
                audio = r.listen(source)

                if not paused:
                    try:
                        partial_text = r.recognize_google(audio)
                        text += partial_text
                        st.write("Transcription:")
                        st.write(text)
                    except sr.UnknownValueError:
                        st.error("Speech recognition could not understand audio.")
                    except sr.RequestError:
                        st.error("Unable to connect to the speech recognition service.")
                    except Exception as e:
                        st.error(f"An error occurred during speech recognition: {str(e)}")

            if st.button("Pause/Resume"):
                paused = not paused
                if paused:
                    st.warning("Transcription paused.")
                else:
                    st.info("Transcription resumed.")

            if st.button("Save Transcription"):
                save_transcription(text)
                st.success("Transcription saved successfully.")
                break




def save_transcription(text):
    filename = st.text_input("Enter a filename:", value="transcription.txt")
    with open(filename, "w") as file:
        file.write(text)

def get_language_code(language):
    language_codes = {"English": "en-US", "Spanish": "es-ES", "French": "fr-FR"}
    return language_codes.get(language, "en-US")

def main():
    st.title("Speech Recognition App")
    st.write("Click the button and speak into your microphone to transcribe speech.")

    if st.button("Transcribe"):
        transcribe_speech()

if __name__ == "__main__":
    main()