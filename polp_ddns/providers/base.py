
from .. import database, models, schemas


class DDNSProvider():
    def update_record(*a, **kwa):
        raise NotImplementedError()

    def get_record(*a, **kwa):
        raise NotImplementedError()

class DDNSProviderConfigSchema(schemas.BaseModel):
    pass
