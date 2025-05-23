import whisper
from whisper.utils import get_writer
from utils import app_config 
import os

class TranscriptionService:
    def __init__(self, model_name=None):
        self.model_name = model_name if model_name else app_config.WHISPER_MODEL_NAME
        self.model = None

    def load_model(self):
        """
        Loads the Whisper model. Returns True on success, False on failure.
        This can be time-consuming and should be called appropriately (e.g., in a thread).
        """
        if self.model:
            print(f"Model '{self.model_name}' already loaded.")
            return True
        try:
            print(f"Loading Whisper model '{self.model_name}'...")
            self.model = whisper.load_model(self.model_name)
            print(f"Whisper model '{self.model_name}' loaded successfully.")
            return True
        except Exception as e:
            print(f"Error loading Whisper model '{self.model_name}': {e}")
            self.model = None
            return False

    def transcribe_audio(self, audio_file_path):
        """
        Transcribes the given audio file.
        This should run in a separate thread to avoid freezing the UI.
        Returns a result dictionary or a dictionary with an "error" key.
        """
        if not self.model:
            print("Transcription service: Model not loaded.")
            return {"error": app_config.MESSAGE_MODEL_LOAD_ERROR, "text": "", "segments": []}
        
        print(f"Starting transcription for: {audio_file_path}")
        try:
            result = self.model.transcribe(audio_file_path, verbose=False)
            print(f"Transcription successful for: {audio_file_path}")
            return result # a dict with "text", "segments", "language"
        except Exception as e:
            print(f"Error during transcription for '{audio_file_path}': {e}")
            return {"error": f"{app_config.MESSAGE_TRANSCRIPTION_ERROR} Details: {str(e)}", "text": "", "segments": []}

    def generate_srt(self, result_data, audio_file_for_srt_context, output_directory):
        """
        Generates an SRT file from the transcription result.
        'audio_file_for_srt_context' is typically the original audio filename, used by the writer.
        'output_directory' is where the SRT file will be saved. The writer names the file based on audio_file_for_srt_context.
        """
        if "error" in result_data and not result_data.get("segments"):
            print(f"SRT Generation: Cannot generate SRT due to error: {result_data.get('error')}")
            return False
        if not result_data.get("segments"):
            print("SRT Generation: No segments found in result data.")
            return False

        try:
            srt_writer = get_writer("srt", output_directory)
            srt_writer(result_data, audio_file_for_srt_context)
            
            base_audio_filename = os.path.basename(audio_file_for_srt_context)
            srt_filename = os.path.splitext(base_audio_filename)[0] + ".srt"
            full_srt_path = os.path.join(output_directory, srt_filename)
            print(f"SRT file generated successfully: {full_srt_path}")
            return True
        except Exception as e:
            print(f"Error generating SRT for '{audio_file_for_srt_context}': {e}")
            return False