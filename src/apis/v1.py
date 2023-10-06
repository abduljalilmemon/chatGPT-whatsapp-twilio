from flask import Blueprint
from loguru import logger
from utils import generate_response

v1 = Blueprint('/v1', __name__, template_folder='templates')


@v1.post('/chatgpt')
def get_chatgpt_response():
    pass


@v1.get('/')
def main():
    try:
        return 'Welcome to chatgpt-api'
    except Exception as e:
        logger.error(e)
    # return JSONResponse(content={}, status_code=500)
    return ''
