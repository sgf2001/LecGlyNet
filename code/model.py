import torch
import torch.nn as nn
import torch.nn.functional as F

class GlycoproteinProphet(nn.Module):
    def __init__(self):
        super(GlycoproteinProphet, self).__init__()
        self.prot_fc1 = nn.Linear(1280, 64)
        self.prot_fc2 = nn.Linear(64, 32)
        self.prot_dropout1 = nn.Dropout(0.3)
        self.prot_dropout2 = nn.Dropout(0.2)
        self.bn_prot1 = nn.BatchNorm1d(64)
        self.bn_prot2 = nn.BatchNorm1d(32)
        self.activation_fn = nn.GELU()
        self.glycan_fc1 = nn.Linear(402, 64)
        self.glycan_lstm = nn.LSTM(128, 64, 2, batch_first=True)
        self.conv1 = nn.Conv1d(128, 64, 1)
        self.glycan_rnn = nn.RNN(64, 64, 2)
        self.glycan_f2 = nn.Linear(402, 32)
        self.bn_glycan1 = nn.BatchNorm1d(32)

        #self.bn_fc1 = nn.Linear(64, 32)
        #medthod1
        self.bn_fc1 = nn.Linear(64, 32)
        self.bn_fc2 = nn.Linear(32, 16)
        self.bn_fc3 = nn.Linear(16, 1)
        self.bn_relu = nn.ReLU()
        # Attention

        self.W_query = nn.Linear(402, 64)
        self.W_key = nn.Linear(402, 64)
        self.W_value = nn.Linear(402, 64)
        self.softmax = nn.Softmax(dim=1)
        self.attention_glycan_fc1 = nn.Linear(466, 32)
        self.softmax = nn.Softmax(dim=1)

    def forward(self, input):
        prot_X_train_tensor = input[:, 0:1280]
        glycan_X_train_tensor = input[:, 1280:1684]
        prot_X_train_tensor = prot_X_train_tensor.float()
        glycan_X_train_tensor = glycan_X_train_tensor.float()
        x = self.prot_fc1(prot_X_train_tensor)
        prot1 = self.bn_prot1(self.prot_dropout1(x))
        prot2 = self.bn_prot2(self.prot_dropout2(self.prot_fc2(prot1)))
        #LSTM
        #glycan1,_= self.glycan_lstm(self.glycan_fc1(glycan_X_train_tensor))
        #glycan_X_train_tensor = glycan_X_train_tensor.transpose(0,1)
        # CNN
        # glycan1 = self.conv1(glycan_X_train_tensor)
        # glycan1 = glycan1.transpose(0, 1)
        # glycan1,_=self.glycan_rnn(glycan1)
        # glycan1 = glycan1.transpose(0, 1)
        # glycan1 = self.conv2(glycan1)
        # glycan1 = glycan1.transpose(0, 1)
        # glycan1 = self.conv1(self.glycan_fc1(glycan_X_train_tensor).transpose(0,1)).transpose(0,1)
        # #glycan2 = self.pool(glycan1).transpose(0,1)
        # #glycan2 = glycan2.view(glycan2.size(0), -1)
        # glycan3 = self.bn_glycan1(self.activation_fn(self.glycan_f2(glycan1)))
        # LSTM+RNN
        # glycan1, _ = self.glycan_lstm(glycan_X_train_tensor)
        # # glycan2,_ = self.glycan_rnn(glycan1)
        #glycan3 = self.bn_glycan1(self.glycan_f2(glycan1))
        # Attention
        query = self.W_query(glycan_X_train_tensor)
        key = self.W_key(glycan_X_train_tensor)
        value = self.W_value(glycan_X_train_tensor)
        key = key.transpose(0, 1)
        scores = torch.matmul(query, key)
        # attention_weights = torch.exp(scores)/torch.sum(scores, dim=1, keepdim=True)
        # attention_weights = self.softmax(scores)
        attention_weights = F.normalize(scores, p=2, dim=1)
        weighted_values = torch.matmul(attention_weights, value)
        #print(weighted_values.shape)
        glycan_feature = torch.cat((glycan_X_train_tensor, weighted_values), dim=1)
        glycan = self.attention_glycan_fc1(glycan_feature)
        #glycan = self.glycan_f2(glycan_X_train_tensor)
        h_n = torch.cat((prot2, glycan), 1)
        #x = F.sigmoid(self.bn_fc1(h_n))
        x = F.sigmoid(self.bn_fc3(self.bn_relu(self.bn_fc2(self.bn_relu(self.bn_fc1(h_n))))))
        #x = nn.functional.softmax(self.bn_fc3(self.bn_relu(self.bn_fc2(self.bn_relu(self.bn_fc1(h_n))))))
        return x
