import time
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

'''
@Author:Shuangyi Ju
@Time:2024.1.27
'''


student_data = pd.read_csv('D:/研一下/dataAnalyse/sourceFile/student_data.csv')
question_difficulty = pd.read_csv('D:/研一下/dataAnalyse/sourceFile/question_difficulty.csv', encoding='utf-8')


features = []
targets = []
for i, row in student_data.iterrows():
    features.append([float(x) for x in row[1:81]] + [question_difficulty.iloc[int(row[1])]['difficult']])
    targets.extend([float(x) for x in row[81:]])


features = np.array(features, dtype=float)
targets = np.array(targets, dtype=int)


group_size = 20605


num_groups = 21


new_list = []


for i in range(num_groups):
    start = i * group_size
    end = (i + 1) * group_size
    group = targets[start:end]
    new_list.append(group)

X = features[1:, :]


accuracies = []
recalls = []
f1_scores = []


start_time = time.time()


for i in range(20):
    y = new_list[i]


    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    model = DecisionTreeClassifier()


    model.fit(X_train, y_train)


    y_pred = model.predict(X_test)


    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append([i, accuracy])

    report = classification_report(y_test, y_pred, output_dict=True)
    recalls.append(report['1']['recall'])
    f1_scores.append(report['1']['f1-score'])


end_time = time.time()


result_df = pd.DataFrame({'number': range(20), 'accuracy': accuracies, 'recall': recalls, 'f1-score': f1_scores})

# 将结果保存到 CSV 文件
result_df.to_csv('D:/研一下/dataAnalyse/sourceFile/Result/dt_scores.csv', index=False)

print('运行时间：', end_time - start_time, '秒')
print('运行结束')
