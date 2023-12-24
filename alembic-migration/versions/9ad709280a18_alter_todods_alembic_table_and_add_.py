"""alter todods_alembic table and add completion_time colomn

Revision ID: 9ad709280a18
Revises: cf1869d32fa3
Create Date: 2023-12-20 12:13:05.431403

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9ad709280a18'
down_revision: Union[str, None] = 'cf1869d32fa3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("ALTER TABLE `alembic-db-migration`.todos_alembic ADD completion_time TIMESTAMP;")


def downgrade() -> None:
    op.drop_column("todos_alembic", "completion_time")
