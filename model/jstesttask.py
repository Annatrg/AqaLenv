from pydantic import BaseModel


class JsTestTask(BaseModel):
    name: str
    image: str
    price: int
