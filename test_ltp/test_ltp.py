import os
from pyltp import SentenceSplitter, Segmentor,Postagger, NamedEntityRecognizer

def deal_one_sentence(line, segmentor, postagger, recognizer):
    # 分词
    words = segmentor.segment(line)
    # 词性标注
    postags = postagger.postag(words)
    # 命名实体识别
    netags = recognizer.recognize(words, postags)
    return list(words), list(netags)

# 加载模型
def load_model(model_dir=""):
    # 分词
    cws_model_path = os.path.join(model_dir, "cws.model")
    segmentor = Segmentor()
    segmentor.load(cws_model_path)
    # 词性标注
    pos_model_path = os.path.join(model_dir, "pos.model")
    postagger = Postagger()
    postagger.load(pos_model_path)
    # 实体识别
    ner_model_path = os.path.join(model_dir, "ner.model")
    recognizer = NamedEntityRecognizer()
    recognizer.load(ner_model_path)
    return segmentor, postagger, recognizer

# 释放模型
def release_model(segmentor, postagger, recognizer):
    segmentor.release()
    postagger.release()
    recognizer.release()

def get_recognized_data(src_text="", model_dir=""):
    recognized_entity = set()
    segmentor, postagger, recognizer = load_model(model_dir)
    with open(src_text, "r", encoding="utf-8") as fp:
        for row in fp.readlines():
            sentence_list = list(SentenceSplitter.split(row))
            for sentence in sentence_list:
                words, netags = deal_one_sentence(sentence, segmentor, postagger, recognizer)
                for word, tag in zip(words, netags):
                    if tag != "o":
                        recognized_entity.add(word)
    return recognized_entity

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__) + "/../data/problem.txt")
    recognized_entity = get_recognized_data(src_text=data_path, model_dir=os.path.dirname(__file__) + "/model/ltp_data_v3.4.0")
    print(recognized_entity)
    