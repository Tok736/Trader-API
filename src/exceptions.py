from fastapi import HTTPException

class UserNotFound(HTTPException):
    def __init__(
            self, 
            status_code: int = 404, 
            detail:      str = "User not found", 
        ) -> None:
        super().__init__(status_code, detail)
