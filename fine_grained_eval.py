import pandas as pd
from coarse_grained_eval import model, embed_sentence, cos_similarity

if __name__ == '__main__':
    # sentence1 = 'It was a great day'
    # sentence2 = 'Today was awesome'
    # print(cos_similarity(embed_sentence(sentence1), embed_sentence(sentence2)))

    excel_name = 'plans.xlsx'

    # 读取Excel文件
    df = pd.read_excel(excel_name)  # 可以添加sheet_name参数指定工作表

    # 读取特定列（例如'A'列和'C'列）
    columns = ['oagents_planning_arr', 'human_Planning_arr']  # 替换为你需要的列名或列索引
    selected_columns = df[columns].values.tolist()

    steps_sim = []

    i = 1
    for column in selected_columns:
        print(i)
        i = i + 1
        a_steps = eval(column[0])
        h_steps2 = eval(column[1])
        scores = []
        for a_step in a_steps:
            row_scores = []
            for h_step in h_steps2:
                score = cos_similarity(embed_sentence(a_step), embed_sentence(h_step))
                row_scores.append(score.item())
            scores.append(row_scores)
        steps_sim.append(scores)

    column_name = 'steps_sim'
    df[column_name] = steps_sim

    # 保存回Excel文件
    df.to_excel(excel_name, index=False)
