from datetime import datetime
from sqlalchemy import Table, BINARY, ForeignKey,\
    VARCHAR, BOOLEAN, Column, BIGINT, Index, PrimaryKeyConstraint, CHAR
from sqlalchemy.dialects.mysql import TINYINT, INTEGER, BIGINT, DATETIME, DECIMAL
from lib.sqlalchemydb import AlchemyDB


class FlaskDB(AlchemyDB):

    @classmethod
    def init(cls):
            AlchemyDB.init()

            FulfilmentDB.sample_table = Table(
                "sample_table", FulfilmentDB.metadata,
                Column("id", BIGINT, primary_key=True, autoincrement=True),
                Column("sample_field", VARCHAR(250)),
                
            )

            FulfilmentDB._table["sample_table"] = FulfilmentDB.sample_table