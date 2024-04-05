"""empty message

Revision ID: a5e4eb71b18d
Revises: dd9c32932184
Create Date: 2024-04-05 20:51:55.405004

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'a5e4eb71b18d'
down_revision: Union[str, None] = 'dd9c32932184'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_index('ix_user_registered_at', table_name='user')
    op.drop_index('ix_user_username', table_name='user')
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('role_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('permissions', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='role_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('registered_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=320), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(length=1024), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_verified', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('role_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], name='user_role_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.create_index('ix_user_username', 'user', ['username'], unique=False)
    op.create_index('ix_user_registered_at', 'user', ['registered_at'], unique=False)
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    # ### end Alembic commands ###