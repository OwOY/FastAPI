from fastapi import FastAPI
import uvicorn


app = FastAPI(
    title='Sample',
)


from controller import api as sample_api
app.include_router(sample_api)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=1234, reload=True)