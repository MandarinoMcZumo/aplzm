import os

from predict.app import create_app

port = os.environ.get('PORT_PREDICT')

if port is not None:
    port = str(port)
else:
    port = '5001'

# MAIN
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='localhost', port=port)
