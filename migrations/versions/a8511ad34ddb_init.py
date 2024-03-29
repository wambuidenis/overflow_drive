"""init

Revision ID: a8511ad34ddb
Revises: 
Create Date: 2021-08-02 15:39:46.166764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a8511ad34ddb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('destination_departure',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=100), nullable=False),
    sa.Column('lastname', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('type', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id', 'firstname'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('mpesa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=True),
    sa.Column('receipt_number', sa.String(length=255), nullable=True),
    sa.Column('transaction_date', sa.String(length=255), nullable=True),
    sa.Column('phone_number', sa.Integer(), nullable=True),
    sa.Column('checkout_request_id', sa.String(length=255), nullable=True),
    sa.Column('merchant_request_id', sa.String(length=255), nullable=True),
    sa.Column('result_code', sa.Integer(), nullable=False),
    sa.Column('result_desc', sa.Text(), nullable=True),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('qr', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('password_token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=250), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('payment_dump',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('data', sa.Text(), nullable=True),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=255), nullable=False),
    sa.Column('date_added', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('route',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('departure', sa.Integer(), nullable=False),
    sa.Column('destination', sa.Integer(), nullable=False),
    sa.Column('fare', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['departure'], ['destination_departure.id'], ),
    sa.ForeignKeyConstraint(['destination'], ['destination_departure.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('fleet',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('route', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['route'], ['route.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('route', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=50), nullable=True),
    sa.ForeignKeyConstraint(['route'], ['route.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('car',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plate_number', sa.String(length=100), nullable=False),
    sa.Column('fleet_id', sa.Integer(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('owner', sa.Integer(), nullable=True),
    sa.Column('in_service', sa.Boolean(), nullable=True),
    sa.Column('route', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fleet_id'], ['fleet.id'], ),
    sa.ForeignKeyConstraint(['owner'], ['user.id'], ),
    sa.ForeignKeyConstraint(['route'], ['route.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('plate_number')
    )
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('route', sa.Integer(), nullable=False),
    sa.Column('car', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['car'], ['car.id'], ),
    sa.ForeignKeyConstraint(['route'], ['route.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('group')
    op.drop_table('car')
    op.drop_table('stage')
    op.drop_table('fleet')
    op.drop_table('route')
    op.drop_table('payment_dump')
    op.drop_table('password_token')
    op.drop_table('mpesa')
    op.drop_table('user')
    op.drop_table('destination_departure')
    # ### end Alembic commands ###
