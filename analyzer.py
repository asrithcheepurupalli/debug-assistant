import openai

def analyze_text(text):
    prompt = f"You're an expert Python assistant. Analyze this error or log and explain the issue, and how to fix it:\n\n{text}"

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that debugs logs and errors."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=500
    )

    return response.choices[0].message.content