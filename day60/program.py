import torch
import torch.nn as nn
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

X = np.array([
    [2,55,40], [3,60,45], [4,65,50], [5,70,58],
    [6,75,62], [7,80,70], [8,85,75], [9,90,82],
    [10,95,88], [3,58,43], [4,68,53], [6,78,66],
    [7,83,72], [8,88,78], [9,92,85], [5,72,60]
], dtype=np.float32)

y = np.array([
    42,47,55,62,68,75,81,87,
    94,45,57,71,77,83,91,64
], dtype=np.float32)

# Splitting Data

X_train,X_temp,y_train,y_temp=train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)

X_val,X_test,y_val,y_test=train_test_split(
    X_temp,
    y_temp,
    test_size=0.50,
    random_state=42
)

# Scaling

scaler=StandardScaler()

X_train=scaler.fit_transform(X_train)
X_val=scaler.transform(X_val)
X_test=scaler.transform(X_test)

# Converting to Tensors

X_train=torch.tensor(
    X_train,
    dtype=torch.float32
)

X_val=torch.tensor(
    X_val,
    dtype=torch.float32
)

X_test=torch.tensor(
    X_test,
    dtype=torch.float32
)

y_train=torch.tensor(
    y_train,
    dtype=torch.float32
).reshape(-1,1)

y_val=torch.tensor(
    y_val,
    dtype=torch.float32
).reshape(-1,1)

y_test=torch.tensor(
    y_test,
    dtype=torch.float32
).reshape(-1,1)

class ResidualBlock(nn.Module):

    def __init__(self,in_features,out_features):

        super().__init__()

        self.layer1=nn.Linear(in_features,out_features)
        self.norm1=nn.LayerNorm(out_features)

        self.layer2=nn.Linear(out_features,out_features)
        self.norm2=nn.LayerNorm(out_features)

        self.relu=nn.ReLU()

        if in_features==out_features:
            self.shortcut=nn.Identity()
        else:
            self.shortcut=nn.Linear(
                in_features,out_features
            )

    def forward(self,x):

        residual=self.shortcut(x)

        out=self.layer1(x)
        out=self.norm1(out)
        out=self.relu(out)

        out=self.layer2(out)
        out=self.norm2(out)

        out= out + residual

        out=self.relu(out)

        return out

class PlainStudentRegressor(nn.Module):

    def __init__(self):

        super().__init__()

        self.network=nn.Sequential(
            nn.Linear(3,32),
            nn.ReLU(),
            nn.Linear(32,32),
            nn.ReLU(),
            nn.Linear(32,32),
            nn.ReLU(),
            nn.Linear(32,1)
        )

    def forward(self,x):

        return self.network(x)


# Building Residual Network

class ResidualStudentRegressor(nn.Module):

    def __init__(self):
        super().__init__()

        self.input_layer=nn.Linear(3,32)

        self.block1=ResidualBlock(32,32)
        self.block2=ResidualBlock(32,32)
        self.block3=ResidualBlock(32,32)

        self.output_layer=nn.Linear(32,1)

    def forward(self,x):

        x=self.input_layer(x)

        x=self.block1(x)
        x=self.block2(x)
        x=self.block3(x)

        return self.output_layer(x)


def train_model(model,epochs=500,patience=40):

    loss_function=nn.MSELoss()

    optimizer=torch.optim.AdamW(
        model.parameters(),
        lr=0.001,
        weight_decay=0.001
    )

    best_val_loss = float("inf")
    best_state = None
    counter = 0

    train_losses = []
    val_losses = []

    for epoch in range(epochs):

        model.train()

        optimizer.zero_grad()

        train_pred=model(X_train)

        train_loss=loss_function(train_pred,y_train)

        train_loss.backward()

        torch.nn.utils.clip_grad_norm_(
            model.parameters(), max_norm=1.0
        )

        optimizer.step()

        model.eval()

        with torch.no_grad():

            val_pred=model(X_val)

            val_loss=loss_function(val_pred,y_val).item()

        train_losses.append(train_loss.item())
        val_losses.append(val_loss)

        if val_loss < best_val_loss - 1e-6:
            best_val_loss = val_loss
            best_state = {
                key: value.detach().clone()
                for key, value in model.state_dict().items()
            }
            counter = 0
        else:
            counter += 1

        if epoch % 50 == 0:
            print(
                f"Epoch: {epoch} | "
                f"Train: {train_loss.item():.4f} | "
                f"Val: {val_loss:.4f}"
            )

        if counter >= patience:
            print("Early stopping at epoch:", epoch)
            break

    if best_state is not None:
        model.load_state_dict(best_state)

    return model, train_losses, val_losses


torch.manual_seed(42)

plain_model = PlainStudentRegressor()

plain_model, plain_train, plain_val = train_model(
    plain_model
)

torch.manual_seed(42)

residual_model = ResidualStudentRegressor()

residual_model, residual_train, residual_val = train_model(
    residual_model
)

import matplotlib.pyplot as plt

plt.plot(plain_train, label="Plain Train")
plt.plot(plain_val, label="Plain Validation")

plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.title("Plain Network")
plt.legend()
plt.show()

plt.plot(residual_train, label="Residual Train")
plt.plot(residual_val, label="Residual Validation")

plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.title("Residual Network")
plt.legend()
plt.show()


def evaluate_model(model):

    model.eval()

    with torch.no_grad():
        predictions = model(X_test).numpy().flatten()

    actual = y_test.numpy().flatten()

    mae = mean_absolute_error(actual, predictions)
    mse = mean_squared_error(actual, predictions)
    rmse = np.sqrt(mse)
    r2 = r2_score(actual, predictions)

    print(f"MAE:  {mae:.4f}")
    print(f"MSE:  {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"R²:   {r2:.4f}")

print("Plain network:")
evaluate_model(plain_model)

print("\nResidual network:")
evaluate_model(residual_model)