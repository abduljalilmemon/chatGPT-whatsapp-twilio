from environs import Env

env = Env()
WORKER_ENV = env('WORKER_ENV', 'local')

if WORKER_ENV == 'local':
    env.read_env()

OPENAI_API_KEY = env.str('OPENAI_API_KEY')
