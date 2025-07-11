from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True  # kalau pydantic v2, ini pengganti orm_mode
