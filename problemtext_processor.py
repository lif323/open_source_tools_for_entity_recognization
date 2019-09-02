import pandas as pd
import re
from bs4 import BeautifulSoup
import os

def get_useful_information(src_csv, filter_csv, target_txt):
    """
    使用题目完整信息作为输入,返回题目的可用信息id2text(problem_id -> description), all_text(所有题目的文本)
    src_csv: 源数据位置
    filter_csv: .csv 存贮的位置
    target_txt:所有题目的文本信息
    """
    data = pd.read_csv(src_csv, sep=",")
    # 选取可用的列
    # select available columns.
    useful_data = data.loc[:, ["problem_id", "description"]]

    # process whitespaces, HTML symbols, etc. in text.
    def get_plain_text(input_text):
        # Replace multiple spaces in text with a single space
        input_text = re.sub("\s+", " ", input_text)
        #
        soup = BeautifulSoup(input_text, "html.parser")
        return soup.get_text().strip()
    # save available information in CSV format.
    useful_data.to_csv(filter_csv, sep=",", columns=["problem_id", "description"], index=False)
    # process raw text into plain text.
    with open(target_txt, "w", encoding="utf-8") as fp:
        for row in useful_data.itertuples(index=False):
            raw_text = getattr(row, "description")
            try:
                text = get_plain_text(raw_text)
            except TypeError:
                pass
            fp.write(text + "\n")
if __name__ == "__main__":
    cur_path = os.path.dirname(__file__)
    src_csv = cur_path + "/data/problem.csv"
    filter_csv = cur_path + "/data/useful_data.csv"
    target_txt = cur_path + "/data/problem.txt"
    get_useful_information(src_csv, filter_csv, target_txt)


