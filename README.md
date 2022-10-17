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
- mainapp  
主要執行程式
- config  
設定檔
```
from sqlalchemy import create_engine

DIALCT = "mysql" # DB名稱
DRIVER = "pymysql" # DB連線套件
USERNAME = "root" # 帳號
PASSWORD = "PassW0rd" # 密碼
HOST = "127.0.0.1" # 連線位置
PORT = "3306" # 埠號
DATABASE = "bps-mm" # 使用DB
DB_URL = f"{DIALCT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

engine = create_engine(DB_URL)
```
- model  
用於定義連線、資料庫設置  

#### 相依資料庫設置
```
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
meta_obj = MetaData(schema=schema)
Base = declarative_base(metadata=meta_obj)
```
#### 自動建立Schema
```
from config import engine
from sqlalchemy.schema import CreateSchema

schema = 'test'
engine.execute(CreateSchema(schema))
```
#### 自動建立TABLE
```
schema = 'test'
meta_obj = MetaData(schema=schema)
Base.metadata.create_all(bind=engine)
```
#### 設置連線
```
sess = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = sess()
```
- Controller  
用於製作API設置
#### API設置
```
from fastapi.routing import APIRouter

api = APIRouter(prefix='/test', # 設定路由初始路徑
                tags=['BuyCode維護'], # 設置Swagger標籤
                route_class=LogRoute) # 設置API相依類
```

#### Get
```
from fastapi import Depends
@api.get('/')
def test(request:GetData = Depends())
    return srv.test()
```
#### Post
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
def upload_excel(file_name:UploadFile)
    file = file_name.file # SpooledTemporaryFile
    file_name = file_name.filename # filename
    return srv.test(file_name)

!! requests post
files = {'file_name':binary} # file_name 對應API
response = requests.post(url, files=files)
```

- Service  
主要計算邏輯
```
class Srv:
    def test(data):
        return 'hello world'
```
### 物件轉換json
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
### 環境變數檔案設置
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

### 使用Request傳輸自定義變數
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
