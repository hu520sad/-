import pymysql
import pymysql.cursors
import time

class MySqlCommand(object):
    def __init__(self):
        self.host = "mysql"
        self.port = 3306
        self.user = 'root'
        self.password = "123456!"
        self.db = "recruit_db"
        self.table = "shixi"

    def connectionMysql(self):
        attempt = 0
        while attempt < 5:  # 尝试5次连接
            try:
                self.conn = pymysql.connect(
                    host=self.host,
                    db=self.db,
                    user=self.user,
                    password=self.password,
                    port=self.port,
                    charset='utf8',
                    cursorclass=pymysql.cursors.DictCursor
                )
                self.cursor = self.conn.cursor()
                print("链接成功~")
                return self.conn  # 如果连接成功，返回连接对象
            except pymysql.MySQLError as e:
                print(f"连接失败: {e}")
                attempt += 1
                time.sleep(2)  # 等待2秒后重试
        print("无法连接到数据库，请检查数据库服务是否启动")
        return None  # 如果多次连接失败，返回 None

        # 插入数据，插入之前先查询是否存在，如果存在就不再插入


# 插入数据，插入之前先查询是否存在，如果存在就不再插入

    def insertData(self, page_url, data):
        table = "shixi_web"  # 要操作的表格
        # 检查数据是否已存在
        sqlExit = f"SELECT * FROM {table} WHERE page_url = '{page_url}'"
        res = self.cursor.execute(sqlExit)
        if res:
            print("数据已存在", res)
            return 0

        # 数据不存在时，执行插入操作
        try:
            # 拼接列名和值
            cols = ', '.join(data.keys())
            values = ', '.join(f"'{v}'" for v in data.values())

            # print(cols, values)
            # 构建插入 SQL
            sql = f"INSERT INTO {table} ({cols}) VALUES ({values})"

            # 执行插入操作
            try:
                result = self.cursor.execute(sql)
                insert_id = self.conn.insert_id()  # 插入成功后返回的 ID
                self.conn.commit()
                # 判断是否插入成功
                if result:
                    print("插入成功", insert_id)
                    return insert_id
            except pymysql.Error as e:
                # 发生错误时回滚
                self.conn.rollback()
                # 检查是否主键冲突
                if "key 'PRIMARY'" in e.args[1]:
                    print("数据已存在，未插入数据")
                else:
                    print(f"插入数据失败，原因 {e.args[0]}: {e.args[1]}")
        except pymysql.Error as e:
            print(f"数据库错误，原因 {e.args[0]}: {e.args[1]}")

    def QueryData(self, table):
        sql = f"SELECT * FROM {table};"
        try:
            res = self.cursor.execute(sql)  # 执行查询
            # 获取所有结果
            rows = self.cursor.fetchall()  # 返回所有查询结果

            return rows  # 返回查询结果

        except pymysql.Error as e:
            print(f"查询失败，原因 {e.args[0]}: {e.args[1]}")

    def getLastId(self):
        sql = "SELECT max(id) FROM " + self.table
        try:
            self.cursor.execute(sql)
            row = self.cursor.fetchone()  # 获取查询到的第一条数据
            if row[0]:
                return row[0]  # 返回最后一条数据的id
            else:
                return 0  # 如果表格为空就返回0
        except:
            print(sql + ' execute failed.')

    def closeMysql(self):
        self.cursor.close()
        self.conn.close()
