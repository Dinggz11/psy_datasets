import pandas as pd

'''
@Author:Shuangyi Ju
@Time:2024.1.27
'''

dropout_data = pd.read_csv("D:/研一下/dataAnalyse/sourceFile/dropout_prediction.csv")


dropout_data['Dropout_Risk'] = 'Low'
dropout_data.loc[(dropout_data['Ratio'] < 0.5) & (dropout_data['accuracy'] < 0.5), 'Dropout_Risk'] = 'High'
'''
dropout_data.to_csv('D:/研一下/dataAnalyse/sourceFile/dropout_prediction.csv', index=False)
'''

# 统计 'High' 和 'Low' 的人数
dropout_count = dropout_data['Dropout_Risk'].value_counts()

print(dropout_count)