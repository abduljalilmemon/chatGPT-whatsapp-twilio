from flask import Blueprint, request
from loguru import logger
from utils import generate_response

v1 = Blueprint('/v1', __name__, url_prefix='/v1')


@v1.post('/chatgpt')
def get_chatgpt_response():
    response = "no response"
    try:
        body = request.get_json()
        query = body.get('query', '').lower()
        logger.info(f'Q: {query}')
        response = generate_response(query)
    except Exception as e:
        logger.error(e)
    return response
