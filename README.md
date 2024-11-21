
# **Weather Assistant Chatbot**

## **Overview**
The Weather Assistant Chatbot is a Python-based conversational assistant that provides real-time weather information. It interacts with users via the command line, answering weather-related queries like current conditions, forecasts, and advice for specific cities.

---

## **Features**
1. **Real-Time Weather Updates**: Get the current temperature, weather conditions, and other details for any city worldwide.
2. **Weather Forecast**: Provide short-term forecasts (optional—if included in your project).
3. **Friendly Advice**: Suggest clothing or items based on weather conditions (e.g., "Take an umbrella!" for rain).
4. **Interactive Chat**: Respond to user queries in natural language.

---

## **Tech Stack**
- **Programming Language**: Python
- **Weather API**: [OpenWeatherMap](https://openweathermap.org/)
- **Libraries Used**:
  - `requests`: For making HTTP requests to the weather API.
  - (Optional) `nltk` or `spaCy`: For natural language processing.
  - `json`: For parsing API responses.

---

## **Setup Instructions**

### **1. Clone the Repository**
   ```bash
   git clone https://github.com/your-username/weather-assistant-chatbot.git
   cd weather-assistant-chatbot
   ```

### **2. Install Dependencies**
   Make sure Python 3.x is installed. Then install the required libraries:
   ```bash
   pip install requests
   ```

### **3. Get an API Key**
   - Go to [OpenWeatherMap](https://openweathermap.org/) and sign up for an account.
   - Generate an API key from the dashboard.

### **4. Configure the API Key**
   - Open the `weather_bot.py` file.
   - Replace `"your_api_key"` with your actual API key:
     ```python
     api_key = "your_api_key"
     ```

---

## **Usage Instructions**

1. **Run the Chatbot**  
   Execute the Python script in your terminal:
   ```bash
   python weather_bot.py
   ```

2. **Interact with the Bot**  
   - **Example Queries**:
     - "What's the weather in Paris?"
     - "Will it rain in Tokyo today?"
     - "How's the weather in New York?"
   - To exit, type:
     ```text
     bye, exit, or quit
     ```

3. **Example Interaction**:
   ```
   You: What's the weather in London?
   Bot: The current temperature in London is 8°C with light rain.
   You: Will it rain in Tokyo today?
   Bot: No, it's expected to stay dry in Tokyo.
   You: bye
   Bot: Goodbye! Stay safe!
   ```

## **Future Enhancements**
1. **Forecast Feature**: Extend functionality to provide multi-day weather forecasts.
2. **GUI Version**: Use `Tkinter` or `Flask` to build a graphical interface.
3. **Voice Assistant**: Enable voice interaction using libraries like `speech_recognition` or `pyttsx3`.
4. **Geolocation**: Detect user location automatically to provide local weather updates.

---

## **Contributing**
If you'd like to contribute:
1. Fork the repository.
2. Create a new branch:  
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push to the branch:  
   ```bash
   git push origin feature-name
   ```
4. Submit a pull request.

---

## **License**
This project is licensed under the Apache License. See the `LICENSE` file for details.
