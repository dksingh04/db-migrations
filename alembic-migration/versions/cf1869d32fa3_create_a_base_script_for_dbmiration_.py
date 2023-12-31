"""Create a base script for dbmiration application

Revision ID: cf1869d32fa3
Revises: 
Create Date: 2023-12-10 07:48:34.141513

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'cf1869d32fa3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table("users_alembic",
                    sa.Column("id", sa.BigInteger(), primary_key=True, index=True),
                    sa.Column("email", sa.String(length=100), nullable=False, unique=True),
                    sa.Column("username", sa.String(length=50), unique=True),
                    sa.Column("first_name", sa.String(length=50), nullable=False),
                    sa.Column("last_name", sa.String(length=50)),
                    sa.Column("hashed_password", sa.String(length=200), nullable=False),
                    sa.Column("is_active", sa.BOOLEAN, nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    mysql_collate='utf8mb4_0900_ai_ci',
                    mysql_default_charset='utf8mb4',
                    mysql_engine='InnoDB'
                    )

    op.create_table("todos_alembic",
                    sa.Column("id", sa.BigInteger(), primary_key=True, index=True),
                    sa.Column("title", sa.String(length=100), nullable=False),
                    sa.Column("description", sa.String(length=400)),
                    sa.Column("priority", sa.INTEGER),
                    sa.Column("complete", sa.BOOLEAN, default=False),
                    sa.Column("owner_id", sa.BigInteger(), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.ForeignKeyConstraint(["owner_id"], ["users_alembic.id"]),
                    mysql_collate = 'utf8mb4_0900_ai_ci',
                    mysql_default_charset = 'utf8mb4',
                    mysql_engine = 'InnoDB'
                    )

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
   ''' op.create_table('alembic_version',
    sa.Column('version_num', mysql.VARCHAR(length=32), nullable=False),
    sa.PrimaryKeyConstraint('version_num'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    '''
    # ### end Alembic commands ###
