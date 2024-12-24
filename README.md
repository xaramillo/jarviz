# jarviz-stt - Speech-to-Text Integration with OpenAI

This project implements an application to convert audio to text, send questions to the OpenAI API, and receive spoken answers. It also includes a Docker environment for easy deployment and an interactive Jupyter Notebook.

## Features
- Speech-to-Text conversion using SpeechRecognition.
- Interaction with OpenAI's API for intelligent responses.
- Text-to-Speech conversion using pyttsx3.
- Python implementation with support for Docker and notebooks.

## Requirements
- Python 3.9+
- Docker (optional, for containerized deployment)
- OpenAI API Key

## Manual Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/xaramillo/jarviz.git
   cd jarviz
   ```

2. Install local dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure the OpenAI API key:
   Add your `OPENAI_API_KEY` in a `.env` file.

## Usage
### Local
Run the main script:
```bash
python main.py
```

### Docker
1. Build the image:
   ```bash
   docker build -t jarviz-stt .
   ```

2. Run the container:
   ```bash
   docker run --rm -it jarviz-stt
   ```

### Jupyter Notebook
Run the interactive notebook:
```bash
jupyter notebook notebooks/stt_openai.ipynb
```

## License