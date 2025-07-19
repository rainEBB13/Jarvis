#!/usr/bin/env python3

import time
import datetime
import threading
import logging
from speech_analysis import JarvisSTT, JarvisTTS

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class JarvisAssistant:
    """Complete Jarvis Voice Assistant with STT and TTS"""
    
    def __init__(self):
        self.stt = JarvisSTT(stt_engine="whisper", model_name="base")
        self.tts = JarvisTTS(tts_engine="system")
        self.is_active = False
        self.is_listening = False
        
        # Set up STT callbacks
        self.stt.set_speech_callback(self.on_speech_received)
        self.stt.set_wake_word_callback(self.on_wake_word_detected)
        
        # Simple command processing
        self.commands = {
            "time": self.tell_time,
            "date": self.tell_date, 
            "hello": self.greet,
            "hi": self.greet,
            "goodbye": self.goodbye,
            "bye": self.goodbye,
            "how are you": self.status_check,
            "status": self.status_check,
            "test": self.test_response,
            "stop listening": self.stop_listening,
            "shutdown": self.shutdown
        }
        
        logger.info("Jarvis Assistant initialized")
    
    def on_wake_word_detected(self):
        """Handle wake word detection"""
        logger.info("🚨 Wake word detected!")
        self.is_active = True
        self.tts.speak_direct("Yes, sir. How may I assist you?")
    
    def on_speech_received(self, text):
        """Handle speech input"""
        logger.info(f"📝 Speech received: '{text}'")
        
        if self.is_active or "jarvis" in text.lower():
            self.process_command(text)
        else:
            logger.info("Jarvis is not active - say 'Jarvis' to activate")
    
    def process_command(self, text):
        """Process voice commands"""
        text_lower = text.lower()
        
        # Check for exact command matches
        for command, handler in self.commands.items():
            if command in text_lower:
                logger.info(f"🎯 Executing command: {command}")
                handler(text)
                return
        
        # Default response for unrecognized commands
        self.handle_unknown_command(text)
    
    def tell_time(self, text):
        """Tell current time"""
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}, sir."
        self.tts.speak_direct(response)
    
    def tell_date(self, text):
        """Tell current date"""
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        response = f"Today is {current_date}, sir."
        self.tts.speak_direct(response)
    
    def greet(self, text):
        """Handle greetings"""
        current_hour = datetime.datetime.now().hour
        if current_hour < 12:
            greeting = "Good morning"
        elif current_hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
        
        response = f"{greeting}, sir. How may I assist you today?"
        self.tts.speak_direct(response)
    
    def goodbye(self, text):
        """Handle goodbye"""
        self.tts.speak_direct("Until next time, sir. Have a pleasant day.")
        self.is_active = False
    
    def status_check(self, text):
        """System status check"""
        response = "All systems are functioning normally, sir. I am ready to assist you."
        self.tts.speak_direct(response)
    
    def test_response(self, text):
        """Test response"""
        responses = [
            "Test successful. All systems operational, sir.",
            "Voice recognition and synthesis are working perfectly, sir.",
            "I hear you loud and clear, sir."
        ]
        import random
        self.tts.speak_direct(random.choice(responses))
    
    def stop_listening(self, text):
        """Stop listening temporarily"""
        self.tts.speak_direct("Stopping voice recognition, sir. Say my name to reactivate.")
        self.is_active = False
    
    def shutdown(self, text):
        """Shutdown the assistant"""
        self.tts.speak_direct("Shutting down. Until next time, sir.")
        self.is_listening = False
        self.is_active = False
    
    def handle_unknown_command(self, text):
        """Handle unrecognized commands"""
        responses = [
            "I'm not sure I understand that request, sir. Could you please rephrase?",
            "I don't have that capability at the moment, sir. How else may I assist you?",
            "I'm afraid I don't comprehend that command, sir. Please try again.",
            "Could you please clarify what you'd like me to do, sir?"
        ]
        import random
        self.tts.speak_direct(random.choice(responses))
    
    def start(self):
        """Start the voice assistant"""
        print("🤖 Starting Jarvis Voice Assistant...")
        print("=" * 60)
        print("🎙️  Say 'Jarvis' to activate")
        print("📢 Available commands:")
        print("   • 'time' - Get current time")
        print("   • 'date' - Get current date") 
        print("   • 'hello/hi' - Greeting")
        print("   • 'how are you/status' - System status")
        print("   • 'test' - Test response")
        print("   • 'stop listening' - Deactivate")
        print("   • 'goodbye/bye' - Farewell") 
        print("   • 'shutdown' - Exit assistant")
        print("⏹️  Press Ctrl+C to stop")
        print("=" * 60)
        
        # Start with greeting
        self.tts.speak_direct("Good day, sir. Jarvis voice assistant is now online. Say my name to begin.")
        
        # Start listening
        self.is_listening = True
        self.stt.start_listening()
        
        try:
            while self.is_listening:
                time.sleep(0.5)
                
        except KeyboardInterrupt:
            print("\n\n⏹️  Shutting down...")
        finally:
            self.stop()
    
    def stop(self):
        """Stop the voice assistant"""
        self.is_listening = False
        self.stt.stop_listening()
        print("✨ Jarvis Assistant stopped.")

def main():
    """Main entry point"""
    assistant = JarvisAssistant()
    assistant.start()

if __name__ == "__main__":
    main()
