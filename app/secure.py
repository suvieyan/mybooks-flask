# 配置文件当中的值最好大写，类似于全局变量
# 数据库、密码、
# 生产环境的相关配置

DEBUG = True

# cymysql:引擎
# sqlalchemy 支持分布式的数据库

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost:3306/yan-books?charset=utf8' # 引擎
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True
SQLALCHEMY_MAX_OVERFLOW = 0  # 超过连接池大小外最多创建的连接
SQLALCHEMY_POOL_SIZE = 5  # 连接池大小
SQLALCHEMY_POOL_TIMEOUT = 30  # 池中没有线程最多等待的时间，否则报错
SQLALCHEMY_POOL_RECYCLE = -1  # 多久之后对线程池中的线程进行一次连接的回收（重置）

APPID = 'wx141565d8c5463713'
AppSecret = '52e5d7c4985d17edc9a16a134da2b9bc'

# 上传文件的文件夹
UPLOAD_FOLDER = 'upload'


