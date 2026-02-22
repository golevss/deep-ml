import torch
import torch.nn as nn
import torch.optim as optim
import math


def train_model(model, X_train, y_train, X_val, y_val, epochs, batch_size, lr):
    history = []
    optimizer = optim.Adam(model.parameters(), lr=lr)
    loss_f = nn.CrossEntropyLoss()

    for epoch in range(epochs):
        model.train()
        order = torch.randperm(len(X_train))

        train_loss_sum = 0.0
        num_batches = 0

        for start in range(0, len(X_train), batch_size):
            optimizer.zero_grad()

            batch_idx = order[start:start + batch_size]
            x_batch = X_train[batch_idx]
            y_batch = y_train[batch_idx]

            y_pred = model(x_batch)
            loss = loss_f(y_pred, y_batch)
            loss.backward()

            optimizer.step()

            train_loss_sum += loss.item()
            num_batches += 1

        model.eval()
        with torch.no_grad():
            y_pred = model(X_val)
            val_loss = loss_f(y_pred, y_val).item()
            val_acc = (y_pred.argmax(dim=1) == y_val).float().mean().item()

        history.append({
            "epoch": epoch + 1,
            "train_loss": train_loss_sum / num_batches,
            "val_loss": val_loss,
            "val_accuracy": val_acc
        })

    return history