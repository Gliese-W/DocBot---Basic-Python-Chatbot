from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)


#DocBot

def get_response(user_input):

  print("Hi, I'm your personal Chatbot Doctor - DocBot")

  if not user_input:
    return "No input received"
  
  # while True:
    # user_input = input("You: ").lower()
  user_input = user_input.lower()

  if user_input == "bye":
    return "DocBot: Goodbye! Have a great day!"

  elif "hello" in user_input or "hi" in user_input:
    return "DocBot: Hi! How can I help you?"

  elif "how are you" in user_input:
    return "DocBot: I'm good. What about you?"

  elif "your name" in user_input:
    return "DocBot: My name is DocBot - Your personal doctor chatbot. How can I help you?"

  elif "help" in user_input:
    return "DocBot: Yes, I'm with you. Try saying something."

  elif "fever" in user_input:
    return "DocBot: Take small doses of paracetamol and rest well. Consult a doctor if still not well."

  elif "skincare" in user_input:
    return "DocBot: Use skin products like sunscreen, moisturizer, toner, etc."

  elif "bleeding" in user_input:
    return "DocBot: Calm down. Clean it and use bandage first." 

  elif "depression" in user_input:
    return "DocBot: Try talking with someone or book a therapy session."

  elif "appointment" in user_input:
    return "DocBot: Call on 9084414943 to book an appointment."

  elif "ambulance" in user_input:
    return "DocBot: Call on 108 to call an ambulance."

  elif "dying" in user_input:
    return "DocBot: Consult a doctor on an urgent basis."

  elif "haircare" in user_input:
    return "DocBot: Use haircare products like shampoo and conditioner."
      
  elif "stomachache" in user_input:
    return "DocBot: Take medicines and don't eat for a while."

  elif "motion sickness" in user_input:
    return "DocBot: Drink less water and sleep if you can."

  elif "advice" in user_input:
    return "DocBot: Okay.. What type of advice you want?"

  elif "haircare" in user_input:
    return "DocBot: Use haircare products like shampoo and conditioner."
      
  elif "stomachache" in user_input:
    return "DocBot: Take medicines and don't eat for a while."

  elif "motion sickness" in user_input:
    return "DocBot: Drink less water and sleep if you can."

  elif "advice" in user_input:
    return "DocBot: Drink something warm."

  elif "vomit" in user_input:
    return "DocBot: Stay hydrated and avoid solid food."

  elif "body pain" in user_input:
    return "DocBot: Take sufficient rest and press warm water dipped cloth on muscles."

  elif "diet" in user_input:
    return "DocBot: Maintain a healthy consisting of enough carbs, protien and fats with other necessary minerals."

  elif "sleep" in user_input:
    return "DocBot: Take proper sleep of 7-8 hours everyday to stay healthy."

  elif "anxiety" in user_input:
    return "DocBot: Try talking with yourself in a mirror and slowly interact with others."
  
  elif "thank you" in user_input:
    return "Thanks! Have a great day!"

  else:
    return "DocBot: Sorry, I don't understand. Try saying something else."

#running the Docbot

# docbot()

@app.route("/")
def home():
  return send_from_directory('.', 'templates/index.html')

@app.route("/chat", methods=["POST"])
# def chat():
#     return jsonify({"response": "Backend working"})

def chat():
  data = request.json
  user_message = data.get("message")
  response = get_response(user_message)
  return jsonify({"response":response})




if __name__ == "__main__":
  print("Chatbot is running! Visit http://127.0.0.1:5000 in your browser")
  print("Serving templates/index.html file")
  app.run(debug = True)