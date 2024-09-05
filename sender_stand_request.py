import configuration
import requests
import data

'''
SOLICITUDES GET - EJERCICIOS

print("ssr get docs func starts")
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
response_doc = get_docs()
print(response_doc.status_code)
print("ssr get docs func ends")

print("ssr get logs func starts")
def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count": 20})
response_logs = get_logs()
print(response_logs.status_code)
print(response_logs.headers)
print("ssr get logs func ends")
'''

print("ssr get users table func start")
def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response_userstable = get_users_table()
print(response_userstable.status_code)
print("ssr get users table func end")

print("ssr post new user func start")
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

response_newuser= post_new_user(data.user_body)
print(response_newuser.status_code)
print(response_newuser.json())
print("ssr post new user func end")


'''
print("ssr products kits func starts")
def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data.headers)
response_product = post_products_kits(data.product_ids)
print(response_product.status_code)
print(response_product.json())
print("ssr products kits func ends")
'''

