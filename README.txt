LecGlyNet

A multimodal deep learning framework integrating pretrained protein language models and glycan structural fingerprints for lectin–glycan interaction prediction
LecGlyNet is a deep learning framework for predicting oligosaccharide–lectin interactions by integrating large-scale pretrained protein language models with glycan structural fingerprints. The framework leverages ESM-2 transformer-based protein embeddings together with glycan subtree descriptors to capture both lectin sequence information and the tree-like structural complexity of glycans derived from CFG glycan microarray datasets.
The framework is designed to generalize across diverse lectin families and previously unseen lectin–glycan pairs while improving biological interpretability through glycan subtree analysis and dynamic thresholding strategies.


Code availability
glycan_encode:Glycan subtree encoding methods.
code/data_class.py:Dynamic thresholding strategy for binding-state classification.
code/feature.py:Dataset preprocessing and multimodal feature construction.
code/glycan_feature.py:Glycan structural feature extraction pipeline.
code/training.py:LecGlyNet model training framework.
code/predict.py:Model inference and lectin–glycan interaction prediction.

How to run LecGlyNet
python predict.py --model_path LecglyNet.pt --csv_path feature.csv --output_path LecglyNet_result.csv

Installation
git clone https://github.com/sgf2001/LecGlyNet.git
cd LecGlyNet

Install dependencies
pip install -r requirements.txt
