# 源数据处理
这里所有的工具所需要的数据均使用相同的文本处理: `problemtext_processor.py`.
# ltp
[github仓库](https://github.com/HIT-SCIR/ltp)是由哈工大提供的开源工具.需要安装`pyltp`,下载模型
## 结构
- `test_ltp.py`用于测试
- `result.txt`存放了部分测试结果
## 测试结果
`ltp`提供了对人名,地名,机构名这些实体类型识别的支持.[API](https://pyltp.readthedocs.io/zh_CN/latest/api.html#id5)<br>
从结果来看,识别实体为人名,地名,国家名,无法正确识别所需实体.
# Jiagu
[github仓库](https://github.com/ownthink/Jiagu).这一个名叫 思知(ownthink) 的开源项目,
## 结构
- `test_jiagu.py` 用于测试
- `result.txt` 存放了对于OJ文本处理的部分结果
- `result_sample.txt`存放了对于纯文本的政治新闻数据的处理结果
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