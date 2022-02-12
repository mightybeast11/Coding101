# Transformer

- Transformer是一个翻译模型, 目的是将输入语言转化为输出语言. 在此基础上理解encoder和decoder.
- Encoder: 将源语言词汇进行**合理** (multihead self-attention) 的编码1 (word embedding + postitional embedding).
- Decoder: 将目标语言的词汇已经**初步** (masked multihead self-attention, mask的目的是在transformer并行时防止模型提前知道完整的目标语言输出) 编码2. 然后编码1作为query和key, 编码2作为value, 再进行self-attention, 此操作就是在用源语言的词汇 (query, key) 匹配目标语言的词汇 (value), 最终的输出就是目标语言了. 
- 要训练的transformer模型参数主要是各个self-attention block中将embeddings转化为 (query, key, value) 的矩阵, 和各个linear layer (feed forward layer) 矩阵.