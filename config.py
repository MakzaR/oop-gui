from pydantic import BaseSettings


class ServiceSettings(BaseSettings):
    host: str
    port: int


service_settings = ServiceSettings(host='localhost',port=5000)
