from fastapi import Request
from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend
from starlette.responses import Response

from app import app
from database import engine
from config import settings

from .dependencies import User, Role, Operation

class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        ''' Login to admin panel '''
        form = await request.form()
        username, password = form["username"], form["password"]

        if username == settings.sqladmin_login and password == settings.sqladmin_password:
            request.session.update({"token": "1234"})
            return True
        
        return False

    async def logout(self, request: Request) -> bool:
        ''' Logout from admin panel '''
        request.session.clear()

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token or token != "1234":
            return False

        return True

authentication_backend = AdminAuth(secret_key=settings.auth_secret_key)

admin = Admin(app, engine, authentication_backend=authentication_backend)

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
        Operation.quantity,
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
