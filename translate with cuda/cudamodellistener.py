from RealtimeSTT import AudioToTextRecorder
import multiprocessing
import time

def process_text(text):
    print(f"Transcribed: {text}")

def main():
    try:
        recorder = AudioToTextRecorder(
            wake_words="computer",         
            model="large-v2",              
            device="cuda"                  
        )
        print("Say 'computer' to start recording...")
        with recorder:
            while True:
                try:
                    recorder.text(process_text)
                except EOFError:
                    print("EOFError encountered. Restarting transcription...")
                    time.sleep(1)
                    continue

    except BrokenPipeError:
        print("BrokenPipeError encountered. Check the transcription process or connection.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        if 'recorder' in locals():
            recorder.shutdown()  

if __name__ == "__main__":
    multiprocessing.freeze_support()  

    main()  
