from sentence_transformers import SentenceTransformer, util
import pandas as pd

model = SentenceTransformer('bert-base-nli-mean-tokens')

def embed_sentence(sentence):
    return model.encode(sentence)

def cos_similarity(a, b):
    return util.cos_sim(a, b)

if __name__ == '__main__':
    # sentence1 = 'It was a great day'
    # sentence2 = 'Today was awesome'
    # print(cos_similarity(embed_sentence(sentence1), embed_sentence(sentence2)))

    excel_name = 'plans.xlsx'

    # 读取Excel文件
    df = pd.read_excel(excel_name)  # 可以添加sheet_name参数指定工作表

    # 读取特定列（例如'A'列和'C'列）
    columns = ['oagents_planning', 'human_Planning']  # 替换为你需要的列名或列索引
    selected_columns = df[columns].values.tolist()

    scores = []

    for column in selected_columns:
        sentence1 = column[0]
        sentence2 = column[1]
        score = cos_similarity(embed_sentence(sentence1), embed_sentence(sentence2))
        scores.append(score)

    column_name = 'bert_score'
    df[column_name] = scores

    # 保存回Excel文件
    df.to_excel(excel_name, index=False)