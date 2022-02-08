import os

from base.app import create_app

port = os.environ.get('PORT')

if port is not None:
    port = str(port)
else:
    port = '5005'

# MAIN
if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=port)
