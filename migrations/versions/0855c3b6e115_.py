"""empty message

Revision ID: 0855c3b6e115
Revises: 
Create Date: 2018-07-13 15:47:45.040964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0855c3b6e115'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('label',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('requester', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('date', sa.String(length=120), nullable=True),
    sa.Column('service', sa.String(length=255), nullable=True),
    sa.Column('orderer', sa.String(length=255), nullable=True),
    sa.Column('actions', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_date'), 'order', ['date'], unique=False)
    op.create_index(op.f('ix_order_requester'), 'order', ['requester'], unique=False)
    op.create_table('service',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('about_me', sa.String(length=140), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('equipment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('label_id', sa.Integer(), nullable=True),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.Column('model', sa.String(length=120), nullable=True),
    sa.Column('serial', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['label_id'], ['label.id'], ),
    sa.ForeignKeyConstraint(['service_id'], ['service.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_equipment_model'), 'equipment', ['model'], unique=False)
    op.create_index(op.f('ix_equipment_name'), 'equipment', ['name'], unique=False)
    op.create_table('interview',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('requester', sa.String(length=120), nullable=True),
    sa.Column('service_id', sa.String(length=255), nullable=True),
    sa.Column('equipment_id', sa.Integer(), nullable=True),
    sa.Column('reasons', sa.String(length=255), nullable=True),
    sa.Column('interviewer', sa.String(length=255), nullable=True),
    sa.Column('request_date', sa.String(length=120), nullable=True),
    sa.Column('request_time', sa.String(length=120), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('actions', sa.String(length=255), nullable=True),
    sa.Column('start_date', sa.String(length=120), nullable=True),
    sa.Column('end_date', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['equipment_id'], ['equipment.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_interview_requester'), 'interview', ['requester'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_interview_requester'), table_name='interview')
    op.drop_table('interview')
    op.drop_index(op.f('ix_equipment_name'), table_name='equipment')
    op.drop_index(op.f('ix_equipment_model'), table_name='equipment')
    op.drop_table('equipment')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('service')
    op.drop_index(op.f('ix_order_requester'), table_name='order')
    op.drop_index(op.f('ix_order_date'), table_name='order')
    op.drop_table('order')
    op.drop_table('label')
    op.drop_table('category')
    # ### end Alembic commands ###
