from pydantic import BaseModel, EmailStr

class ContactFormDTO(BaseModel):
    name: str
    phone: str
    email: EmailStr
    subject: str
    message: str

class ContactResponseDTO(BaseModel):
    status: str
    message: str