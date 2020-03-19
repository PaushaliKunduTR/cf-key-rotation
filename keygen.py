from Crypto.PublicKey import RSA
# import boto3

KEY = RSA.generate(2048)


def get_privatekey():
    private_key = KEY.export_key()
    # file_out = open("private.pem", "wb")
    # file_out.write(private_key)
    # private_key = private_key.decode("utf-8")
    print(type(private_key))
    return private_key


# def put_privatekey(private_key):
#     client = boto3.client('secretsmanager')
#     response = client.put_secret_value(SecretId='arn:aws:secretsmanager:us-east-1:486076294107:secret:a205257/cfsigner/source-secret-C5X6dN',
#                                        SecretString=private_key)
#     return response


def get_publickey():
    public_key = KEY.publickey().export_key()
    file_out = open("public.pem", "wb")
    file_out.write(public_key)
    public_key = public_key.decode("utf-8")

    return public_key


if __name__ == '__main__':
    public_key = get_publickey()
    print(public_key)
