import torch
from torch import nn

torch.manual_seed(20260907)
x = torch.linspace(-1, 1, 101).reshape(-1, 1)
y = 3 * x - 1

model = nn.Linear(1, 1)
loss_fn = nn.MSELoss()
opt = torch.optim.SGD(model.parameters(), lr=0.1)

for _ in range(200):
    pred = model(x)
    loss = loss_fn(pred, y)
    # TODO: 清空梯度、反向传播、更新参数
    opt.zero_grad()
    loss.backward()
    opt.step()

# TODO: 进入评估模式并在no_grad中打印最终损失、weight 和 bias
model.eval()
with torch.no_grad():
    pred_final = model(x)
    loss_final = loss_fn(pred_final, y)
    w = model.weight.item()
    b = model.bias.item()
    print(f"final loss: {loss_final:.8f}")
    print(f"weight: {w:.4f}")
    print(f"bias: {b:.4f}")
