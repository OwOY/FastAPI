<p align='center'>
    <img src='https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png'/>
</p>

## Installation
- fastapi
```
python -m pip install fastapi
```
- uvicorn
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
- Run
```
uvicorn.run(f'{filename}:app', host:'0.0.0.0', port=8089, reload=True)
```
>> filename為該檔案之名稱   reload為自動刷新功能(程式碼變更即更改)  

### Controller
- docs
```
from pydantic import BaseModel

class GetData(BaseModel):
    string:str
    integer:int
    list:list
```
- api
```
@app.post('/')
def test(request:get_data):
    data = request.get_data
    return srv.test(data)
```
### Model
```
class Srv:
    def test(data):
        return 'hello world'
```
### View
```
url = domain/docs      #開啟可執行API之UI介面
```
