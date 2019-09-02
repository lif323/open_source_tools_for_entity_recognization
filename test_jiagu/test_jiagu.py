import jiagu
import os
################
#Jiagu
#结果不是很好
###############
def extract_named_entity(tag_lsit, text_list):
        named_entity = set()
        now = ""
        for tag, word in zip(tag_lsit, text_list):
                for tag_x, word_x in zip(list(tag), list(word)):
                        if tag_x == "O":
                                if now != "":
                                        named_entity.add(now)
                                        now = ""
                        else:
                                now += word_x
        if now != "":
                named_entity.add(now)
        return named_entity
                        
def test_jiagu(src_path):
    text_list = []
    with open(src_path, "r", encoding="utf-8") as fp:
        for line in fp.readlines():
            text_list.append(line.strip("\n"))
    tag_list = jiagu.ner(text_list, input="batch")
    named_entity = extract_named_entity(tag_list, text_list)
    return named_entity

if __name__ == "__main__":
        # 处理OJ题目文本
        data_path = os.path.dirname(__file__) + "/../data/problem.txt"
        
        word_list = test_jiagu(data_path)
        word_list = list(word_list)

        # 保存前100个
        recognized_entity = list(word_list)[:100]
        result_path = os.path.dirname(__file__) +"/result.txt"
        with open(result_path, "w") as fp:
                for i in range(10):
                        fp.write(str(recognized_entity[i: i + 10]) + "\n")


        # 处理纯中文文本 这里为了比较纯中文,中英混杂的不同情况下,处理结果的差异
        sample_path = os.path.dirname(__file__) + "/../data/sample_only_chinese.txt"
        word_list = test_jiagu(sample_path)
        # 保存前100个
        recognized_entity = list(word_list)[:100]
        result_path = os.path.dirname(__file__) +"/result_sample.txt"
        with open(result_path, "w") as fp:
                for i in range(10):
                        fp.write(str(recognized_entity[i: i + 10]) + "\n")

        
        