# YouTube Transcript Fetcher

A Python program to retrieve the text transcript of YouTube videos. This tool uses the [`youtube_transcript_api`](https://github.com/jdepoix/youtube-transcript-api) library to fetch available transcripts (both manually provided and auto-generated) for a given YouTube video URL.

## Table of Contents

- [Prerequisites](#prerequisites)
  - [1. Python Installation](#1-python-installation)
  - [2. Install Required Python Packages](#2-install-required-python-packages)
  - [3. (Optional) Handling Non-English Transcripts](#3-optional-handling-non-english-transcripts)
- [Python Script: Retrieve YouTube Video Transcript](#python-script-retrieve-youtube-video-transcript)
- [How to Use the Program](#how-to-use-the-program)
  - [Clone the repository](#clone-the-repository)
  - [Install Dependencies](#install-dependencies)
  - [Run the Script](#run-the-script)
- [Examples](#examples)
  - [Fetch English Transcript (Default)](#fetch-english-transcript-default)
  - [Specify Output Filename and Language](#specify-output-filename-and-language)
  - [Fetching a Non-English Transcript](#fetching-a-non-english-transcript)
- [Handling Errors and Exceptions](#handling-errors-and-exceptions)
  - [No Transcript Available](#no-transcript-available)
  - [Transcripts Disabled](#transcripts-disabled)
  - [Invalid URL](#invalid-url)
- [Additional Notes](#additional-notes)
  - [Multiple Transcripts](#multiple-transcripts)
  - [Auto-Generated vs. Manually Provided Transcripts](#auto-generated-vs-manually-provided-transcripts)
  - [Handling Long Videos](#handling-long-videos)
  - [Privacy and Respecting YouTube's Terms of Service](#privacy-and-respecting-youtubes-terms-of-service)
- [Contributions](#contributions)

## Prerequisites

### 1. Python Installation

Ensure you have **Python 3.6** or later installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### 2. Install Required Python Packages

Open your terminal or command prompt and install the necessary packages using `pip`:

pip install youtube_transcript_api pytube

### 3. (Optional) Handling Non-English Transcripts

If you need transcripts in languages other than English, ensure that the video has transcripts available in those languages. The script can be adjusted to fetch transcripts in specific languages.



## How to Use the Program

### Clone the repository
`git clone https://github.com/ChristianE00/Youtube-Transcript-Fetcher.git`

### Install Dependencies

`pip install youtube_transcript_api pytube`


### Run the Script
Open your terminal or command prompt, navigate to the directory containing youtube_transcript_fetcher.py, and execute the script using the following syntax:

```powershell
python youtube_transcript_fetcher.py "YOUTUBE_VIDEO_URL" -o "output_filename.txt" -l "language_code"
```
- `"YOUTUBE_VIDEO_URL"`: Replace with the actual URL of the YouTube video.
- `"output_filename.txt"`: (Optional) Replace with your desired output filename. Defaults to transcript.txt if not specified.
- `"language_code"`: (Optional) Replace with the desired language code (e.g., 'en' for English, 'es' for Spanish). Defaults to 'en' if not specified.
## Examples

### Fetch English Transcript (Default) 
```powershell
python youtube_transcript_fetcher.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
```
__Description__: This command fetches the English transcript of the provided video and saves it to `transcript.txt`.


### Specify Output Filename and Language
```powershell
python youtube_transcript_fetcher.py "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -o "rickroll_transcript.txt" -l "en"

```
__Description__: This fetches the English transcript and saves it to `rickroll_transcript.txt`.

### Fetching a Non-English Transcript

__Description__: This command fetches the Spanish transcript of the specified video and saves it to `transcript_es.txt`.

## Handling Errors and Exceptions

### No Transcript Available
- __Scenario__: If a transcript isn't available in the specified language, the script will attempt to fetch the English transcript. If no transcript is found, it will notify you accordingly.
### Transcripts Disabled
- __Scenario__: If transcripts are disabled for the video, the script will inform you that transcripts are disabled.

### Invalid URL
- __Scenario__: If the provided URL is invalid or the video ID cannot be extracted, the script will display an error message.

## Additional Notes

### Multiple Transcripts
- __Description__: Some YouTube videos have multiple transcripts in different languages or both auto-generated and manually provided captions. The script lists all available transcripts before attempting to fetch the desired one. This helps you choose the correct language code.
### Auto-Generated vs. Manually Provided Transcripts
- __Description__: Auto-generated transcripts might be less accurate compared to manually provided ones. This is indicated in the transcript listing output.
### Handling Long Videos
- __Description__: The youtube_transcript_api handles relatively long transcripts efficiently. However, if you encounter issues with exceptionally long videos, consider modifying the script to process segments or use more advanced transcript retrieval methods.
### Privacy and Respecting YouTube's Terms of Service
- __Description__: Ensure that you have the right to access and use the transcripts, especially for copyrighted content. Always respect YouTube's Terms of Service when accessing and using their data.
## Contributions
__Feel free to contribute!__ If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

