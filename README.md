# FastAPI

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
- Run
```
uvicorn.run(f'{filename}:app', host:'0.0.0.0', port=8089, reload=True)
```
>> filename為該檔案之名稱   reload為自動刷新功能(程式碼變更即更改)
- variable page
domain/?page=test  
{message:test}  
```
def api(params):
    return {'message':params}
```

