# Chat with AI using Flask and Ollama (Locally)

This project is a simple chat application that utilizes Flask for the web server and the Ollama library for AI model interaction. The chat interface allows users to send messages and receive responses from the AI model, and it supports markdown formatting in the AI responses.

## Features

- User messages are right-aligned and in blue.
- AI responses are left-aligned and in grey.
- AI responses support markdown formatting.
- Typing indicator is shown while waiting for the AI response.
- Clear conversation button to reset the chat history.

## Requirements

- Python 3.7+
- pip
- ollama3.1

## Setup and Installation

1. **Install Ollama**

You must first download the ollama source from here: https://github.com/ollama/ollama/tree/main to get started. To trial out and download the llama3 model, after ollama is installed, run the following

> ollama run llama3.1

Once you have the model downloaded you can easily refer back to it in your code.

2. **Clone the repository:**

    ```bash
    git clone https://github.com/kwalker430/llama3-chatbot.git
    cd llama3-chatbot
    ```

3. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the application:**

    ```bash
    flask run
    ```

    The application will be available at `http://127.0.0.1:5000`.

## Usage

- Open your browser and navigate to `http://127.0.0.1:5000`.
- Type a message in the input box and press Enter or click the "Send" button.
- The AI response will appear below your message.
- Use the "Clear Conversation" button to reset the chat history.

## Sample Interactions

**User**: Why is the sky blue?  
**AI**: The sky is blue due to Rayleigh scattering.

**User**: How is that different from Mie scattering?  
**AI**: Rayleigh scattering occurs when the particles causing the scattering are smaller than the wavelength of light. Mie scattering occurs when the particles are about the same size as the wavelength of light.

## Project Structure
llama3-chatbot/
│
├── app.py # Main Flask application
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # HTML template for the chat interface
└── README.md # This README file

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Disclaimer

This README file was generated with AI but has been reviewed and modified for readability.
