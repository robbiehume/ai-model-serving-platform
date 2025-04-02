import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, 1)
        self.fc1 = nn.Linear(10816, 10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        return x

# SageMaker Entry Point
def model_fn(model_dir):
    model = SimpleCNN()
    model.load_state_dict(torch.load(f'{model_dir}/model.pth'))
    model.eval()
    return model

