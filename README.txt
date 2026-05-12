# LecGlyNet

**LecGlyNet** is a deep learning framework for predicting oligosaccharide–lectin interactions by integrating transformer-based lectin sequence representations with glycan structural fingerprints. The model combines ESM-2 protein embeddings with hierarchical glycan subtree descriptors to capture both sequence-level and structure-level biological information.

---

## Overview

Lectins are key mediators in biological recognition processes, including immune regulation, cell–cell communication, and pathogen adhesion. However, the structural diversity and branching complexity of glycans make computational modeling of lectin–glycan interactions challenging.

LecGlyNet addresses this problem by:

- Encoding lectin sequences using **ESM-2 protein language model embeddings**
- Representing glycans using **hierarchical subtree fingerprint descriptors**
- Fusing multimodal features through a deep neural network
- Predicting lectin–glycan binding vs non-binding states
- Applying a **dynamic thresholding strategy** for robust binding state definition

This design improves both predictive performance and biological interpretability.

---

## Key Features

- Transformer-based protein representation (ESM-2)
- Structural glycan encoding via subtree descriptors
- Multimodal feature fusion network
- Dynamic threshold-based classification
- Generalization to unseen lectin–glycan pairs
- Interpretability of glycan substructures and protein residues

---

## Repository Structure


LecGlyNet/
│
├── glycan_encode/ # Glycan encoding scripts (subtree fingerprinting)
├── code/
│ ├── data_class.py # Dynamic thresholding strategy
│ ├── feature.py # Data preprocessing pipeline
│ ├── glycan_feature.py # Glycan feature extraction
│ ├── training.py # Model training script
│
├── predict.py # Inference script
├── README.md # Documentation


---

## Code Availability

- **glycan_encode**: Oligosaccharide encoding module  
- **code/data_class.py**: Dynamic thresholding implementation  
- **code/feature.py**: Data preprocessing pipeline  
- **code/glycan_feature.py**: Glycan feature extraction  
- **code/training.py**: Model training pipeline  
- **predict.py**: Inference script  

---

## Installation

```bash
git clone https://github.com/your_username/LecGlyNet.git
cd LecGlyNet

pip install -r requirements.txt

Dependencies typically include:

PyTorch
NumPy
Pandas
scikit-learn
fair-esm (ESM-2)
How to Run LecGlyNet
1. Feature Preparation
python code/feature.py
2. Glycan Encoding
python glycan_encode/encode.py
3. Training
python code/training.py
4. Prediction
python predict.py
Model Description

LecGlyNet integrates:

ESM-2 embeddings for lectin sequences
Glycan subtree structural fingerprints
Neural fusion layers for multimodal integration

A dynamic thresholding strategy is used to define binding states across heterogeneous lectin–glycan interactions.

Biological Applications
Glycan-binding protein prediction
Lectin specificity profiling
Host–pathogen interaction analysis
Glyco-immune interaction studies
Reproducibility Note

This repository contains the core implementation of LecGlyNet, including encoding methods, model architecture, and training scripts.

Additional resources such as datasets, molecular simulation files, and auxiliary preprocessing modules may not yet be fully included in this release and will be added in future updates to improve reproducibility.

Citation

If you use this code, please cite:

LecGlyNet: A deep learning framework for predicting lectin–glycan interactions using protein language models and glycan subtree fingerprints
License

To be added.

Contact

For questions or collaboration, please contact the corresponding author.


---

如果你下一步需要，我可以帮你再升级两件很关键的 GitHub 内容：

- 🔥 `requirements.txt`（完全补齐环境）
- 🔥 `Figure 1 model architecture`（论文级架构图说明）
- 🔥 `workflow diagram (glycan → esm → fusion → threshold)`
- 🔥 或:contentReference[oaicite:0]{index=0}

直接说就行。
