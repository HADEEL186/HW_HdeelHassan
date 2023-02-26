"""contact added

Revision ID: 7d86a09bd2c6
Revises: 55cbd02e1e9e
Create Date: 2023-01-30 13:58:27.642832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d86a09bd2c6'
down_revision = '55cbd02e1e9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('message', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('women', schema=None) as batch_op:
        batch_op.add_column(sa.Column('rate', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('name', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('position', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('company', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('country', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('birth_date', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('about', sa.String(length=200), nullable=False))
        batch_op.drop_column('Rate')
        batch_op.drop_column('Birth_date')
        batch_op.drop_column('Position')
        batch_op.drop_column('About')
        batch_op.drop_column('Name')
        batch_op.drop_column('Country')
        batch_op.drop_column('Company')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('women', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Company', sa.VARCHAR(length=20), nullable=False))
        batch_op.add_column(sa.Column('Country', sa.VARCHAR(length=20), nullable=False))
        batch_op.add_column(sa.Column('Name', sa.VARCHAR(length=20), nullable=False))
        batch_op.add_column(sa.Column('About', sa.VARCHAR(length=200), nullable=False))
        batch_op.add_column(sa.Column('Position', sa.VARCHAR(length=20), nullable=True))
        batch_op.add_column(sa.Column('Birth_date', sa.VARCHAR(length=20), nullable=False))
        batch_op.add_column(sa.Column('Rate', sa.INTEGER(), nullable=False))
        batch_op.drop_column('about')
        batch_op.drop_column('birth_date')
        batch_op.drop_column('country')
        batch_op.drop_column('company')
        batch_op.drop_column('position')
        batch_op.drop_column('name')
        batch_op.drop_column('rate')

    op.drop_table('contact')
    # ### end Alembic commands ###
