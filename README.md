# AI Joke Generator

A Flask web application that generates jokes using various Large Language Models (LLMs) through the Groq API. Users can select their preferred language model, choose between English and Portuguese languages, and specify a theme for the joke.

## Features

- Multiple LLM model selection (llama-3.3-70b-versatile, deepseek-r1-distill-llama-70b, gemma2-9b-it, mixtral-8x7b-32768)
- Bilingual support (English and Portuguese)
- Theme-based joke generation
- Mobile-responsive interface
- Clean and user-friendly UI using Bootstrap

## Prerequisites

- Python 3.x
- Groq API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ai-joke-generator.git
cd ai-joke-generator
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your Groq API key:
```
GROQ_API_KEY=your_api_key_here
```

## Usage

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5001
```

3. Select your preferred:
   - Language model
   - Language (English or Portuguese)
   - Enter a theme for the joke

4. Click "Generate Joke" to get your customized joke

## Deployment

The application includes Gunicorn in its dependencies for production deployment. You can deploy it to platforms like Heroku, DigitalOcean, or any other Python-compatible hosting service.

## Project Structure

```
├── templates/
│   ├── index.html      # Main page with joke generation form
│   └── result.html     # Page displaying the generated joke
├── .gitignore         # Git ignore file
├── app.py            # Main Flask application
├── LICENSE           # MIT License
├── README.md         # Project documentation
└── requirements.txt  # Python dependencies
```

## Dependencies

- Flask: Web framework
- Groq: API client for LLM interactions
- python-dotenv: Environment variable management
- gunicorn: Production WSGI server
- Additional dependencies listed in `requirements.txt`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Acknowledgments

- Built with Flask framework
- Styled with Bootstrap
- Powered by Groq API and various LLM models

---

Made with ❤️ by [Augusto Souza](https://github.com/augustosouza8) and with assistance from ChatGPT ([click here to access the main used chat](https://chatgpt.com/share/67a8c84e-8f74-8013-bcbb-1b86a71aa7ae)) 