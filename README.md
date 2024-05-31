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
- Main  
    主要執行程式  
    ```python
    import uvicorn
    from fastapi import FastAPI
    
    app = FastAPI(title='demo') # 可設置swagger標題以及路徑
    
    
    if __name__ == '__main__':
        uvicorn.run('mainapp:app', host='0.0.0.0', port=8888)
    ```
    CORS設置
    ```python
    from fastapi.middleware.cors import CORSMiddleware

    app.add_middleware(
        CORSMiddleware, 
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    ```
- Schema
    定義輸入參數  
    ```python
    from pydantic import BaseModel
    
    class GetData(BaseModel):
        dataId: int
    ```
    - Get
        ```python
        from fastapi import Depends
        
        async def test(payload:GetData=Depends())
            test_id = payload.dataId
        ```
    - Post
        ```python
        async def test(payload:GetData)
            test_id = payload.dataId
        ```
- Controller  
    用於製作API設置
    ```python
    from fastapi.routing import APIRouter
    
    api = APIRouter(
        prefix='/test', # 設定路由初始路徑
        tags=['BuyCode維護'], # 設置Swagger標籤
        route_class=LogRoute  # 設置API相依類
    )
    ```
    - Get
        ```python
        from fastapi import Depends
    
        @api.get('/')
        def test(request:GetData = Depends())
            return srv.test()
        ```
    - Post
        ```python
        @api.post('/')
        def test(request:GetData):
            data = request.get_data
            return srv.test(data)
        ```
    - UploadFile
        ```python
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

- Service  
    主要計算邏輯
    ```python
    class Srv:
        def test(data):
            return 'hello world'
    ```
    物件轉換json
    ```python
    from fastapi.encoder import jsonable_encoder
    
    obj = session.query(ObjTest).first()
    data_dict = jsonable_encoder(obj)
    ```
    - Response
        - FileResponse
            ```python
            def file(path, file_name):
                return FileResponse(
                    f'{path}', # 檔案位置
                    media_type='application/vnd.ms-excel', # 設置檔案格式(此例為Excel)
                    filename=file_name # 設定輸出檔案名稱
                )
            ```
        - JsonResponse
            ```python
            def json_response(output):
                return JsonResponse(
                    f'{output}, # 輸出資料
                    status_code=200, # 輸出http_code
                    headers=headers  # 設定輸出標頭
                )
            ```
- Schedule
    ```python
    class BackgroundTask(threading.Thread):
        def run(self, *arg, **kwarg):
            from time import sleep
            while True:
                print('hello world')
                sleep(10)
    ```
    - mainapp.py
        ```python
        from schedule import BackgroundTask
        from fastapi import FastAPI
    
        app = FastAPI()
        @app.on_event('startup')
        def scheduler():
            task = BackgroundTask()
            task.start()
        ```
- Middleware
    - 全域中間層
        ```python
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
    - 單個模塊中間層邏輯  
        ```python
        from fastapi import HTTPException, Request
        
        async def controller_middleware(request:Request):
            # payload = request.query_params._dict # 若API為GET，則使用這個
            payload = await request.json() 
            if not payload:
                return HTTPException('未輸入參數', 400)
        ```
        ! 注意：若要Catch message，需抓取HTTPException  
        ```python
        try:
            filter_controller()
        except HTTPException as err:
            error_code = err.status_code # 400
            msg = err.detail # 未輸入參數
        ```
        Controller設置
        ```python
        from fastapi import Depends
        from fastapi.router import APIRouter
        api = APIRouter()
        
        @api.post('/middleTest')
        def middle_test(
            dependencies=[
                Depends(controller_middleware),
            ]
        ):
            ...
        
        ```

- Env
    ###  直接設置環境變數
        ```
        # CMD
        set test=test
        ```
    ### 讀取環境變數檔案
    1. 下載相依套件
        ```
        python -m pip install python-dotenv
        ```
    2. 新增.env檔案
       config.env
        ```
        test="TESTENV"
        ```
    4. Uvicorn CMD執行時命令
        1. 方法1
            ```
            uvicorn --env-file="config.env"
            ```
        2. 方法2
            ```python
            uvicorn.run('testapp:app', env_file='config.env')
            ```
    5. config.py
        ```python
        from pydantic import BaseSetting
        
        class Setting(BaseSetting):
            test:str
        print(Setting().test) # TESTENV
        ```

### 使用Request傳輸自定義變數(全域)
```python
from fastapi import Request

def tansport(func)
    def wrapper(request:Request)
        request.state.id = '123'
        return func(request)
    return wrapper
```

### Swagger 設立 Token驗證
- main.py
```python
from fastapi import FastAPI, Security, Depends
from fastapi.security import APIKeyHeader+

async def CheckHeader(
    token_key:str=Security(APIKeyHeader(name='Authorization'))
):
    return token_key

app = FastAPI(
    title='test',
    dependencies=[Depends(CheckHeader)]
)

```
### lifespan 設置
```python
from fastapi import FastAPI
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app:FastAPI):
    do something...
    yield
    end do something...

app = FastAPI(lifespan=lifespan)

```

### Gunicorn 
- Gunicorn CMD執行時命令(Windows不適用)
    ```
    # 官方文件設置
    gunicorn mainapp:app --worker 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8888
    ```
- Gunicorn Config設定  
    [gunicorn.conf.py](/gunicorn.conf.py)

<br>

## 大架構使用案例
- fastapi + SQLalchemy  
參閱 [Reserve專案(限本人)](https://github.com/OwOY/side_project/tree/main/reserve) 
