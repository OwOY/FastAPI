from model import Test
from sqlalchemy.orm import Session

class SampleService():
    def __init__(self):
        pass
    
    def sample(self, session:Session, foo, bar):
        obj = Test()
        obj.foo = foo
        obj.bar = bar
        session.add(obj)
        session.commit()
        return '儲存成功'