from pydantic import BaseModel


class Test(BaseModel):
    foo: str
    bar: str