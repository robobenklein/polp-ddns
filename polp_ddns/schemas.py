
from pydantic import BaseModel


class DDNSRecordBase(BaseModel):
    fqdn: str
    description: str = None

class DDNSRecordCreate(DDNSRecordBase):
    password: str

class DDNSRecord(DDNSRecordBase):
    id: int
    provider_id: int

    class Config:
        from_attributes = True


class DDNSProviderBase(BaseModel):
    name: str
    provider_type: str

class DDNSProviderCreate(DDNSProviderBase):
    name: str
    provider_type: str
    provider_config: dict

class DDNSProvider(DDNSProviderBase):
    id: int
    provider_config: dict
    ddns_records: list[DDNSRecord] = []

    class Config:
        from_attributes = True


class MachineBase(BaseModel):
    name: str
    is_active: bool = True

class MachineCreate(MachineBase):
    pass

class Machine(MachineBase):
    id: int
    update_token: str
    ddns_records: list[DDNSRecord] = []

    class Config:
        from_attributes = True


class MachineUpdateReport(BaseModel):
    machine: Machine
    records: list[DDNSRecord]
