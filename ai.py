import google.generativeai as genai



# def help_gemini():
# Replace with your API key
genai.configure(api_key="AIzaSyDvyFvmt_o3fxUDi0IZmEuGJMcRZpstwMo")

# Use a valid model from your list
model = genai.GenerativeModel('models/gemini-1.5-pro-latest')

# Ask something
response = model.generate_content("Tell me a joke.")

print(response.text)
