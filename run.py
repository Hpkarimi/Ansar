from app import app

context = ('cert.pem', 'key.pem')

app.run(host='0.0.0.0', port=443, ssl_context=context)
