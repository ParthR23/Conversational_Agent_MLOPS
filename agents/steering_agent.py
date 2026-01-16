from groq import Groq
import os
os.environ["GROQ_API_KEY"] = "" 

class SteeringAgent:
    def __init__(self):
        self.client = Groq()

    def route(self, query: str) -> str:
        prompt = f"""
        You are a routing agent for a conversational AI system.

Classify the user query into ONE category only:
- weather
- knowledge
- other

Rules:
- Return ONLY the category name
- Do NOT add explanations

User query: "{query}"
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature = 0,
            max_tokens = 5
        )

        route = response.choices[0].message.content.strip().lower()
        return route