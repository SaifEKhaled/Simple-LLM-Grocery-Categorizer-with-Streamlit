import ollama

def categorize_items(prompt: str, model="llama3.2"):
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.get("message", {}).get("content", "No response")
    except Exception as e:
        return f"Error during model generation: {e}"
