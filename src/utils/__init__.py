from uuid import uuid4

import openai


def generate_response(query):
    model_engine = "text-davinci"
    prompt = f"Q: {query}\nA:"
    response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None,
                                        temperature=0.7)
    print(response)
    return response


def auth_user(username, password):
    return False, "username or password is invalid"
