from app import app

from auth.router       import register_router, auth_router
from operations.router import router as operations_router
from users.router      import router as users_router
from tasks.router      import router as tasks_router

from admin_panel import admin

def register_all_routers() -> None:
    ''' Function to register all project routers '''
    app.include_router(auth_router)
    app.include_router(register_router)
    app.include_router(operations_router)
    app.include_router(users_router)
    app.include_router(tasks_router)

register_all_routers()
