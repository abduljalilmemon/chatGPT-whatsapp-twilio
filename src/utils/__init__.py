import jmespath
import openai
from config import OPENAI_API_KEY


def generate_response(query):
    model_engine = "text-davinci-002"
    prompt = f"Q: {query}\nA:"
    openai.api_key = OPENAI_API_KEY
    raw_response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None,
                                            temperature=0.7)
    response = jmespath.search('choices[0].text', raw_response)
    return response


def auth_user(username, password):
    return False, "username or password is invalid"
