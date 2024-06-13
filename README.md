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
    ex: [main.py](sample/main.py)  
- Schema
    定義輸入參數    
    ex: [schema.py](sample/schema.py)
- Controller  
    用於製作API設置  
    ex: [controller.py](sample/controller.py)

- Service  
    主要計算邏輯  
    ex: [service.py](sample/service.py)
- Middleware
    - 全域中間層
        用於做系統層面卡控  
        ex: [middleware.py](sample/middleware.py)  
    - 單個模塊中間層邏輯  
        用於做各服務層面卡控  
        ex: [filter.py](sample/filter.py)  
        ! 注意：若要Catch message，需抓取HTTPException  
        ```python
        try:
            filter_controller()
        except HTTPException as err:
            error_code = err.status_code # 400
            msg = err.detail # 未輸入參數
        ```
        Controller套用設置
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
