from sqlalchemy import Column, Integer, String, ForeignKey, Float, Text, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class Call(Base):
    __tablename__ = 'calls'
    id = Column(Integer, primary_key=True, index=True)
    caller_number = Column(String, nullable=False)
    receiver_number = Column(String, nullable=False)
    call_start_time = Column(DateTime, default=datetime.utcnow)
    call_end_time = Column(DateTime, default=datetime.utcnow)
    status = Column(String, nullable=False)

    transcripts = relationship("Transcript", back_populates="call")
    intents = relationship("Intent", back_populates="call")

class Transcript(Base):
    __tablename__ = 'transcripts'
    id = Column(Integer, primary_key=True, index=True)
    call_id = Column(Integer, ForeignKey('calls.id'))
    transcript_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    call = relationship("Call", back_populates="transcripts")

class Intent(Base):
    __tablename__ = 'intents'
    id = Column(Integer, primary_key=True, index=True)
    call_id = Column(Integer, ForeignKey('calls.id'))
    intent_name = Column(String, nullable=False)
    confidence_score = Column(Float, nullable=False)
    detected_at = Column(DateTime, default=datetime.utcnow)

    call = relationship("Call", back_populates="intents")
