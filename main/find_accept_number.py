import pandas as pd
import pymysql
import time

'''
@Author:Shuangyi Ju
@Time:2024.1.27
'''
data = pd.read_csv("D:/研一下/dataAnalyse/sourceFile/student_data.csv")
userIds = data.iloc[:, 0].tolist()

conn = pymysql.connect(host='localhost', port=3306, user='root', password='jsyJSY', db='data')
cursor = conn.cursor()


result_dict = {}

start_time = time.time()

for userId in userIds:
    # 构造SQL查询语句
    sql = "SELECT userId, SUM(testNumber) AS total_test_number, SUM(acceptNumber) AS total_accept_number FROM cplus WHERE userId = %s AND problemId BETWEEN 888 AND 987 GROUP BY userId"

    # 执行SQL语句，并传入userId作为参数
    cursor.execute(sql, (userId,))

    # 获取查询结果
    query_result = cursor.fetchone()

    # 计算acceptNumber之和和testNumber之和的比值
    if query_result:
        userId, total_test_number, total_accept_number = query_result
        result_dict[userId] = total_accept_number / total_test_number if total_test_number > 0 else 0


result_df = pd.DataFrame(result_dict.items(), columns=['User ID', 'Ratio'])
result_df.to_csv('accept_test_result.csv', index=False)

# 输出每个userId的acceptNumber之和与testNumber之和的比值
for user_id, ratio in result_dict.items():
    print(f"User ID: {user_id}, Ratio: {ratio}")
end_time = time.time()

print(end_time-start_time)
# 关闭数据库连接
cursor.close()
conn.close()
