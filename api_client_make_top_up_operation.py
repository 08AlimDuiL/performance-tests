'''
from clients.http.gateway.users.client import build_users_gateway_http_client
from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.operations.client import build_operations_gateway_http_client

"""
Скрипт для создания операции пополнения счета.

Выполняет последовательность действий:
1. Создание пользователя;
2. Открытие дебетового счёт для этого пользователя;
3. Создание операции пополнения дебетового счета.
"""
users_gateway_client = build_users_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()
operations_client = build_operations_gateway_http_client()

# Создаем пользователя
create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)
print('-' * 80)

# Открываем дебетовый счет для пользователя
open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(
    user_id=create_user_response['user']['id']
)
print('Open debit card account response:', open_debit_card_account_response)
print('-' * 80)

# Получаем ID карты и аккаунта
account_id = open_debit_card_account_response['account']['id']
card_id = open_debit_card_account_response['account']['cards'][0]['id']

# Создаем операцию пополнения
make_top_up_operation_response = operations_client.make_top_up_operation(
    card_id=card_id,
    account_id=account_id
)
print('Make top up operation response:', make_top_up_operation_response)
print('-' * 80)
'''

from clients_for_lessons.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.operations.client import build_operations_gateway_http_client
from clients_for_lessons.http.gateway.users.client import build_users_gateway_http_client

users_gateway_client = build_users_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()
operations_gateway_client = build_operations_gateway_http_client()

create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)

open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(
    user_id=create_user_response.user.id
)
print('Open debit card account response:', open_debit_card_account_response)

make_top_up_operation_response = operations_gateway_client.make_top_up_operation(
    card_id=open_debit_card_account_response.account.cards[0].id,  # Используем атрибуты вместо ключей
    account_id=open_debit_card_account_response.account.id  # Используем атрибуты вместо ключей
)
print('Make top up operation response:', make_top_up_operation_response)
