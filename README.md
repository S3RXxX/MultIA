# MultIA

Trying to create a multimodal AI using models/tools already trained/created which fit in my GPU (4060 8GB + 4 (RAM)).

## Overview

MultIA aims to leverage pre-trained models and tools to create a multimodal AI that can handle various tasks such as language understanding, transcription, and text-to-speech synthesis. The project utilizes the following components:

- **Llama 3 Instruct 8B** for the Large Language Model (LLM)
- **Whisper** for transcription
- **MMS** for text-to-speech (TTS)

## Components

### Llama 3 Instruct 8B
Llama 3 Instruct 8B is used as the core large language model to handle natural language understanding and generation tasks. It provides powerful capabilities to interact with users through natural language.

### Whisper
Whisper is used for audio transcription. It converts spoken language into text, enabling the AI to process and understand verbal input effectively.

### MMS (Multimodal Speech)
MMS is employed for text-to-speech synthesis. It converts text into spoken language, allowing the AI to communicate with users in a natural and fluent manner.

## Hardware Requirements

- GPU: NVIDIA RTX 4060 8GB or superior

## Installation

To install the required dependencies and set up the project, follow these steps:

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/MultIA.git
   cd MultIA
   ```
2. Install PyTorch:
   For CUDA drivers 12.1:
 ```sh
   pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
   ```
3. Install other dependencies:
   ```sh
   pip install -r requirements.txt
   ```
## Usage
 ```sh
py src/...
```
## Contribution
<!-- Contributors -->
* [**Sergi Guimerà Roig**](https://github.com/S3RXxX)

## License
IDK yet ...

## Contact
For any inquiries or feedback, please reach out to sergiguimeraroig@gmail.com.
