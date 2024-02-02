from datetime import datetime
import enum

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,Boolean, Enum
from sqlalchemy.orm import relationship
from sqlalchemy_utils import URLType


from ..db_setup import Base
from .user import User
from .mixins import Timestamp

class ContentType(enum.Enum):
    lesson = 1
    quiz = 2
    assignment = 3
    exam = 4


class Course(Base, Timestamp):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False, index=True)
    description = Column(String(50), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))

    created_by = relationship(User, backref='courses')
    sections = relationship('Section', back_populates='course',uselist=False)
    student_courses = relationship('StudentCourse', back_populates='course')

    
class Section(Base, Timestamp):
    __tablename__ = 'sections'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False, index=True)
    description = Column(String(50), nullable=False, index=True)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
   
    course = relationship('Course', back_populates='sections')
    content_blocks = relationship('ContentBlock', back_populates='section')


class ContentBlock(Base, Timestamp):
    __tablename__ = 'content_blocks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False, index=True)
    description = Column(String(50), nullable=False, index=True)
    section_id = Column(Integer, ForeignKey('sections.id'), nullable=False)
    content_type = Column(Enum(ContentType), default=ContentType.lesson)
    url = Column(URLType, nullable=True)
    content = Column(String(50), nullable=False, index=True)

    section = relationship('Section', back_populates='content_blocks')
    completed_content_blocks = relationship('CompletedContentBlock', back_populates='content_block')


class StudentCourse(Base , Timestamp):
    __tablename__ = 'student_courses'

    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    student_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    completed = Column(Boolean, default=False)

    course = relationship('Course', back_populates='student_courses')
    student = relationship(User, back_populates='student_courses')


class CompletedContentBlock(Base, Timestamp):
    __tablename__ = 'completed_content_blocks'

    id = Column(Integer, primary_key=True, index=True)
    content_block_id = Column(Integer, ForeignKey('content_blocks.id'), nullable=False)
    student_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    url = Column(URLType, nullable=True)
    feedback = Column(String(50), nullable=False, index=True)
    grade = Column(Integer, nullable=False, index=True)

    content_block = relationship('ContentBlock', back_populates='completed_content_blocks')
    student = relationship(User, back_populates='completed_content_blocks')


