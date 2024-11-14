import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# Modelo de Usuario
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(250), nullable=False, unique=True)
    full_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

# Modelo de Publicación
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    user = relationship(User)

# Modelo de Comentario
class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=False)
    post = relationship(Post)
    user = relationship(User)

# Modelo de Like
class Like(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    created_at = Column(DateTime, nullable=False)
    post = relationship(Post)
    user = relationship(User)

# Generar el diagrama
try:
    result = render_er(Base, 'diagram.png')
    print("¡Éxito! Revisa el archivo diagram.png")
except Exception as e:
    print("Hubo un problema al generar el diagrama")
    raise e
