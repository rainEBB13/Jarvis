#!/usr/bin/env python3
"""
Live Transcribe - Real-time Speech-to-Text
==========================================

A simple script for continuous speech-to-text transcription using Jarvis STT.

Usage:
    python live_transcribe.py [options]

Options:
    --engine ENGINE     STT engine to use (whisper, google, azure, sphinx)
    --debug            Enable debug logging for audio processing
    --quiet            Suppress info messages, only show transcriptions
    --help             Show this help message

Controls:
    Ctrl+C             Stop transcription and exit
    
Example:
    python live_transcribe.py --engine whisper --debug
"""

import argparse
import sys
import signal
import time
from speech_analysis.stt import JarvisSTT

class LiveTranscriber:
    def __init__(self, stt_engine="whisper", debug=False, quiet=False):
        """Initialize the live transcriber with specified settings."""
        self.stt_engine = stt_engine
        self.debug = debug
        self.quiet = quiet
        self.running = False
        self.stt = None
        
        # Set up signal handler for graceful shutdown
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
    
    def _signal_handler(self, signum, frame):
        """Handle interrupt signals for graceful shutdown."""
        if not self.quiet:
            print("\n🛑 Stopping live transcription...")
        self.stop()
        sys.exit(0)
    
    def start(self):
        """Start the live transcription session."""
        if not self.quiet:
            print(f"🎤 Starting live transcription with {self.stt_engine} engine...")
            print("📝 Speak clearly into your microphone. Press Ctrl+C to stop.\n")
            print("-" * 60)
        
        try:
            # Initialize STT with debug settings
            self.stt = JarvisSTT(stt_engine=self.stt_engine, model_name="tiny.en", debug=self.debug)
            self.running = True
            
            session_count = 0
            
            while self.running:
                try:
                    if not self.quiet:
                        print(f"🔴 Listening... (session {session_count + 1})")
                    
                    # Listen for speech and transcribe
                    transcription = self.stt.listen_and_transcribe()
                    
                    if transcription and transcription.strip():
                        session_count += 1
                        timestamp = time.strftime("%H:%M:%S")
                        
                        if self.quiet:
                            # Quiet mode: just print the transcription
                            print(transcription.strip())
                        else:
                            # Normal mode: formatted output
                            print(f"📝 [{timestamp}] You said: {transcription.strip()}")
                            print("-" * 60)
                    else:
                        if not self.quiet:
                            print("🔇 No speech detected or transcription failed.")
                            print("-" * 60)
                    
                    # Small delay to prevent overwhelming the system
                    time.sleep(0.1)
                    
                except Exception as e:
                    if not self.quiet:
                        print(f"❌ Error during transcription: {e}")
                        print("🔄 Continuing...")
                        print("-" * 60)
                    
        except KeyboardInterrupt:
            self._signal_handler(signal.SIGINT, None)
        except Exception as e:
            print(f"❌ Failed to initialize STT engine '{self.stt_engine}': {e}")
            sys.exit(1)
    
    def stop(self):
        """Stop the live transcription."""
        self.running = False


def main():
    """Main function to parse arguments and start live transcription."""
    parser = argparse.ArgumentParser(
        description="Live speech-to-text transcription using Jarvis STT",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python live_transcribe.py                    # Use default whisper engine
    python live_transcribe.py --engine whisper   # Use Whisper Speech Recognition
    python live_transcribe.py --debug            # Enable audio debug logging
    python live_transcribe.py --quiet            # Only show transcriptions
    python live_transcribe.py --engine whisper --quiet > transcript.txt  # Save to file
        """
    )
    
    parser.add_argument(
        "--engine",
        choices=["whisper", "google", "azure", "sphinx"],
        default="whisper",
        help="STT engine to use (default: whisper)"
    )
    
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug logging for audio processing"
    )
    
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress info messages, only show transcriptions"
    )
    
    args = parser.parse_args()
    
    # Create and start the live transcriber
    transcriber = LiveTranscriber(
        stt_engine=args.engine,
        debug=args.debug,
        quiet=args.quiet
    )
    
    transcriber.start()


if __name__ == "__main__":
    main()
