from fastapi import Request, Depends, UploadFile
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse
from middleware import LogRoute
from model import create_session
from controllerMiddleware import reject_no_payload
from service import SampleService
from schema import Test


api = APIRouter(
    prefix='/sample',
    tags=['sample'],
    route_class=LogRoute,
)


@api.get('/')
def hello_world(request:Request):
    # headers = request.headers
    return {'foo':'bar'}

@api.post('/insert', dependencies=[Depends(reject_no_payload)])
def insert(payload:Test, session = Depends(create_session)):
    foo = payload.foo
    bar = payload.bar
    response = SampleService().sample(session, foo, bar)
    return JSONResponse({'message':response})

@api.post('/upload')
def upload_file(
    file: UploadFile
):
    file_name = file.filename
    file_size = file.file.read()
    return JSONResponse({'file_name':file_name, 'file_size':len(file_size)})