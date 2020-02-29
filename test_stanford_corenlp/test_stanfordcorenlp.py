from stanfordcorenlp import StanfordCoreNLP
from pyltp import SentenceSplitter
import os

def get_recognized_entity(src_text, model_path):
    nlp = StanfordCoreNLP(model_path, lang="zh")
    recognized_entity = set()
    with open(src_text, "r", encoding="utf-8") as fp:
        for row in fp.readlines():
            sentence_list = list(SentenceSplitter.split(row))
            for sentence in sentence_list:
                try: # 对于某些符号会发生异常,这里跳过处理
                    word_tag = nlp.ner(sentence)
                    for word, tag in word_tag:
                        if tag != "O":
                            recognized_entity.add(word)
                except BaseException:
                    pass
    return recognized_entity

if __name__ == "__main__":
    data_path = "../data/text.txt"
    model_path = "../model/stanford-corenlp-full-2018-10-05/"
    recognized_entity = get_recognized_entity(data_path, model_path)
    print(recognized_entity)
    os._exit(0)

    # 保存前100个数据
    #recognized_entity = list(recognized_entity)[:100]
    result_path = os.path.dirname(__file__) +"/result.txt"
    with open(result_path, "w") as fp:
        for i in range(10):
            fp.write(str(recognized_entity[i*10: i*10+10]) + "\n")
