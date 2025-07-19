#!/usr/bin/env python3

import time
from jarvis_assistant import JarvisAssistant

def demo_voice_responses():
    """Demo the TTS responses without STT"""
    print("🎭 Jarvis TTS Demo - Testing Voice Responses")
    print("=" * 50)
    print("🔊 Make sure your audio is on - you should hear Jarvis speak!")
    print()
    
    assistant = JarvisAssistant()
    
    # Test various responses
    demo_interactions = [
        ("Wake word activation", lambda: assistant.on_wake_word_detected()),
        ("Greeting", lambda: assistant.greet("hello jarvis")),
        ("Time request", lambda: assistant.tell_time("what time is it")),
        ("Date request", lambda: assistant.tell_date("what's the date")),
        ("Status check", lambda: assistant.status_check("how are you")),
        ("Test command", lambda: assistant.test_response("test")),
        ("Unknown command", lambda: assistant.handle_unknown_command("play music")),
        ("Goodbye", lambda: assistant.goodbye("goodbye"))
    ]
    
    for description, action in demo_interactions:
        print(f"\n🎯 Testing: {description}")
        time.sleep(1)
        action()
        time.sleep(2)  # Wait for speech to complete
    
    print("\n✨ TTS Demo completed!")

def demo_full_interaction():
    """Demo with brief voice interaction"""
    print("\n🎙️ Brief Voice Interaction Test")
    print("=" * 50)
    print("Say 'Jarvis' to activate, then try commands like:")
    print("  - 'Hello Jarvis'")
    print("  - 'What time is it?'") 
    print("  - 'Test'")
    print("  - 'Goodbye'")
    print("This will run for 30 seconds...")
    print()
    
    assistant = JarvisAssistant()
    
    # Run for 30 seconds
    start_time = time.time()
    assistant.stt.start_listening()
    assistant.is_listening = True
    
    try:
        while time.time() - start_time < 30:
            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    finally:
        assistant.stop()
    
    print("✅ Voice interaction test completed!")

if __name__ == "__main__":
    print("🤖 Jarvis Voice Assistant Demo")
    print("=" * 60)
    
    choice = input("Choose demo:\n1. TTS responses only\n2. Full voice interaction (30s)\nEnter 1 or 2: ")
    
    if choice == "1":
        demo_voice_responses()
    elif choice == "2":
        demo_full_interaction()
    else:
        print("Invalid choice. Running TTS demo...")
        demo_voice_responses()
    
    print("\n🎉 Demo finished!")
