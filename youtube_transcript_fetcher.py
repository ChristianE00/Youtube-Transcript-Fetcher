import argparse
import sys
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound, CouldNotRetrieveTranscript
from pytube import YouTube
from urllib.parse import urlparse, parse_qs

def get_video_id(url):
    """
    Extract the video ID from a YouTube URL.

    Args:
        url (str): The full YouTube video URL.

    Returns:
        str: The extracted video ID.

    Raises:
        ValueError: If the URL is invalid or video ID cannot be extracted.
    """
    parsed_url = urlparse(url)
    if parsed_url.hostname in ['youtu.be']:
        return parsed_url.path[1:]
    elif parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
        if parsed_url.path == '/watch':
            query_params = parse_qs(parsed_url.query)
            return query_params.get('v', [None])[0]
        elif parsed_url.path.startswith('/embed/'):
            return parsed_url.path.split('/')[2]
        elif parsed_url.path.startswith('/v/'):
            return parsed_url.path.split('/')[2]
    raise ValueError("Invalid YouTube URL or unable to extract video ID.")

def fetch_transcript(video_id, language='en'):
    """
    Fetch the transcript for a YouTube video.

    Args:
        video_id (str): The YouTube video ID.
        language (str): The language code for the transcript (default is 'en').

    Returns:
        list: A list of transcript segments.

    Raises:
        Exception: If transcript cannot be retrieved.
    """
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=[language, 'en'])
        return transcript
    except TranscriptsDisabled:
        raise Exception("Transcripts are disabled for this video.")
    except NoTranscriptFound:
        raise Exception("No transcript found for this video.")
    except CouldNotRetrieveTranscript:
        raise Exception("Could not retrieve transcript. It might be unavailable or restricted.")
    except Exception as e:
        raise Exception(f"An error occurred while fetching transcript: {str(e)}")

def save_transcript(transcript, output_file):
    """
    Save the transcript to a text file.

    Args:
        transcript (list): The transcript segments.
        output_file (str): The path to the output text file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for segment in transcript:
            f.write(segment['text'] + ' ')
    print(f"Transcript successfully saved to '{output_file}'.")

def list_available_transcripts(video_id):
    """
    List all available transcripts for a YouTube video.

    Args:
        video_id (str): The YouTube video ID.

    Returns:
        list: A list of available transcript dictionaries.
    """
    transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
    available = []
    for transcript in transcripts:
        available.append({
            'language': transcript.language,
            'language_code': transcript.language_code,
            'is_generated': transcript.is_generated
        })
    return available

def main():
    parser = argparse.ArgumentParser(description="Retrieve the transcript of a YouTube video.")
    parser.add_argument('url', help='URL of the YouTube video')
    parser.add_argument('-o', '--output', default='transcript.txt', help='Output text file name')
    parser.add_argument('-l', '--language', default='en', help='Language code of the transcript (default: en)')

    args = parser.parse_args()

    try:
        video_id = get_video_id(args.url)
    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)

    # Optional: List available transcripts
    try:
        available_transcripts = list_available_transcripts(video_id)
        if not available_transcripts:
            print("No transcripts available for this video.")
            sys.exit(1)
        print("Available Transcripts:")
        for idx, t in enumerate(available_transcripts, start=1):
            gen_status = "Auto-Generated" if t['is_generated'] else "Manually Provided"
            print(f"{idx}. Language: {t['language']} ({t['language_code']}) - {gen_status}")
    except Exception as e:
        print(f"Error fetching available transcripts: {str(e)}")
        sys.exit(1)

    # Fetch transcript
    try:
        transcript = fetch_transcript(video_id, language=args.language)
        save_transcript(transcript, args.output)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
