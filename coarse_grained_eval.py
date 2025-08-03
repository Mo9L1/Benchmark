from sentence_transformers import SentenceTransformer, util
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_text_similarity(text1, text2):
    """
    使用TF-IDF算法计算两段英文文本的余弦相似度

    参数:
        text1 (str): 第一段文本
        text2 (str): 第二段文本

    返回:
        float: 两段文本的相似度得分(0-1之间)
    """
    # 创建TF-IDF向量器
    vectorizer = TfidfVectorizer()

    # 将两段文本组合成一个列表
    corpus = [text1, text2]

    # 计算TF-IDF矩阵
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # 计算余弦相似度
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    return similarity[0][0]

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
        # score = cos_similarity(embed_sentence(sentence1), embed_sentence(sentence2))
        score = calculate_text_similarity(sentence1, sentence2)
        scores.append(score)

    # column_name = 'bert_score'
    column_name = 'TF-IDF_score'
    df[column_name] = scores

    # 保存回Excel文件
    df.to_excel(excel_name, index=False)