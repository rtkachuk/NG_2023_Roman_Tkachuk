"""Created table News

Revision ID: 5f7fc98a6268
Revises: db3e4a35959f
Create Date: 2023-05-14 21:30:48.714382

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f7fc98a6268'
down_revision = 'db3e4a35959f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.Text(), nullable=True),
    sa.Column('desc', sa.Text(), nullable=True),
    sa.Column('author', sa.Integer(), nullable=True),
    sa.Column('creationDate', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news')
    # ### end Alembic commands ###
