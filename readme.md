# 源数据处理
这里所有的工具所需要的数据均使用相同的文本处理: `problemtext_processor.py`.
# ltp
[github仓库](https://github.com/HIT-SCIR/ltp)是由哈工大提供的开源工具.需要安装`pyltp`,下载模型
## 技术原理
论文: Wanxiang Che, Zhenghua Li, Ting Liu. LTP: A Chinese Language Technology Platform. In Proceedings of the Coling 2010:Demonstrations. 2010.08, pp13-16, Beijing, China.
- **模型**: `maximum entropy model `(A Maximum Entropy Approach to Natural Language Processing)
Berger等人在1996提出的模型.
- **语料**: 主要使用的人们日常的语料
## 结构
- `test_ltp.py`用于测试
- `test_ltp/result.txt`存放了部分测试结果
## 测试结果
`ltp`提供了对人名,地名,机构名这些实体类型识别的支持.[API](https://pyltp.readthedocs.io/zh_CN/latest/api.html#id5)<br>
从结果来看,识别实体为人名,地名,国家名,无法正确识别所需实体.
# Jiagu
[github仓库](https://github.com/ownthink/Jiagu).这一个名叫 思知(ownthink) 的开源项目,
## 结构
- `test_jiagu.py` 用于测试
- `test_jiagu/result.txt` 存放了对于OJ文本处理的部分结果
- `test_jiagu/result_sample.txt`存放了对于纯文本的政治新闻数据的处理结果
## 技术原理
没有找到具体的论文,通过查看源码,使用的是`BILSTM+CRF`的方式
## 测试结果
与`ltp`相同,Jiagu仅仅识别人名,地名,机构名,并且`Jiagu`对于中英混杂的数据处理不好(通过对比`result_sample.txt`,`result.txt`)
`Jiagu`所使用的标注方法:
```
B-PER,I-PER 人名
B-LOC,I-LOC 地名
B-ORG,I-ORG 机构名
B-XX代表实体名开始
I-XX表示实体名中间的,末尾的词语
```
# coreNLP
[standfordcorenlp](https://github.com/stanfordnlp/CoreNLP)使用斯坦福大学开发的nlp工具,这里只是用了命名实体识别工具,相比较与之前的工具,这个工具可以是识别日期,时间等.
## 技术原理
论文:Manning, Christopher D., Mihai Surdeanu, John Bauer, Jenny Finkel, Steven J. Bethard, and David McClosky. 2014. The Stanford CoreNLP Natural Language Processing Toolkit In Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations, pp. 55-60.
- **模型**: 主要使用的是CRF.
- **语料**: CoNLL, ACE, MUC, ERE
## 结构
- `test_stanfordcorenlp.py`用于测试
- `test_stanford_corenlp/result.txt`保存了部分识别结果
## 测试结果
corenlp相比于前两个工具,**效果最好**,识别更大范围的实体,但是也不能识别目标实体.