


import torch.nn as nn
import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModelForMaskedLM
from transformers import XLMRobertaModel, XLMRobertaTokenizer


tokenizer = XLMRobertaTokenizer.from_pretrained('xlm-roberta-base')
model = XLMRobertaModel.from_pretrained("xlm-roberta-base")

# ジェネレータへの入力前の処理
def gen_V(sentence1,sentence2):
    encoded_input1 = tokenizer(sentence1, return_tensors='pt')
    encoded_input2 = tokenizer(sentence2, return_tensors='pt')
    output1 = model(**encoded_input1)
    output2 = model(**encoded_input2)
    sentence_vector_1 = output1.last_hidden_state
    sentence_vector_2 = output2.last_hidden_state

    # テンソルを連結する
    #pooled_tensor = torch.cat([tensor1, tensor2], dim=1)
    pooled_tensor = torch.cat([sentence_vector_1, sentence_vector_2], dim=1)
    padding_needed = 336 - pooled_tensor.size(1)#336が一番大きいサイズになっている
    padded_tensor = torch.nn.functional.pad(pooled_tensor, (0, 0, 0, padding_needed))

    return padded_tensor


# Generatorの定義
class Generator(nn.Module):
    def __init__(self, input_size):#, output_size):
        super(Generator, self).__init__()
        #self.flatten_size = input_size[1] * input_size[2]
        #print(self.flatten_size)#258048
        #print('')
        self.fc = nn.Linear(input_size, output_size)
        print(self.fc)


    def forward(self, x):
        print(x)
        print(aq.size())


        # 全結合層の適用
        x = self.fc(x)
        # tanh関数の適用
        x = F.softmax(x, dim=1)
        return x

# Generatorのインスタンスを作成

input_size = torch.Size([1, 336, 768])
output_size = 1  # スカラー値を生成するための出力サイズ
generator = Generator(input_size, output_size)


lp='sa fwds f fsdfs f sdfs dfsf  fs df sdfsev dry d'
pl='ko'
aq=gen_V(lp,pl)
#print('aq')
#print(aq)
#print(aq.size())
#print(generator)
#generator = Generator(output_size=1)
output = generator(aq)#Generatorの生成するもの


# Generatorによる生成


# モデルの表示


# 入力と出力のサイズを表示
print(f"Input size: {aq.size()}")


print(output)