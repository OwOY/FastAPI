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
- UI
```
url = domain/docs      #開啟可執行API之UI介面
```
