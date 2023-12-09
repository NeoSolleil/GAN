import torch
import torch.nn as nn

# Generatorの定義
class Generator(nn.Module):
    def __init__(self, input_size, output_size):
        super(Generator, self).__init__()
        self.flatten_size = input_size[1] * input_size[2]
        self.fc = nn.Linear(self.flatten_size, output_size)
        self.tanh = nn.Tanh()

    def forward(self, x):
        # 入力を平坦化
        x = x.view(-1, self.flatten_size)
        # 全結合層の適用
        x = self.fc(x)
        # tanh関数の適用
        x = self.tanh(x)
        return x

# Generatorのインスタンス化
input_size = torch.Size([1, 336, 768])
output_size = 1  # スカラー値を生成するための出力サイズ
generator = Generator(input_size, output_size)

# ダミーの入力データの生成
dummy_input = torch.randn(1, *input_size)

# フォワードパスの実行
output = generator(dummy_input)

# 結果の表示
print("入力サイズ:", input_size)
print("出力サイズ:", output_size)
print("出力値:", output.item())
