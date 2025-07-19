# 🤖 Jarvis Voice Assistant

A complete voice assistant system combining Speech-to-Text (STT) and Text-to-Speech (TTS) capabilities, inspired by the Jarvis AI from Iron Man.

## ✅ **Features**

### **Speech-to-Text (STT)**
- **Whisper STT**: High-accuracy speech recognition using OpenAI Whisper
- **Wake Word Detection**: Responds to "Jarvis" or "Hey Jarvis"
- **Voice Activity Detection**: Smart silence detection with adaptive thresholds
- **Background Noise Adaptation**: Automatically adjusts to ambient sound levels
- **Real-time Processing**: Continuous listening with callback-based processing

### **Text-to-Speech (TTS)** 
- **pyttsx3 Engine**: Reliable cross-platform TTS
- **British Voice**: Uses Daniel voice for authentic Jarvis experience
- **Personality Enhancement**: Adds formal "sir" addressing and contextual responses
- **Direct Speech**: Optimized for immediate audio output

### **Voice Commands**
- `"Jarvis"` - Wake word activation
- `"Hello/Hi"` - Greeting with time-appropriate response
- `"What time is it?"` - Current time
- `"What's the date?"` - Current date
- `"How are you?/Status"` - System status check
- `"Test"` - Test voice response
- `"Stop listening"` - Deactivate (say "Jarvis" to reactivate)
- `"Goodbye/Bye"` - Farewell
- `"Shutdown"` - Exit assistant

## 🚀 **Quick Start**

### **1. Run Complete Voice Assistant**
```bash
python jarvis_assistant.py
```

### **2. Demo Mode**
```bash
python demo_jarvis.py
# Choose option 1 for TTS-only demo
# Choose option 2 for full voice interaction
```

### **3. Live Transcription (STT Testing)**
```bash
python force_transcribe_test.py
```

### **4. Original STT Testing** 
```bash
python test_stt.py
```

## 📋 **System Requirements**

- **Python 3.8+**
- **Microphone access**
- **Audio output (speakers/headphones)**

### **Dependencies**
- `openai-whisper` - STT engine
- `pyttsx3` - TTS engine  
- `pyaudio` - Audio I/O
- `numpy` - Audio processing

## 🎯 **Usage Example**

1. **Start the assistant**: `python jarvis_assistant.py`
2. **Activate**: Say "Jarvis"
3. **Jarvis responds**: "Yes, sir. How may I assist you?"
4. **Give command**: "What time is it?"
5. **Jarvis responds**: "The current time is 5:30 PM, sir."

## 🔧 **Components**

### **Core Modules**
- `speech_analysis/stt.py` - Speech-to-text engine
- `speech_analysis/tts.py` - Text-to-speech engine  
- `jarvis_assistant.py` - Main voice assistant
- `demo_jarvis.py` - Demo and testing script

### **Testing Scripts**
- `force_transcribe_test.py` - Live transcription with logging
- `test_stt.py` - STT callback system testing

## 🎨 **Features Demonstrated**

### **✅ Working Systems**
1. **Real-time speech recognition** with Whisper
2. **Natural voice responses** with British accent
3. **Wake word detection** ("Jarvis")
4. **Conversational flow** with activation/deactivation
5. **Command processing** with multiple intents
6. **Adaptive silence detection** 
7. **Background noise handling**
8. **Professional voice personality**

### **🎭 Personality Features**
- Formal addressing ("sir")
- Time-appropriate greetings
- Contextual responses
- Polite error handling
- Professional tone

## 🔊 **Audio Configuration**

### **STT Settings**
- Sample rate: 16kHz
- Chunk size: 1024 samples
- Silence duration: 0.8 seconds
- Max recording: 10 seconds

### **TTS Settings**
- Voice: British English (Daniel)
- Speech rate: 180 WPM
- Volume: 90%

## 🧪 **Testing Results**

### **STT Performance**
- ✅ Speech detection working
- ✅ Silence detection working  
- ✅ Wake word detection working
- ✅ Transcription accuracy high
- ✅ Background noise adaptation working

### **TTS Performance**
- ✅ Voice synthesis working
- ✅ British accent selected
- ✅ Speech timing appropriate
- ✅ Direct audio output working

### **Integration**
- ✅ STT → TTS pipeline working
- ✅ Wake word → Response working
- ✅ Command → Action → Response working
- ✅ Conversation flow working

## 🎉 **Status: FULLY OPERATIONAL**

The Jarvis Voice Assistant is complete and functional with:
- ✅ Speech recognition
- ✅ Voice responses  
- ✅ Wake word activation
- ✅ Command processing
- ✅ Natural conversation flow
- ✅ Professional voice personality

Ready for use as a complete voice assistant system!
