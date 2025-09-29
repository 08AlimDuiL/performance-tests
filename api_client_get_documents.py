from clients_for_lessons.http.gateway.users.client import build_users_gateway_http_client
from clients_for_lessons.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.documents.client import build_documents_gateway_http_client

"""
Скрипт для получения документов по счету через HTTP API.

Выполняет последовательность действий:
1. Создание пользователя
2. Открытие кредитного счета
3. Получение документа тарифа
4. Получение документа контракта
"""

users_gateway_client = build_users_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()
documents_gateway_http_client = build_documents_gateway_http_client()

# Создаем пользователя.
create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)
print('-' * 80)

# Открывает кредитный счёт для этого пользователя.
open_credit_card_account_response = accounts_gateway_client.open_credit_card_account(
    # user_id=create_user_response['user']['id']
    user_id=create_user_response.user.id
)
print('Open credit card account response:', open_credit_card_account_response)
print('-' * 80)

# Получаем документ тарифа.
get_document_tariff_response = documents_gateway_http_client.get_tariff_document(
    # account_id=open_credit_card_account_response['account']['id']
    account_id=open_credit_card_account_response.account.id
)
print('Get tariff document response:', get_document_tariff_response)
print('-' * 80)

# Получаем документ контракта.
get_document_contract_response = documents_gateway_http_client.get_contract_document(
    # account_id=open_credit_card_account_response['account']['id']
    account_id=open_credit_card_account_response.account.id
)
print('Get contract document response:', get_document_contract_response)
print('-' * 80)
