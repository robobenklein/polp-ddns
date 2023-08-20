
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


class MachineUpdateParams(BaseModel):
    # TODO: allow machine to provide it's own SSH fingerprints:
    # polpddns will verify they match and can then set SSHFP records
    # TODO: allow machine to limit which records it wants updated (by type, fqdn, or id?)
    pass

class MachineUpdateReport(BaseModel):
    """Update results returned to machine."""
    machine: Machine
    records: list[DDNSRecord]


class HTTPError(BaseModel):
    detail: str

    class Config:
        json_schema_extra = {
            "example": {"detail": "Some information about why the HTTPException was raised."},
        }
