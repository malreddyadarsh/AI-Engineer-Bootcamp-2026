# Part 2 — Compare Optimizers
# Run the same architecture with:
# Experiment A
# SGD(lr=0.01)
# 
# 
# Experiment B
# SGD(lr=0.01, momentum=0.9)
# 
# 
# Experiment C
# Adam(lr=0.001)
# 
# 
# Experiment D
# AdamW(    lr=0.001,    weight_decay=0.01)
# 
# 


# Experiment A
# SGD(lr=0.01)

# Training Losses is :192.4000
# Validation Losses is :282.5989


# Experiment B              
# SGD(lr=0.01, momentum=0.9)

# Training Losses is :192.4000
# Validation Losses is :282.4998


# Experiment C  
# Adam(lr=0.001)

# Training Losses is :3226.9573
# Validation Losses is :4217.1475


# Experiment D                             
# AdamW(    lr=0.001,    weight_decay=0.01)

# Training Losses is :3024.7456
# Validation Losses is :3775.7920


import numpy as np                                  
import torch                                        
import torch.nn as nn                               
from torch.utils.data import TensorDataset          
                                                    
                                                    
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler    
                                                    
                                                    
                                                    
                                                    
X = np.array([                                      
    [1.5, 62.0, 55.0],                              
    [2.0, 68.0, 60.0],                              
    [2.5, 72.0, 64.0],                              
    [3.0, 76.0, 68.0],                              
    [3.5, 80.0, 72.0],                              
    [4.0, 84.0, 76.0],                              
    [4.5, 88.0, 80.0],                              
    [5.0, 91.0, 84.0],                              
    [5.5, 94.0, 88.0],                              
    [6.0, 96.0, 91.0],                              
    [1.0, 58.0, 50.0],                              
    [2.2, 70.0, 63.0],                              
    [3.2, 78.0, 70.0],                              
    [4.2, 86.0, 77.0],                              
    [5.2, 92.0, 85.0]                               
],dtype=np.float32)                                 
                                                    
                                                    
                                                    
                                                    
y =np.array([                                       
    52.0,                                           
    58.0,                                           
    63.0,                                           
    68.0,                                           
    73.0,                                           
    78.0,                                           
    83.0,                                           
    88.0,                                           
    93.0,                                           
    96.0,                                           
    47.0,                                           
    61.0,                                           
    71.0,                                           
    79.0,                                           
    86.0                                            
],dtype=np.float32)                                 
                                                    
                                                    
# Splitting Data                                    
                                                    
                                                    
X_train,X_temp,y_train,y_temp=train_test_split(     
    X,                                              
    y,                                              
    test_size=0.3,                                  
    random_state=42                                 
)                                                   
                                                    
                                                    
X_val,X_test,y_val,y_test=train_test_split(         
    X_temp,                                         
    y_temp,                                         
    test_size=0.5,                                  
    random_state=42                                 
)                                                   
                                                    
                                                    
# Scale the Data                                    
                                                    
                                                    
scaler=StandardScaler()                             
                                                    
                                                    
X_train=scaler.fit_transform(X_train)               
                                                    
                                                    
X_test=scaler.transform(X_test)                     
                                                    
                                                    
X_val=scaler.transform(X_val)                       
                                                    
                                                    
# Convert to tensors                                
                                                    
                                                    
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
                                                    
                                                    
                                                    
                                                    
class StudentModel(nn.Module):                      
                                                    
                                                    
    def __init__(self):                             
        super().__init__()                          
                                                    
                                                    
        self.layer1=nn.Linear(3,8)                  
                                                    
                                                    
        self.layer2=nn.Linear(8,4)                  
                                                    
                                                    
        self.relu=nn.ReLU()                         
                                                    
                                                    
        self.output=nn.Linear(4,1)                  
                                                    
                                                    
    def forward(self,x):                            
                                                    
        x=self.layer1(x)                            
        x=self.relu(x)                              
                                                    
                                                    
        x=self.layer2(x)                            
        x=self.relu(x)                              
                                                    
                                                    
        x=self.output(x)                            
                                                    
                                                    
        return x                                    
                                                    
                                                    
model=StudentModel()                                
                                                    
                                                    
loss_function=nn.MSELoss()                          
                                                    
                                                    
optimizer=torch.optim.AdamW(                         
    model.parameters(),                             
    lr=0.001,
    weight_decay=0.01                                    
)                                                   
                                                    
                                                    
train_losses=[]                                     
val_losses=[]                                       
                                                    
                                                    
for epoch in range(500):                            
                                                    
                                                    
    # MODEL TRAINING                                
                                                    
                                                    
    model.train()                                   
                                                    
                                                    
    optimizer.zero_grad()                           
                                                    
                                                    
    train_prediction=model(X_train)                 
                                                    
                                                    
    train_loss=loss_function(                       
        train_prediction,y_train                    
    )                                               
                                                    
                                                    
    train_loss.backward()                           
                                                    
                                                    
    optimizer.step()                                
                                                    
                                                    
    train_losses.append(train_loss.item())          
                                                    
                                                    
    # MODEL VALIDATION                              
                                                    
                                                    
    model.eval()                                    
                                                    
                                                    
    with torch.no_grad():                           
                                                    
                                                    
        val_prediction=model(X_val)                 
                                                    
                                                    
        val_loss=loss_function(                     
            val_prediction,y_val                    
        )                                           
                                                    
                                                    
        val_losses.append(val_loss.item())          
                                                    
                                                    
                                                    
                                                    
print(f"Training Losses is :{train_losses[-1]:.4f}")
print(f"Validation Losses is :{val_losses[-1]:.4f}")