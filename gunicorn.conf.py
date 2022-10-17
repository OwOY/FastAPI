import multiprocessing

bind = '0.0.0.0:9088' # 綁定FASTAPI接口
workers = 2 # 並行工作進程數   預設為2*CPU+1
worker_class = 'uvicron.workers.UvicornWorker' # 還可以使用gevent模式以及sync模式，默認sync模式
threads = 1 # 指定worker的線程數
backlog = 2048 # 監聽隊列
timeout = 120 # 逾時多少秒後工作將被殺掉，並重新啟動。一般設置為30秒或更多
worker_connections = 1000 # 設置最大併發
daemon = False # 默認False，設置守護進程，將近成交给supervisor管理
debug = True
loglevel = 'debug'
proc_name = 'main' # 默認None，這會影響ps和top。如果運行多個Gunicorn，需要設置一个名稱來區分，就得安装setproctitle模組。如果未安装
accesslog = './logs/access.log'
pidfile = './logs/gunicron.pid' # 設置進程文件目錄
errorlog = './logs/error.log'
#logger_class = 'gunicron.gologging.Logger'
preload_app = True # 預加載資源
autorestart = True
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" " "%(a)s"' # 設置gunicron LOG，無法設置ERROR LOG

# 啟用方式
# gunicorn -c gunicorn.py main:app -k uvicorn.workers.UvicornWorker
