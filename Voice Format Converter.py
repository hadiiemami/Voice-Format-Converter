"""
audio_converter.py

A general-purpose script to batch convert audio files from one format
to another using ffmpeg-python.
"""

import os
import ffmpeg

# Define the input folder containing audio files
INPUT_FOLDER = r"Define Your Path"

# Define the output folder for converted files
OUTPUT_FOLDER = os.path.join(INPUT_FOLDER, "Converted_Audio")

# Define target output format (e.g., "mp3", "wav", "flac", "ogg")
TARGET_FORMAT = "mp3"

# Create the output folder if it does not exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def convert_audio(input_file: str, output_file: str):
    """
    Convert a single audio file to the desired format.
    The codec will be selected automatically by ffmpeg 
    based on the output format.
    """
    (
        ffmpeg
        .input(input_file)
        .output(output_file, format=TARGET_FORMAT)
        .run(overwrite_output=True, quiet=True)
    )

def batch_convert():
    """
    Loop through all files in the input folder and convert 
    them to the specified target format.
    """
    for file_name in os.listdir(INPUT_FOLDER):
        # Skip hidden files or folders
        if file_name.startswith("."):
            continue

        input_path = os.path.join(INPUT_FOLDER, file_name)

        # Skip if it's not a file
        if not os.path.isfile(input_path):
            continue

        # Extract extension and name
        base, ext = os.path.splitext(file_name)

        # Skip if already in target format
        if ext.lower() == f".{TARGET_FORMAT}":
            continue

        # Define output file name
        output_file = os.path.join(OUTPUT_FOLDER, f"{base}.{TARGET_FORMAT}")

        try:
            convert_audio(input_path, output_file)
            print(f"[OK] Converted: {file_name} -> {os.path.basename(output_file)}")
        except Exception as e:
            print(f"[ERROR] Failed to convert {file_name}: {e}")

    print("All audio files converted successfully.")

if __name__ == "__main__":
    batch_convert()
