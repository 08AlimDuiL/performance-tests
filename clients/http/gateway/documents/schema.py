from pydantic import BaseModel, HttpUrl


class DocumentSchema(BaseModel):
    url: HttpUrl
    document: str


class GetTariffDocumentResponseSchema(BaseModel):
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    contract: DocumentSchema
