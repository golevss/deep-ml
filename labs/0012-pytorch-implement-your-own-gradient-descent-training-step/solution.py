import torch
import torch.nn as nn
import torch.nn.functional as F

def train_step(model, x_batch, y_batch, lr):
    model.train()
    for p in model.parameters():
        if p.grad is not None:
            p.grad.zero_()

    y_pred = model(x_batch)

    loss_val = F.cross_entropy(y_pred, y_batch)

    loss_val.backward()

    with torch.no_grad():
        for p in model.parameters():
            if p.grad is not None:
                p -= lr * p.grad
    
    return loss_val.item()
