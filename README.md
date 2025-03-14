# Build with AI Starter Kit 🚀

Welcome to the Build with AI Starter Kit! Whether you're a beginner taking your first steps into AI development or an experienced developer looking to kickstart your next AI project, you're in the right place. This open-source starter kit provides everything you need to create powerful AI-powered applications using Python and Streamlit.

We've designed this kit to be both approachable and extensible, allowing you to start simple and scale up as your needs grow. Let's build something amazing together! 

## 🌟 Features

- Ready-to-use AI application template powered by Google's Gemini AI
- Multiple example personalities (News Reporter, Poet, Pirate, Conspiracy Theorist)
- Built-in tools for news fetching and more
- Clean project structure for easy expansion
- Streamlit-based web interface for beautiful UI without frontend expertise
- Comprehensive utility functions for AI interaction and data parsing

## 🛠️ Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- A Google API key (for certain functionalities)

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/asengupta07/build-with-ai-starter-kit
   cd build-with-ai-starter-kit
   ```

2. **Set up a virtual environment (optional, but recommended)**
   ```bash
   python -m venv venv
   # On Windows
   .\venv\Scripts\activate
   # On Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   - Copy `.env.example` to `.env`
   ```bash
   cp .env.example .env
   ```
   - Get your Google API key:
     1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
     2. Sign in with your Google account if you haven't already
     3. Click on "Get API key" in the left menu
     4. Click "Create API key"
     5. Copy the generated API key. **Important:** Save this key securely as it will only be shown once
     
   - Add your Google API key to the `.env` file:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

   **Important Security Notes:**
   - Never commit your API key to version control
   - Keep your API key secure and don't share it with others
   - For production applications, consider using environment variables or a secure secrets manager

5. **Run the application**
   ```bash
   streamlit run Home.py
   ```

## 📁 Project Structure

```
build-with-ai-starter-kit/
├── Home.py                # Main Streamlit application
├── examples/              # Example AI personalities
│   ├── news.py           # News reporter personality
│   ├── poet.py           # Poet personality
│   ├── pirate.py         # Pirate personality
│   └── conspiracy.py      # Conspiracy theorist personality
├── tools/                 # Utility tools
├── utils/                 # Helper functions
├── pages/                 # Additional Streamlit pages
├── assets/               # Static assets
├── requirements.txt      # Python dependencies
└── .env.example          # Example environment secrets file
```

## 🔧 Technical Details

### Utility Functions (`utils/`)

Our utility functions are designed to make AI interaction and data handling as smooth as possible:

1. **Generate Module** (`utils/generate.py`)
   ```python
   def generate(prompt: str) -> str
   ```
   - Core function for interacting with Google's Gemini AI model
   - Handles prompt-based text generation
   - Automatically manages API configuration and response handling
   
   ```python
   def analyse_image(image: Image.Image, prompt: str) -> str
   ```
   - Enables image analysis using Gemini's multimodal capabilities
   - Accepts PIL Image objects and text prompts
   - Perfect for building image-understanding applications

2. **Parse Module** (`utils/parse.py`)
   ```python
   def parse_json(response: str) -> dict
   ```
   - Robust JSON parsing with markdown code block handling
   - Automatically cleans response text from AI models
   - Handles common JSON formatting variations
   - Essential for structured data exchange with AI models

### Tools (`tools/`)

The tools directory contains specialized modules for specific functionalities:

1. **News Tool** (`tools/news.py`)
   ```python
   def get_news(query: str) -> str
   ```
   - Real-time news fetching using Google News RSS feeds
   - Smart query processing with regex-based cleanup
   - Returns formatted news items with titles and links
   - Configurable number of results (currently set to top 3)

## 🎯 Examples

The project includes several example AI personalities that demonstrate different capabilities:

1. **News Reporter** (`examples/news.py`)
   - Provides news summaries and updates
   - Uses news API integration
   - Example: "What's happening with Tesla stock?"

2. **Poet** (`examples/poet.py`)
   - Generates creative poetry
   - Example: "Write a poem about sunset"

3. **Pirate** (`examples/pirate.py`)
   - Responds in pirate-speak
   - Example: "Tell me about treasure hunting"

4. **Conspiracy Theorist** (`examples/conspiracy.py`)
   - Generates humorous conspiracy theories
   - Example: "What's the truth about Area 51?"

## 💬 Using the Chat & Image Analysis Pages

### Chat Interface

To use different AI personalities in the chat interface, you need to modify the chat page code directly:

1. **Locate the Chat Page File**
   - Navigate to the `pages` directory
   - Find the chat interface file (e.g., `pages/01_Chat.py`)

2. **Import Desired Personality**
   ```python
   # In pages/01_Chat.py
   
   # Comment out or replace the default generate import
   # from utils.generate import generate
   
   # Import the personality you want to use
   from examples.pirate import generate as pirate_generate
   from examples.poet import generate as poet_generate
   from examples.news import generate as news_generate
   
   # Use the imported generate function
   response = pirate_generate(prompt)  # For pirate responses
   # or
   response = poet_generate(prompt)    # For poetic responses
   # or
   response = news_generate(prompt)    # For news responses
   ```

### Image Analysis

Similarly, for image analysis, you need to modify the image analysis page code:

1. **Locate the Image Analysis Page File**
   - Find the image analysis file (e.g., `pages/02_Image_Analysis.py`)

2. **Import Custom Image Analysis**
   ```python
   # In pages/02_Image_Analysis.py
   
   # Comment out or replace the default analyse_image import
   # from utils.generate import analyse_image
   
   # Import your custom image analyzer
   from examples.pirate import analyse_image as pirate_analyse_image
   from examples.poet import analyse_image as poet_analyse_image
   
   # Use the imported function
   response = pirate_analyse_image(image, prompt)  # For pirate responses
   # or
   response = poet_analyse_image(image, prompt)    # For poetic responses
   ```

### Creating Your Own Personality

To create a new AI personality:

1. Create a new Python file in the `examples` directory
2. Implement the required functions.
3. Use the utility functions from `utils/` for common operations:
   - `utils.generate.generate()` for AI text generation
   - `utils.generate.analyse_image()` for image analysis
   - `utils.parse.parse_json()` for structured data handling
4. Add any necessary tools in the `tools/` directory
5. Import your personality/agent in Chat/Image Analysis page, plug it in and enjoy!

When creating a new personality, ensure it follows the same interface as the examples:

```python
# examples/my_custom_personality.py

def generate(prompt: str) -> str:
    """
    Required: Main generation function
    """
    # Your custom logic here
    return "AI Response"

def analyse_image(prompt: str, image: Image.Image = None) -> str:
    """
    Required: Main image analysis function
    """
    # Your custom logic here
    return "AI Image Analysis Response"
```

### Plugging in Your Personality

1. **For Chat Interface**
   ```python
   # In pages/01_Chat.py
   from examples.my_custom_personality import generate
   
   # Use it directly
   response = generate(user_input)
   ```

2. **For Image Analysis**
   ```python
   # In pages/02_Image_Analysis.py
   from examples.my_custom_personality import analyse_image
   
   # Use it with image
   response = analyse_image(prompt, uploaded_image)
   ```

### Tips for Implementation

1. **Consistent Interface**
   - Always implement the `generate()` function
   - Keep the function signature compatible with the interface
   - Handle both text and image inputs appropriately

2. **Error Handling**
   ```python
   def generate(prompt: str, image: Image.Image = None) -> str:
       try:
           # Your implementation
           return response
       except Exception as e:
           return f"Error in personality: {str(e)}"
   ```

3. **Testing Your Integration**
   - Test with various inputs
   - Ensure proper error handling
   - Verify image handling if applicable


## 🚀 Development Best Practices

1. **Error Handling**: Always try to wrap AI interactions in try-except blocks
2. **Rate Limiting**: Be mindful of API rate limits in production
3. **Testing**: Add test cases for your personalities
4. **Documentation**: Comment your code and update this README
5. **Environment Variables**: Never commit API keys

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🆘 Troubleshooting

Common issues and solutions:

1. **ModuleNotFoundError**: Make sure you've installed all dependencies using `pip install -r requirements.txt`
2. **API Key Error**: Verify that your `.env` file exists and contains the correct API key
3. **Streamlit Issues**: Ensure you're running the latest version of Streamlit

## 📚 Additional Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Documentation](https://docs.python.org/)
- [Google API Documentation](https://developers.google.com/)