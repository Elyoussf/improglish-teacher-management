from sqlmodel import SQLModel , Field
from pydantic import BaseModel
from datetime import datetime
from enum import StrEnum

class pack(StrEnum):
    TopPack = "Top Pack"
    AdvancedPack = "Advanced Pack"
    PremiumPack = "Premium Pack"
    StandardPlan = "Standard Plan"
    BasicPlan = "Basic Plan"

class TeacherBase(SQLModel):
    firstname : str
    lastname : str
    totalpaid : int # money
    totalsessions : int
    totalsessionsdone : int
    totalsessionspaid : int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})

class TransactionBase(SQLModel):

    teacher_id :int = Field(default=None , foreign_key="teacher.id")
    total : int
    session_id : int =  Field(default=None , foreign_key="session.id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})

class StudentBase(SQLModel):
    
    firstname : str
    lastaname : str
    pack_type : pack
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})

class SessionBase(SQLModel):
    Teacher_id : int =  Field(default=None , foreign_key="teacher.id")
    student_id : int =  Field(default=None , foreign_key="student.id")
    done : bool 
    paid : int =  Field(default=None,foreign_key="transaction.id")
    date : datetime
    notesfromteacher : str | None
    notesfromAdmin : str | None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow})

class AdminBase(SQLModel):
    key : str = None
    
#==========================@#$=====================

class Teacher(TeacherBase , table= True):
    __tablename__ = "teacher"
    id : int = Field(default=None , primary_key=True)

class Student(StudentBase , table = True):
    __tablename__ = "student"
    id : int = Field(default=None , primary_key=True)

class Session(SessionBase , table = True):
    __tablename__ = "session"
    id : int = Field(default=None , primary_key=True)

class Transaction(TransactionBase,table=True):
    __tablename__ = "session"
    id : int = Field(default=None , primary_key=True)

class Admin(AdminBase,table=True):
    __tablename__ = "admin"
    id : int =  Field(default=None , primary_key=True)
    


