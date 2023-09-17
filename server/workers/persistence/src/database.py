import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


bind_params = {
    "user": os.getenv("POSTGRES_USER"),
    "pw": os.getenv("POSTGRES_PASSWORD"),
    "host": os.getenv("POSTGRES_HOST"),
    "port": os.getenv("POSTGRES_PORT"),
    "db": os.getenv("DEFAULT_DATABASE")
}

sessions = {}
sessions[os.getenv("DEFAULT_DATABASE")] = sessionmaker(bind=create_engine('postgresql+psycopg2://%(user)s:%(pw)s@/%(db)s?%(host)s' % bind_params,
                                                                 max_overflow=15,
                                                                 pool_pre_ping=True,
                                                                 pool_recycle=3600,
                                                                 pool_size=30))
if "DATABASES" in os.environ:
    if os.getenv("DATABASES") != "":
        for database in os.getenv("DATABASES").split(","):
            bind_params["db"] = database
            sessions[database] = sessionmaker(bind=create_engine('postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % bind_params,
                                                                 max_overflow=15,
                                                                 pool_pre_ping=True,
                                                                 pool_recycle=3600,
                                                                 pool_size=30
                                                                 ))
Base = declarative_base()