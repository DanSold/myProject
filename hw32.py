import jwt
import datetime
import config

payload = {
    'name': 'Dan',
    'location': 'Ukraine',
    'password': 'dgkmsmkemmgddgdl;',
    'exp': datetime.datetime.utcnow() - datetime.timedelta(seconds=60),
    'iat': datetime.datetime.utcnow()
}


def encode_jwt(payload_dict: dict, algorithm: str) -> str:
    result_encode_jwt = jwt.encode(
        payload=payload_dict,
        key=config.JWT_SECRET,
        algorithm=algorithm
    )
    return result_encode_jwt


def decoded_jwt(input_encode_jwt: str, algorithm: list) -> dict | None:
    try:
        decoded = jwt.decode(
            input_encode_jwt,
            config.JWT_SECRET,
            algorithms=algorithm,
        )
        return decoded
    except:
        return None


encode_jwt_item = encode_jwt(payload_dict=payload, algorithm='HS256')
print(encode_jwt_item)
print(decoded_jwt(input_encode_jwt=encode_jwt_item, algorithm=['HS256']))
