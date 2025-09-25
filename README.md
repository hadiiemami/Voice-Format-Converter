# Audio Converter

A simple Python tool for batch converting audio files between different formats 
(M4A, MP3, WAV, FLAC, OGG, etc.) using [ffmpeg-python](https://github.com/kkroening/ffmpeg-python).

---

## Features
- Batch convert all audio files in a folder.
- Supports many formats (input and output), e.g. `.m4a`, `.mp3`, `.wav`, `.flac`, `.ogg`.
- Automatically skips files already in the target format.
- Easy to configure input/output paths and target format.

---

## Requirements

- Python 3.8+
- Install required library:
```bash
pip install ffmpeg-python
```
- FFmpeg must be installed and added to your system PATH.  
  [Download FFmpeg](https://ffmpeg.org/download.html)

---

## Usage

1. Edit the script `audio_converter.py` and set your folder paths:

```python
INPUT_FOLDER = r"D:\Project\Aali Panah\9-25-2025\Voice"
OUTPUT_FOLDER = os.path.join(INPUT_FOLDER, "Converted_Audio")
TARGET_FORMAT = "mp3"   # Change this to "wav", "flac", "ogg", etc.
```

2. Run the script:

```bash
python audio_converter.py
```

3. All converted files will be saved in the `Converted_Audio` subfolder.

---

## Examples

- Convert everything to MP3:
```python
TARGET_FORMAT = "mp3"
```
- Convert everything to WAV:
```python
TARGET_FORMAT = "wav"
```
- Convert everything to FLAC:
```python
TARGET_FORMAT = "flac"
```

---

## Notes
- The script uses ffmpeg under the hood, so nearly any audio format can be converted.
- Conversion quality depends on the codec defaults used by ffmpeg.
- Tested on Windows with Python 3.10+.

---

## License
This project is licensed under the MIT License.
