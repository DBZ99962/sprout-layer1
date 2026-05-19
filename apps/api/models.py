# See full models in the repository
# All ORM models: User, Experience, Education, Skill, Resume
# JobPost, JobMatch, GuidedAnswer, GeneratedDoc
# AutomationRun, AutomationRunArtifact
# Full implementation available at apps/api/models.py
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, Text, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import uuid

def gen_uuid(): return str(uuid.uuid4())

class User(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True, default=gen_uuid)
    email = Column(String, unique=True, nullable=False)
    full_name = Column(String)
    phone = Column(String)
    location = Column(String)
    linkedin_url = Column(String)
    github_url = Column(String)
    portfolio_url = Column(String)
    created_at = Column(DateTime, server_default=func.now())

class JobPost(Base):
    __tablename__ = 'job_posts'
    id = Column(String, primary_key=True, default=gen_uuid)
    title = Column(String)
    company = Column(String)
    location = Column(String)
    description = Column(Text)
    requirements = Column(JSON)
    url = Column(String)
    created_at = Column(DateTime, server_default=func.now())

class AutomationRun(Base):
    __tablename__ = 'automation_runs'
    id = Column(String, primary_key=True, default=gen_uuid)
    user_id = Column(String, ForeignKey('users.id', ondelete='CASCADE'))
    job_id = Column(String)
    portal = Column(String)
    adapter = Column(String)
    mode = Column(String)
    status = Column(String, default='pending')
    steps = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())
