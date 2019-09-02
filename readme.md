# ltp
[github仓库](https://github.com/HIT-SCIR/ltp)是由哈工大提供的开源工具.需要安装`pyltp`,下载模型
## 结构
- `problemtext_processor.py` 用于处理文本.
- `test_ltp.py`用于测试
- `result.txt`存放了部分测试结果
## 测试结果
`ltp`提供了对人名,地名,机构名这些实体类型识别的支持.[API](https://pyltp.readthedocs.io/zh_CN/latest/api.html#id5)<br>
从结果来看,可以识别部分目标实体`公倍数, 数组`等.