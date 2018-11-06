import pymysql

db=pymysql.connect('xxx.xxx.xxx.xxx','username','passwd','dbname ')#创建链接

def DbGet():
    #sql = "select username, password from users where user='%s' and pass='%s'" % (username, password)
    cursor = db.cursor()#获取光标
    cursor.execute("select *from tenant_info") # 执行sql语句
    row_1 = cursor.fetchone()
    print('row_1:',row_1)
    #cursor.scroll(-1, mode='relative')  # 相对当前位置移动
    cursor.scroll(0, mode='absolute')  # 相对绝对位置移动
    row_n=cursor.fetchmany(3) #获取前n行数据
    print('row_n:',row_n)
    row_all=cursor.fetchall()
    print('row_all:',row_all)
    #db.close() ## 关闭数据库连接
DbGet()


def DbInsert():
    cursor = db.cursor()
    sql = """INSERT INTO tenant_info(userid,
             appid, appkey, create_time, status)
             VALUES ("test8", 10008, "xxxxxxxxxxxxxxx", 1541486894, "1")"""
    try:
        cursor.execute(sql)
        db.commit()# 提交到数据库执行
    except:
        db.rollback()# 如果发生错误则回滚
    #db.close()
DbInsert()


def DbUpdate(userid):
    cursor = db.cursor()
    sql = "UPDATE tenant_info SET appid = appid + 1 WHERE userid = '%s'" % (userid)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    #db.close()
DbUpdate('test8')


def DbDel(userid):
    cursor=db.cursor()
    sql = "DELETE FROM tenant_info WHERE userid = '%s'" % (userid)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    #db.close()
DbDel('test8')











