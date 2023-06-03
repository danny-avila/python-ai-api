import openai

def sentiment_analysis(text, api_key):
    openai.api_key = api_key

    try:
        response = openai.Completion.create(
            engine="davinci-codex",
            prompt=f"Perform sentiment analysis on the following text: {text}",
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.5,
        )

        sentiment = response.choices[0].text.strip()
        return sentiment

    except Exception as e:
        return str(e)