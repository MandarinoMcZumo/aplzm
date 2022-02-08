import os

from registry.app import create_app

port = os.environ.get('PORT_REGISTRY')

if port is not None:
    port = str(port)
else:
    port = '5002'

# MAIN
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='localhost', port=port)
