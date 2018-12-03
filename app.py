from core import create_app
from core.config import BaseConfig
from core.extra import io

app = create_app(BaseConfig)

io.init_app(app)

if __name__ == '__main__':
    io.run(app, debug=True, host='0.0.0.0', port=8000)
