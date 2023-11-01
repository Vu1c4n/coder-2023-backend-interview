from pydantic import BaseModel, validator

class Identity(BaseModel):
    name:str
    age:int
    sex:str

    # sex-数据验证
    @validator('sex')
    def checkSex(cls,v):
        if v not in ('male', 'female'):
            raise ValueError('unexisting sex')
        return v
    
