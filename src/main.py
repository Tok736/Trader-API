from auth.router import register_router, auth_router
from operations.router import router as operations_router
from app import app

def register_all_routers() -> None:
    app.include_router(
        auth_router,
        prefix="/auth/jwt",
        tags=["auth"]
    )

    app.include_router(
        register_router,
        prefix="/auth",
        tags=["auth"]
    )

    app.include_router(
        operations_router,
        prefix="/operations",
        tags=["operations"]
    )

register_all_routers()
