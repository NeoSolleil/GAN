



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




lp='sa fwds f fsdfs f sdfs dfsf  fs df sdfsev dry d'
pl='ko'
aq=gen_V(lp,pl)
print(aq)
print(aq.size())
print('')
class generator(nn.Module):
    def __init__(self):
        super(generator, self).__init__()
        print(self)
        #print(self.fc1)
        self.fc1 = nn.Linear(336, 768)
        self.fc2 = nn.Linear(768, 2048)
        self.fc3 = nn.Linear(2048, 784)
        #self.activation = nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)
        x = self.activation(self.fc2(x))
        x = self.fc3(x)
        x = x.view(-1, 1, 28, 28)
        return nn.Tanh()(x)

Generator = generator()
print(Generator)

az=Generator(aq)











#