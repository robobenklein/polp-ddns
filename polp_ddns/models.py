
from sqlalchemy import (
    Boolean, Column, ForeignKey, Integer, String, JSON, DateTime,
)
from sqlalchemy.orm import relationship

from .database import Base


class DDNSRecord(Base):
    __tablename__ = "ddns_records"

    id = Column(Integer, primary_key=True, index=True)
    fqdn = Column(String, index=True)
    description = Column(String, index=True)

    machine_id = Column(Integer, ForeignKey("machines.id"))
    machine = relationship("Machine", back_populates="ddns_records")

    provider_id = Column(Integer, ForeignKey("ddns_providers.id"))
    provider = relationship("DDNSProvider", back_populates="ddns_records")

class Machine(Base):
    __tablename__ = "machines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    update_token = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    last_seen = Column(DateTime, index=True)

    ddns_records = relationship("DDNSRecord", back_populates="machine")

class DDNSProvider(Base):
    __tablename__ = "ddns_providers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    provider_type = Column(String, nullable=False)
    provider_config = Column(JSON)

    ddns_records = relationship("DDNSRecord", back_populates="provider")
