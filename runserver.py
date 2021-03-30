"""
This script runs the PrivacyWebsite application using a development server.
"""

from os import environ
from PrivacyWebsite import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, threaded=True, ssl_context=('cert.pem', 'privkey.pem'))

 
#uncomment this and comment above to run redirector on port 80?
#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=80, threaded=True)
