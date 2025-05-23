# --- Appearance ---
APP_NAME = "transcription-w1"
DEFAULT_APPEARANCE_MODE = "Dark"
DEFAULT_COLOR_THEME = "dark-blue"

# --- Colors ---
COLOR_BUTTON = "#2e5b84"
COLOR_BUTTON_HOVER = "#283d61"
COLOR_BUTTON_TEXT = "white"

# --- File Handling ---
SUPPORTED_AUDIO_FORMATS_DESCRIPTION = "Audio Files"
SUPPORTED_AUDIO_EXTENSIONS_LIST = ["*.m4a", "*.mp3", "*.webm", "*.mp4", "*.mpga", "*.wav", "*.mpeg"]
SUPPORTED_AUDIO_TYPES_TUPLE = (
    SUPPORTED_AUDIO_FORMATS_DESCRIPTION, 
    " ".join(SUPPORTED_AUDIO_EXTENSIONS_LIST)
)
ALL_FILES_TUPLE = ("All Files", "*.*")

FILE_DIALOG_AUDIO_TYPES = [
    SUPPORTED_AUDIO_TYPES_TUPLE,
    ALL_FILES_TUPLE
]

# --- UI Text & Labels ---
# Home View
LABEL_AUDIO_FILE = ""
BUTTON_TEXT_SUBMIT = "Submit"
BUTTON_TEXT_DOWNLOAD_SRT = "Download as SRT file"

# Top Nav
TAB_HOME = "Home"
TAB_GUIDE = "Guide"

# --- Guide Content ---
GUIDE_TITLE = "How to Use"
GUIDE_TEXT = f"""
Welcome to {APP_NAME}!

Follow these simple steps to transcribe your audio:

1.  Upload Audio File:
    *   Click the upload button.
    *   Select an audio file from your computer.
    *   Supported formats: {', '.join([ext.replace('*.','') for ext in SUPPORTED_AUDIO_EXTENSIONS_LIST])}.

2.  Submit for Transcription:
    *   Click the "{BUTTON_TEXT_SUBMIT}" button.
    *   A spinner will indicate that the transcription is in progress. Please wait.
    *   The buttons will be disabled during this process.

3.  View and Download:ß
    *   Once complete, the transcribed text will appear in the main area.
    *   The "{BUTTON_TEXT_DOWNLOAD_SRT}" button will become active.
    *   Click it to save the transcription as an .srt file.

Notes:
*   Ensure your audio quality is clear for best results.
*   The transcription process happens locally on your computer.
"""

# --- Transcription ---
WHISPER_MODEL_NAME = "resource/large-v3-turbo.pt"

# --- Messages ---
MESSAGE_MODEL_LOADING = "Loading transcription model, please wait..."
MESSAGE_MODEL_LOAD_ERROR = "Error: Could not load transcription model."
MESSAGE_TRANSCRIPTION_ERROR = "Error during transcription. Please try again or check the audio file."
MESSAGE_FILE_INVALID_TYPE = "Error: Invalid file type selected. Please choose a supported audio file."
MESSAGE_SRT_SAVE_SUCCESS = "SRT file saved successfully."
MESSAGE_SRT_SAVE_ERROR = "Error: Could not save SRT file."
MESSAGE_NO_AUDIO_SELECTED = "Please select an audio file first."
MESSAGE_NO_TRANSCRIPTION_AVAILABLE = "No transcription available to download."
