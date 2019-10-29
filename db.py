import pymysql
import time


class DataBaseClient:
    def __init__(self, **kwargs):
        """
        数据库操作类；
        Attr:
            __host: 数据库地址，默认使用“localhost”
            __port: 数据库端口，默认使用“3306”
            __user: 数据库用户名，未设置时为“None”
            __password: 数据库连接密码，未设置时为“None”
            __db_name: 数据库名字，未设置时为“None”
            __charset: 数据库使用的字符集，默认为“utf-8”
        :param kwargs:
        """
        self.db = None
        self.config = None
        self.cursor = None
        try:
            self.__host = kwargs["host"]
        except KeyError:
            self.__host = "localhost"
        try:
            self.__port = int(kwargs["port"])
        except KeyError:
            self.__port = 3306
        try:
            self.__user = kwargs["user"]
        except KeyError:
            self.__user = None
        try:
            self.__password = kwargs["password"]
        except KeyError:
            self.__password = None
        try:
            self.__db_name = kwargs["db_name"]
        except KeyError:
            self.__db_name = None
        try:
            self.__charset = kwargs["charset"]
        except KeyError:
            self.__charset = "utf-8"

    def connection(self):
        """
        创建数据库连接；
        :return: None
        """
        self.db = pymysql.connect(host=self.__host, user=self.__user, password=self.__password,
                                  database=self.__db_name, charset=self.__charset,
                                  port=self.__port)

    def execute(self, sql):
        """
        执行指定的sql语句；
        :param sql: sql语句
        :return: 如果sql语句有返回结果，则返回相应的结果；否则返回“None”
        """
        self.cursor = self.db.cursor()
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as error:
            self.db.rollback()
            self.cursor.close()
            print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + ": " + str(error))
            return None
        result = self.cursor.fetchall()
        self.cursor.close()
        return result

    def close(self):
        """
        关闭数据库连接；
        :return: None
        """
        self.db.close()

