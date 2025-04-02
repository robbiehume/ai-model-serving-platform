import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
import os

# Hyperparameters
epochs = 1
batch_size = 64
learning_rate = 0.01

# Simple CNN definition
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 16, 3, 1)
        self.fc1 = nn.Linear(10816, 10)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        return x

# Data loaders
train_loader = torch.utils.data.DataLoader(
    datasets.MNIST('./data', train=True, download=True,
                   transform=transforms.ToTensor()),
    batch_size=batch_size, shuffle=True)

# Model, loss, optimizer
model = SimpleCNN()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

# Training loop (1 epoch for demo)
model.train()
for epoch in range(epochs):
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
    print(f'Epoch {epoch+1} complete')

# Save model in expected SageMaker format
os.makedirs('model', exist_ok=True)
torch.save(model.state_dict(), 'model/model.pth')

print('Model saved to model/model.pth')

