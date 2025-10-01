import grpc # Обеспечивает: создание канала связи с сервером, преобразование данных в бинарный формат, управление соединением
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub # "клиент" для работы с сервисом счетов. Stub в gRPC - это прокси-объект, который преобразует вызовы методов Python в сетевые запросы
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest, # автоматически генерируются из .proto файлов
    OpenDebitCardAccountResponse
)
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse
)
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse
)
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.operations.operation_pb2 import OperationStatus # перечисление (enum) со статусами операций
from tools.fakers import fake

channel = grpc.insecure_channel("localhost:9003") # Это вызов функции, которая создаёт и возвращает объект Channel

#Stub - это прокси-объект или представитель удалённого сервиса на клиентской стороне.
users_gateway_service = UsersGatewayServiceStub(channel)
accounts_gateway_service = AccountsGatewayServiceStub(channel)
operations_gateway_service = OperationsGatewayServiceStub(channel)

# 1. Создание нового пользователя
create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number()
)
create_user_response: CreateUserResponse = users_gateway_service.CreateUser(create_user_request)

print('Create user response:', create_user_response)

# 2 Открытие дебетового счета
open_debit_card_account_request = OpenDebitCardAccountRequest(
    user_id=create_user_response.user.id
)
open_debit_card_account_response: OpenDebitCardAccountResponse = (
    accounts_gateway_service.OpenDebitCardAccount(open_debit_card_account_request)
)

print('Open debit card account response:', open_debit_card_account_response)

# 3 Операция пополнения счета
make_top_up_operation_request = MakeTopUpOperationRequest(
    status=OperationStatus.OPERATION_STATUS_COMPLETED,
    amount=fake.amount(),
    card_id=open_debit_card_account_response.account.cards[0].id,
    account_id=open_debit_card_account_response.account.id
)

make_top_up_operation_response: MakeTopUpOperationResponse = (
    operations_gateway_service.MakeTopUpOperation(make_top_up_operation_request)
)

print('Make purchas operation:', make_top_up_operation_response)

# 4 Получение чека по операции
operation_receipt_request = GetOperationReceiptRequest(
    operation_id=make_top_up_operation_response.operation.id
)

operation_receipt_response: GetOperationReceiptResponse = (
    operations_gateway_service.GetOperationReceipt(operation_receipt_request)
)
print('Get operation receipt response:', operation_receipt_response)
