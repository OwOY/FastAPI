from fastapi import FastAPI, Request
from docs import get_data
from production_service import SrvProductionSchedule
import uvicorn



srvProductionSchedule = SrvProductionSchedule()
app = FastAPI()


    
@app.post('/')
def get_data(request:get_data):
    """取得所有資料

    Args:
        order_no_list:List

    Returns:
        dict: {'data':Array}
    """
    if request:
        data = request.order_no_list
    else:
        data = []
    return srvProductionSchedule.get_data_list(data)
    
@app.post('/getorderno')
def get_order_no():
    """取得所有order_no

    Returns:
        dict: {'order_no_list':List}
    """
    return srvProductionSchedule.get_order_no_list()


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=10241, debug=True)
    uvicorn.run('mainapp:app', host='127.0.0.1', port=10241, reload=True)