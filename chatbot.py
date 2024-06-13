import speech_recognition as sr
import pyttsx3

# Initialize the speech recognition and text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define the prompts the bot will use to ask for user input
prompts = {
    "name": "What is your name?",
    "source": "Where are you traveling from?",
    "destination": "Where are you traveling to?",
    "date": "When are you traveling?",
    "verify": "Please verify your details. Your name is {}, you are traveling from {} to {}, on {}."
}

# Define a function to speak a prompt and return the user's response
def get_input(prompt):
    engine.say(prompt)
    engine.runAndWait()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        input_text = r.recognize_google(audio)
        return input_text
    except sr.UnknownValueError:
        engine.say("I'm sorry, I didn't understand that. Please try again.")
        engine.runAndWait()
        return get_input(prompt)
    except sr.RequestError as e:
        engine.say("I'm sorry, there was an error with the speech recognition service. Please try again later.")
        engine.runAndWait()
        return None

# Define the main function to run the chatbot
def run_chatbot():
    input_fields = ["name", "source", "destination", "date"]
    user_inputs = {}
    for field in input_fields:
        user_input = get_input(prompts[field])
        engine.say(f"You said {user_input}. Is that correct?")
        engine.runAndWait()
        confirmation = get_input("Please say 'yes' or 'no'.")
        while confirmation.lower() not in ["yes", "no"]:
            engine.say("I'm sorry, I didn't understand that.")
            engine.runAndWait()
            confirmation = get_input("Please say 'yes' or 'no'.")
        if confirmation.lower() == "no":
            engine.say(f"Okay, let's try again. {prompts[field]}")
            engine.runAndWait()
            user_input = get_input(prompts[field])
            engine.say(f"You said {user_input}. Is that correct?")
            engine.runAndWait()
            confirmation = get_input("Please say 'yes' or 'no'.")
            while confirmation.lower() not in ["yes", "no"]:
                engine.say("I'm sorry, I didn't understand that.")
                engine.runAndWait()
                confirmation = get_input("Please say 'yes' or 'no'.")
        if confirmation.lower() == "yes":
            user_inputs[field] = user_input
    verify_prompt = prompts["verify"].format(user_inputs["name"], user_inputs["source"], user_inputs["destination"], user_inputs["date"])
    engine.say(verify_prompt)
    engine.runAndWait()
    confirmation = get_input("Please say 'yes' or 'no'.")
    while confirmation.lower() not in ["yes", "no"]:
        engine.say("I'm sorry, I didn't understand that.")
        engine.runAndWait()
        confirmation = get_input("Please say 'yes' or 'no'.")
    if confirmation.lower() == "yes":
        # Fill in the HTML form with the user's details and submit the form
        # Here, you will need to write the code to interact with your HTML form
        pass
    else:
        run_chatbot()

# Call the main function to start the chatbot
run_chatbot()

