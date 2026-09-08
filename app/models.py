from pydantic import BaseModel, EmailStr


class FormData(BaseModel):
    name: str
    email: EmailStr
    phone: str
    city: str
    interest: str
    message: str


class AIResponse(BaseModel):
    category: str
    priority: str
    summary: str