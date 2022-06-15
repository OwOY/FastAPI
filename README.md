<p align='center'>
    <img src='https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png'/>
</p>

## Installation
- fastapi
```
python -m pip install fastapi
```
- uvicorn # fastapi使用uvicorn
```
python -m pip install uvicorn
```
--------------------------------------------------
## How to use fastapi
### mainapp.py
-  App
```
from fastapi import FastAPI
app = FastAPI()
```
- Setting
```
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
- Run
```
uvicorn.run(f'{filename}:app', host:'0.0.0.0', port=8089, reload=True)
```
>> filename為該檔案之名稱   reload為自動刷新功能(程式碼變更即更改)  

### Controller
- docs
```
from pydantic import BaseModel
from typing import Optional, List

class GetData(BaseModel):
    string:str
    integer:int
    list:list
    foo:List[int] # list內為int
    bar:Optional[str] # 參數可填可不填
```

#### Get
```
from fastapi import Depends
@app.get('/')
def test(request:GetData = Depends())
    return srv.test()
```
#### Post
```
@app.post('/')
def test(request:GetData):
    data = request.get_data
    return srv.test(data)
```
- response
```
from fastapi.responses import JSONResponse
@app.post('/')
def test():
    return JSONResponse(status_code=400, message={'foo':'bar'})
```
- UploadFile
```
from fastapi import UploadFile
@app.post('/uploadExcel')
def upload_excel(file_name:UploadFile)
    file = file_name.file # SpooledTemporaryFile
    file_name = file_name.filename # filename
    return srv.test(file_name)

!! requests post
files = {'file_name':binary} # file_name 對應API
response = requests.post(url, files=files)
```

### Service
```
class Srv:
    def test(data):
        return 'hello world'
```
### View
```
url = domain/docs      #開啟可執行API之UI介面
```

## 大架構使用案例
- Controller
```
from fastapi import APIRouter
```

- mainapp
```
from controller.user import users
app.include_router(users.router)
```
---- 
# fastapi + SQLalchemy
參閱 [Reserve專案](https://github.com/OwOY/side_project/tree/main/reserve) 
