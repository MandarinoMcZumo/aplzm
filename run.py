import os

from app import create_app

port = os.environ.get('PORT')

if port is not None:
    port = str(port)
else:
    port = '5005'

# MAIN
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=port)
