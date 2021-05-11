import sys
import cx_Oracle
from conjur import Client
from conjur_iam_client import create_conjur_iam_client_from_env
import os

def handler(event, context):
    iam_role_name=os.environ['IAM_ROLE_NAME']
    access_key=os.environ['AWS_ACCESS_KEY_ID']
    secret_key=os.environ['AWS_SECRET_ACCESS_KEY']
    token=os.environ['AWS_SESSION_TOKEN']

    conjur_client = create_conjur_iam_client_from_env(iam_role_name, access_key, secret_key, token, ssl_verify=False)

    account_name = "epv/lob/AWS_LAMBDA_DEMO/Database-Oracle-34.224.65.69-appuser"

    username = conjur_client.get("{}/username".format(account_name)).decode('utf-8')
    address = conjur_client.get("{}/address".format(account_name)).decode('utf-8')
    password = conjur_client.get("{}/password".format(account_name)).decode('utf-8')
    dsn = "{}/xepdb1".format(address)

    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    cursor = connection.cursor()

    sql = "SELECT * FROM DUAL"
    cursor.execute(sql)

    columns = [i[0] for i in cursor.description]
    rows = [dict(zip(columns, row)) for row in cursor]

    return rows