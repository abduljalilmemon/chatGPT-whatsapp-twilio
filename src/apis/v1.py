from flask import Blueprint
from loguru import logger

v1 = Blueprint('/v1', __name__, template_folder='templates')


@v1.get('/')
def main():
    try:
        response = 'hello'
        return response
    except Exception as e:
        logger.error(e)
    # return JSONResponse(content={}, status_code=500)
    return ''
