from sqlalchemy import Column, Integer, Float, String, DateTime
from datetime import datetime
from database import Base

class OptimizationLog(Base):
    __tablename__ = "optimization_logs"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    occupancy = Column(Integer)
    outdoor_temp = Column(Float)
    outdoor_humidity = Column(Float)
    recommended_setpoint = Column(Float)
    recommended_mode = Column(String)
