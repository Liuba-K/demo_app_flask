"""changed article

Revision ID: 24afa39cfdfa
Revises: c3b802b97e86
Create Date: 2023-03-29 00:35:16.578836

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24afa39cfdfa'
down_revision = 'c3b802b97e86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('articles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=200), server_default='', nullable=False))
        batch_op.add_column(sa.Column('body', sa.Text(), server_default='', nullable=False))
        batch_op.add_column(sa.Column('dt_created', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('dt_updated', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('articles', schema=None) as batch_op:
        batch_op.drop_column('dt_updated')
        batch_op.drop_column('dt_created')
        batch_op.drop_column('body')
        batch_op.drop_column('title')

    # ### end Alembic commands ###