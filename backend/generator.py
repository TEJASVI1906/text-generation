generator.py
from transformers import pipeline

# Load the GPT-2 model once when the server starts
generator = pipeline("text-generation", model="gpt2")

def generate_text(prompt, max_length=150, temperature=0.7):
    output = generator(
        prompt,
        max_length=max_length,
        temperature=temperature,
        num_return_sequences=1
    )
    return output[0]['generated_text']