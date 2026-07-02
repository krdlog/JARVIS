import ollama


class AIEngine:

    def __init__(self):

        self.model = "llama3.2"

        self.system_prompt = """
You are JARVIS.

You are a desktop AI assistant.

Rules:
- Be concise.
- Be friendly.
- Never mention being an AI language model.
- Answer naturally.
- If asked to perform an action you cannot perform directly, explain briefly.
- Keep most replies under 3 sentences.
"""

        print("[AI] Llama 3.2 Online")

    def ask(self, prompt):

        try:

            response = ollama.chat(

                model=self.model,

                messages=[

                    {
                        "role": "system",
                        "content": self.system_prompt
                    },

                    {
                        "role": "user",
                        "content": prompt
                    }

                ]

            )

            return response["message"]["content"].strip()

        except Exception as e:

            return f"I couldn't reach the AI engine. {e}"