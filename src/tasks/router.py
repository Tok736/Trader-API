from fastapi import APIRouter, Depends

from .dependencies import get_current_user, User
from .tasks import send_email_report_dashboard

router = APIRouter(
    prefix="/reports",
    tags=["reports"]
)

@router.get("/dashboard")
async def get_dashboard_report(
        user: User = Depends(get_current_user)
    ):
    send_email_report_dashboard.delay(user.username)
    return {"detail": "Email was delivered"}