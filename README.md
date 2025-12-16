# Simple Python AI Agent

A lightweight, extensible AI agent built with Python and the Google Gemini API. This agent runs in your terminal and demonstrates "agency" by using tools to perform actions like calculations, checking the time, retrieving system information, and fetching real-time weather data.

## Features

- **Conversational Intelligence**: Powered by Google's Gemini Pro / Flash models.
- **Tool Use**: The agent can autonomously decide when to use tools to answer queries.
- **Terminal Interface**: Simple, interactive CLI.
- **Extensible**: Easy to add new Python functions as tools.

## Included Tools

1.  **Calculator**: Safely evaluates mathematical expressions (e.g., "50 * 23").
2.  **Time**: Returns the current local date and time.
3.  **Weather**: Fetches real-time weather for any city using the Open-Meteo API (No API key required!).
4.  **System Info**: Reports the OS, platform, and Python version it's running on.
5.  **Random Number Generator**: Generates random integers (e.g., "Roll a d20").

## Prerequisites

- Python 3.9+
- A specific Google AI Studio API Key (Free tier available).

## Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/kisso-selvan/simple_agent.git
    cd simple_agent
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up authentication**:
    - Get a free API key from [Google AI Studio](https://aistudio.google.com/).
    - Create a `.env` file in the project root:
    ```bash
    touch .env
    ```
    - Add your key to the file:
    ```env
    GOOGLE_API_KEY=your_actual_api_key_here
    ```

## Usage

Run the agent:

```bash
python3 main.py
```

### Example Interactions

Once the agent is running, try these inputs:

-   **Chat**: "Hello, who are you?"
-   **Math**: "What is 15% of 85?" or "Solve (12 * 4) + 10"
-   **Time**: "What time is it now?"
-   **Weather**: "What is the weather like in Tokyo?" or "Is it raining in London?"
-   **System**: "What computer is this?"
-   **Random**: "Pick a number between 1 and 10."

## Project Structure

-   `main.py`: Entry point for the CLI application.
-   `agent.py`: Configures the Gemini model and registers tools.
-   `tools.py`: Contains the actual Python functions that the agent can call.
-   `requirements.txt`: Python package dependencies.
-   `list_models.py`: Utility script to check available Gemini models for your API key.

## Customization

To add a new tool:
1.  Define a python function in `tools.py` with a clear docstring (the agent reads this to understand what the tool does).
2.  Import the function in `agent.py`.
3.  Add it to the `self.tools` list in the `SimpleAgent` class.
