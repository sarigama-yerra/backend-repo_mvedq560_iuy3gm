from pydantic import BaseModel, Field, EmailStr

class ContactMessage(BaseModel):
    """
    Contact messages submitted from the website
    Collection name: "contactmessage" (lowercased class name)
    """
    name: str = Field(..., min_length=2, max_length=100, description="Sender name")
    email: EmailStr = Field(..., description="Sender email")
    message: str = Field(..., min_length=10, max_length=5000, description="Message body")
