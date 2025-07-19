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
    
    # Test various responses with new centralized commands
    demo_interactions = [
        ("Wake word activation", lambda: assistant.on_wake_word_detected()),
        ("Greeting", lambda: assistant.commands.process_command("hello jarvis")),
        ("Time request", lambda: assistant.commands.process_command("what time is it")),
        ("Date request", lambda: assistant.commands.process_command("what's the date")),
        ("System status", lambda: assistant.commands.process_command("how are you")),
        ("Battery check", lambda: assistant.commands.process_command("battery")),
        ("Tell a joke", lambda: assistant.commands.process_command("tell me a joke")),
        ("Introduction", lambda: assistant.commands.process_command("who are you")),
        ("Help command", lambda: assistant.commands.process_command("help")),
        ("Goodbye", lambda: assistant.commands.process_command("goodbye"))
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
