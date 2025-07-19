#!/usr/bin/env python3
"""
Force Transcribe - Simple audio file transcription utility
Only prints the transcribed text without any additional processing.
"""

import sys
import os
from speech_analysis.stt import JarvisSTT


def main():
    if len(sys.argv) != 2:
        print("Usage: python force_transcribe.py <audio_file>", file=sys.stderr)
        print("Supported formats: WAV files", file=sys.stderr)
        sys.exit(1)
    
    audio_file = sys.argv[1]
    
    # Check if file exists
    if not os.path.exists(audio_file):
        print(f"Error: File '{audio_file}' not found", file=sys.stderr)
        sys.exit(1)
    
    # Initialize STT with Whisper (more accurate for file transcription)
    try:
        stt = JarvisSTT(stt_engine="whisper", model_name="base")
    except Exception as e:
        print(f"Error initializing STT engine: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Transcribe the file
    try:
        transcription = stt.transcribe_file(audio_file)
        
        # Only print the transcribed text (no additional output)
        if transcription:
            print(transcription)
        else:
            # If no transcription, exit silently (no output)
            pass
            
    except Exception as e:
        print(f"Error transcribing file: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
