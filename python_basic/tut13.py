# # AI Interview Simulator - Base Prototype

# # import speech_recognition as sr
# # import pyttsx3
# # from transformers import pipeline

# # Initialize text-to-speech engine
# engine = pyttsx3.init()

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# # Initialize speech recognizer
# recognizer = sr.Recognizer()

# def listen():
#     with sr.Microphone() as source:
#         print("Listening...")
#         audio = recognizer.listen(source)
#         try:
#             text = recognizer.recognize_google(audio)
#             print("You said:", text)
#             return text
#         except:
#             print("Sorry, could not understand.")
#             return ""

# # Simple Q&A setup
# questions = [
#     {"question": "Tell me about yourself.", "type": "HR"},
#     {"question": "What is a binary search?", "type": "Technical"},
#     {"question": "Why should we hire you?", "type": "HR"},
# ]

# # Load zero-shot-classification pipeline to check answers
# classifier = pipeline("zero-shot-classification")

# def evaluate_answer(answer, question_type):
#     # Very basic evaluation
#     if question_type == "Technical":
#         labels = ["correct", "incorrect"]
#         result = classifier(answer, candidate_labels=labels)
#         score = 50 + 50 * result['scores'][0]  # simple weighted score
#     else:  # HR question
#         score = 50 + len(answer.split())  # simple proxy: longer answer = more points
#         if score > 100:
#             score = 100
#     return round(score, 2)

# def run_interview():
#     total_score = 0
#     for q in questions:
#         print("\nAI Interviewer:", q["question"])
#         speak(q["question"])
#         answer = listen()
#         score = evaluate_answer(answer, q["type"])
#         print(f"Score for this answer: {score}/100")
#         total_score += score

#     avg_score = round(total_score / len(questions), 2)
#     print("\n=== Interview Finished ===")
#     print(f"Your average score: {avg_score}/100")
#     speak(f"Your average score is {avg_score} out of 100")

# if __name__ == "__main__":
#     print("=== Welcome to AI Interview Simulator ===")
#     speak("Welcome to AI Interview Simulator")
#     run_interview()
import numpy as np

