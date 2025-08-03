import pandas as pd

# 读取Excel文件
df = pd.read_excel('plans.xlsx')  # 可以添加sheet_name参数指定工作表

# 读取特定列（例如'A'列和'C'列）
columns = ['oagents_planning', 'human_Planning']  # 替换为你需要的列名或列索引
selected_columns = df[columns].values.tolist()

