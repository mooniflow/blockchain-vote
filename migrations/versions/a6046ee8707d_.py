"""empty message

Revision ID: a6046ee8707d
Revises: 39c06d7a5af6
Create Date: 2024-05-07 08:59:17.045465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6046ee8707d'
down_revision = '39c06d7a5af6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cand_prom',
    sa.Column('CID', sa.Integer(), nullable=False),
    sa.Column('PID', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['CID'], ['candidate.CID'], ),
    sa.ForeignKeyConstraint(['PID'], ['promise.PID'], ),
    sa.PrimaryKeyConstraint('CID', 'PID')
    )
    op.drop_table('candprom')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('candprom',
    sa.Column('CID', sa.INTEGER(), nullable=False),
    sa.Column('PID', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['CID'], ['candidate.CID'], ),
    sa.ForeignKeyConstraint(['PID'], ['promise.PID'], ),
    sa.PrimaryKeyConstraint('CID', 'PID')
    )
    op.drop_table('cand_prom')
    # ### end Alembic commands ###
