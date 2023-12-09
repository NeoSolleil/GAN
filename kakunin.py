
import time

# 計測開始時刻
start_time = time.time()

import torch
import torch.nn as nn
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForMaskedLM

from transformers import XLMRobertaModel, XLMRobertaTokenizer

model_name = "xlm-roberta-base"
model = XLMRobertaModel.from_pretrained(model_name)
tokenizer = XLMRobertaTokenizer.from_pretrained(model_name)


text = "私はケーキを食べます"
inputs = tokenizer(text, return_tensors="pt")

outputs = model(**inputs)

sentence_vector = outputs.last_hidden_state#.mean(dim=1)  # 例: 平均プーリングを使用して文章ベクトルを得る

#print(sentence_vector)
#print(sentence_vector.size())




with open('/Users/fujidai/GGAANN/WMT22_data/cs-en/cs-en_src.txt', 'r') as f:#
    left = f.read()
left_lines = left.splitlines()
#left_lines.pop()
   #2383690
print(len(left_lines))

with open('/Users/fujidai/GGAANN/WMT22_data/cs-en/cs-en_hyp.txt', 'r') as f:#
    senter = f.read()
senter_lines = senter.splitlines()
#senter_lines.pop()




aq=[]
for i in range(len(left_lines)):
    inputs_left = tokenizer(left_lines[i], return_tensors="pt")
    inputs_senter = tokenizer(senter_lines[i], return_tensors="pt")

    outputs_left = model(**inputs_left)
    outputs_senter = model(**inputs_senter)

    sentence_vector_left = outputs_left.last_hidden_state
    sentence_vector_senter = outputs_senter.last_hidden_state

    pooled_tensor = torch.cat([sentence_vector_left, sentence_vector_senter], dim=1)
    #print(pooled_tensor.size())

    '''

    padding_needed = 336 - pooled_tensor.size(1)
    padded_tensor = torch.nn.functional.pad(pooled_tensor, (0, 0, 0, padding_needed))
    print("元のサイズ:", pooled_tensor.size())
    print("パディング後のサイズ:", padded_tensor.size())
    '''

    aq.append(pooled_tensor.size(1))

    #if i ==10:
        #break



print(max(aq))




import torch

# オリジナルのテンソルとして original_tensor を仮定します
original_tensor = torch.randn(1, 16, 768)

# パディングが必要な量を計算します
padding_needed = 336 - original_tensor.size(1)

# torch.nn.functional.pad を使用してテンソルをパディングします
padded_tensor = torch.nn.functional.pad(original_tensor, (0, 0, 0, padding_needed))

print("元のサイズ:", original_tensor.size())
print("パディング後のサイズ:", padded_tensor.size())



end_time = time.time()

# 経過時間を計算
elapsed_time = end_time - start_time

# 経過時間を表示
print("プログラムの実行時間:", elapsed_time, "秒")











#