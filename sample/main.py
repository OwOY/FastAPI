import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller import api as sample_api


app = FastAPI(
    title='Sample',
)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(sample_api)

    
if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=1234, reload=True)