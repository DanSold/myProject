import jwt
import datetime
import config

payload = {
    'name': 'Dan',
    'location': 'Ukraine',
    'password': 'dgkmsmkemmgddgdl;',
    'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=60),
    'iat': datetime.datetime.utcnow()
}

encode_jwt = jwt.encode(
    payload=payload,
    key=config.JWT_SECRET,
    algorithm='HS256'
)

decoded = jwt.decode(
    encode_jwt,
    config.JWT_SECRET,
    algorithms=['HS256'],
)
