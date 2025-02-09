import os
import re
from flask import Flask, render_template, request
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from the .env file
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)


def fetch_joke(theme, language, model):
    """
    Fetch a joke based on the given theme, language, and selected model using Groq's chat completions API.

    Args:
        theme (str): The theme for the joke.
        language (str): The language code ('en' for English, 'pt' for Portuguese).
        model (str): The selected language model to use.

    Returns:
        str: The cleaned joke text, or an error message if something goes wrong.
    """
    # Retrieve the API key from the environment variable
    api_key = os.environ.get("GROQ_API_KEY")

    # Create a Groq client instance using the API key
    client = Groq(api_key=api_key)

    # Define messages based on the language selection
    if language == "pt":
        system_message = "Você é um gerador de piadas amigável."
        user_message = f"Conte-me uma piada sobre {theme}"
    else:
        system_message = "You are a friendly joke generator."
        user_message = f"Tell me a joke about {theme}"

    try:
        # Request a chat completion (joke) from Groq's API using the selected model
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_message}
            ],
            model=model  # Use the model selected by the user
        )

        # Extract the raw joke text from the API response
        joke = chat_completion.choices[0].message.content

        # Remove any text between <think> and </think> tags (and any trailing whitespace)
        cleaned_joke = re.sub(r'<think>.*?</think>\s*', '', joke, flags=re.DOTALL)
        return cleaned_joke.strip()

    except Exception as e:
        # Return an error message (could be enhanced with logging)
        return f"Error fetching joke: {e}"


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route for displaying the joke form and processing form submissions.
    GET: Render the input form.
    POST: Process the form, fetch a joke, and display the result.
    """
    if request.method == 'POST':
        # Retrieve the LLM model, language, and theme from the submitted form
        model = request.form.get('model', 'deepseek-r1-distill-llama-70b')
        language = request.form.get('language', 'en')  # Default to English if not specified
        theme = request.form.get('theme', '').strip()

        # Validate that the theme is not empty
        if not theme:
            error_message = "Theme cannot be empty." if language == 'en' else "O tema não pode ser vazio."
            return render_template('index.html', error=error_message)

        # Fetch a joke using the provided theme, language, and selected model
        joke = fetch_joke(theme, language, model)
        return render_template('result.html', joke=joke, language=language)

    # For GET requests, simply render the form
    return render_template('index.html')


if __name__ == '__main__':
    # Run the app in debug mode for development; remove debug=True in production
    app.run(debug=True, port=5001)
