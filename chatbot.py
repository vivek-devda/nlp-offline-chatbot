import json
import re
from fuzzywuzzy import fuzz
# This function compares user input with known phrases
# using fuzzy string matching and returns the closest match.
from pypdf import PdfReader

#load responses
def load_responses(file="responses.json"):
    try:
        with open(file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: responses.json file not found.")
        return {}

# extract txt from pdf
def extract_pdf_text(path):
  reader = PdfReader(path)
  text = ""
  for page in reader.pages:
    page_text = page.extract_text()
    if page_text:
      text += page_text + "\n"
  return text

#clean text
def preprocess(text):
  text = text.lower()
  text = re.sub(r'[^\w\s]','',text)
  return text

#find response
def get_response(user_input, responses):
  best_match = None
  best_score = 0

  for key in responses:
  score = fuzz.ratio(user_input, key)
  if score > best_score:
    best_Score = score
    best_match = key

if best_score > 60:
  return responses[best_match]
else:
  return "sorry, i dont understand."

#chat loop
def chatbot():
  responses = load_responses()
  print("chatbot is ready! type 'exit' to quit.\n")

   while True:
       user_input = input("you: ").lower()
       if not user_input.strip():
           print("Bot: Please enter something.")
           continue
           if user_input == "exit":
               print("Bot: Goodbye!")
               break

user_input = preprocess(user_input)
reply = get_response(user_input,responses)
print("Bot:",reply)

#run chatbot
if __name__ == "__main__":
  chatbot()
  
