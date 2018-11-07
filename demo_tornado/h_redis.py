import redis
import time

'''
r = redis.Redis(host='10.133.146.250', port=6379,decode_responses=True)
#r = redis.StrictRedis(host='0.0.0.0', port=6379, db=0) 指定redis的数据库db
r.set('name', 'test')
print(r.get('name')) #默认取出来的为字节型b'test'， 设定decode_responses=True可将其改为字符串
'''
pool=redis.ConnectionPool(host='10.133.146.250', port=6379,decode_responses=True)#直接建立一个连接池
#r=redis.Redis(connection_pool=pool)
r = redis.StrictRedis(connection_pool=pool)#Redis是StrictRedis的子类，StrictRedis用于实现大部分官方的命令。


#string操作
r.set('age', '16')
r.set('age','17')
print(r.get('age'))

r.setnx('a', 'python') # 第一次设置时，键值a不存在，设置值，只有name不存在时，执行设置操作（添加）
r.setnx('a', 'golang') # 再次设置，键值a已经存在了
print(r.get('a'))

r.psetex('name','1','test')
time.sleep(0.1)
print (r.get('name'))

#mset(k1='v1', k2='v2')
r.mset(k1='tom',k2='18')
print(r.get('k1'),r.get('k2'))

r.set('testkey','tomhhaha')
res=r.getrange('testkey',0,3) #取子序列
print(res)

r.set('testkey1','tomname')
r.setrange('testkey1',0,'python') #修改字符串内容，从指定字符串索引开始向后替换（新值太长时，则向后添加）
print(r.get('testkey1'))

r.set('age','1')
print(r.incr('age','2'))
r.set('byfloat','1')
print(r.incrbyfloat('byfloat','2.0'))
r.set('age','11')
print(r.decr('age','2'))

r.hset('noset','python','11')
print(r.hget('noset','python'))
# r.hmset('xx', {'k1':'v1', 'k2': 'v2'})
r.hmset('someset',{'k1':'v1','k2':'v2'})
print(r.hmget('someset','k1','k2'))

r.lpush('num','33','44','55')
print(r.lrange('num','0','2'))

r.sadd('sex','11')
print(r.smembers('sex'))























