from affiliate_bypass.api import Api
from affiliate_bypass.core.config import Config
from affiliate_bypass.core.service_container import ServiceContainer

config = Config()
service_container = ServiceContainer(config=config)
api = Api(config=config, service_container=service_container).api
