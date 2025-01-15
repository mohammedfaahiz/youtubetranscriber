import sys
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

def get_video_id(url):
    """Extract the video ID from a YouTube URL."""
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1]
    else:
        raise ValueError("Invalid YouTube URL")

def fetch_transcript(video_url):
    """Fetch the transcript of a YouTube video."""
    try:
        video_id = get_video_id(video_url)
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Format the transcript into readable text
        formatter = TextFormatter()
        transcript_text = formatter.format_transcript(transcript)
        return transcript_text
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        video_url = sys.argv[1]
        transcript = fetch_transcript(video_url)
        print(transcript)
    else:
        print("Error: No URL provided.")
