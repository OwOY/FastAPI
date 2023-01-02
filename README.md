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
- 若有上傳檔案，則需下載額外套件
```
python -m pip install python-multipart
```
--------------------------------------------------
## How to use fastapi
#### mainapp  
主要執行程式
```
import uvicorn
from fastapi import FastAPI

app = FastAPI(title='demo') # 可設置swagger標題以及路徑


if __name__ == '__main__':
    uvicorn.run('mainapp:app', host='0.0.0.0', port=8888)
```
- CORS設置
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
#### Controller  
用於製作API設置
```
from fastapi.routing import APIRouter

api = APIRouter(prefix='/test', # 設定路由初始路徑
                tags=['BuyCode維護'], # 設置Swagger標籤
                route_class=LogRoute) # 設置API相依類
```

- Get
```
from fastapi import Depends
@api.get('/')
def test(request:GetData = Depends())
    return srv.test()
```
- Post
```
@api.post('/')
def test(request:GetData):
    data = request.get_data
    return srv.test(data)
```
- UploadFile
```
from fastapi import UploadFile
@api.post('/uploadExcel')
def upload_excel(file:UploadFile)
    file = file_name.file # SpooledTemporaryFile
    file_name = file_name.filename # filename
    return srv.test(file_name)

!! requests post
files = {'file':binary} # file_name 對應API
response = requests.post(url, files=files)
```

#### Service  
主要計算邏輯
```
class Srv:
    def test(data):
        return 'hello world'
```
- 物件轉換json
```
from fastapi.encoder import jsonable_encoder
obj = session.query(ObjTest).first()
data_dict = jsonable_encoder(obj)
```
### Response
- FileResponse
```
def file():
    return FileResponse(
        f'{path}', # 檔案位置
        media_type='application/vnd.ms-excel', # 設置檔案格式(此例為Excel)
        filename=file_name # 設定輸出檔案名稱
    )
```
- JsonResponse
```
def output():
    return JsonResponse(
        f'{output}, # 輸出資料
        status_code=200, # 輸出http_code
        headers=headers) # 設定輸出標頭
```
### 啟動背景排程設置
- schedule.py
```
class BackgroundTask(threading.Thread):
    def run(self, *arg, **kwarg):
        from time import sleep
        while True:
            print('hello world')
            sleep(10)
```
- mainapp.py
```
from schedule import BackgroundTask
from fastapi import FastAPI

app = FastAPI()
@app.on_event('startup')
def scheduler():
    task = BackgroundTask()
    task.run()
```
### 設置API中間層
```
from fastapi.routing import APIRoute
from typing import Callable
from fastapi import Request, Response

class LogRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            """
            Do Something
            """
            response: Response = await original_route_handler(request)
            return response
```
## 環境變數設置
###  直接設置環境變數
```
set test=test
```
### 讀取環境變數檔案
- 下載相依套件
```
python -m pip install python-dotenv
```
- .env
```
test="TESTENV"
```
- config.py
```
from pydantic import BaseSetting
class Setting(BaseSetting):
    test:str
print(Setting().test) # TESTENV
```
- Uvicorn CMD執行時命令
```
uvicorn --env-file=".env"
```

### 使用Request傳輸自定義變數(全域)
```
from fastapi import Request

def test(request:Request)
    request.state.id = '123'
    return func(request)
```

### Gunicorn 
- Gunicorn CMD執行時命令(Windows不適用)
```
# 官方文件設置
gunicorn mainapp:app --worker 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8888
```
- Gunicorn Config設定  
![gunicorn.conf.py](/gunicorn.conf.py)

## 大架構使用案例
- fastapi + SQLalchemy  
參閱 [Reserve專案](https://github.com/OwOY/side_project/tree/main/reserve) 
