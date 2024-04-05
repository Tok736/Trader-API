from sqladmin import Admin, ModelView

from app import app
from database import engine

from .dependencies import User, Role, Operation

admin = Admin(app, engine)

class RoleModelView(ModelView, model=Role):
    column_list = [
        Role.id, 
        Role.name, 
        Role.permissions,
        Role.created_at
    ]
    form_excluded_columns = [
        Role.created_at, 
        Role.updated_at
    ]

class OperationModelView(ModelView, model=Operation):
    column_list = [
        Operation.id, 
        Operation.quantinity,
        Operation.figi, 
        Operation.instrument_type, 
        Operation.date,
        Operation.created_at
    ]
    form_excluded_columns = [
        Operation.created_at, 
        Operation.updated_at
    ]

class UserModelView(ModelView, model=User):
    column_list = [
        User.id, 
        User.username,
        User.email, 
        User.registered_at,
    ]
    form_excluded_columns = [
        User.registered_at, 
        User.updated_at
    ]

admin.add_view(RoleModelView)
admin.add_view(OperationModelView)
admin.add_view(UserModelView)
