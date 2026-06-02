import google.generativeai as genai

# Configure with your API key
genai.configure(api_key="YOUR_API_KEY")  # Replace with your actual API key

print("Available models:\n")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(f"✅ {model.name}")