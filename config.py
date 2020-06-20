from pydantic import BaseSettings


class ServiceSettings(BaseSettings):
    host: str
    port: int
    max_workers: int


service_settings = ServiceSettings(host='localhost',port=5000,max_workers=20)
