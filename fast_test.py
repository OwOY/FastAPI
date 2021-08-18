from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def test():
    return {'message':'Hello World'}
  
if __name__ == '__main__':
  uvicorn.run('fast_test:app', host='0.0.0.0', port=8089, reload=True)
