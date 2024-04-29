from auth.manager import fastapi_users
from users.models import User

get_current_user = fastapi_users.current_user()
