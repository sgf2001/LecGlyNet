LecGlyNet
LecGlyNet is a deep learning framework for predicting oligosaccharide–lectin interactions.
It integrates transformer-based lectin sequence embeddings (ESM-2) with glycan fingerprint descriptors derived from CFG glycan microarray data. The fused features are processed through a neural network to classify binding and non-binding states. Before training, the model applies a dynamic thresholding method to define binding states, improving discrimination across different lectin–glycan combinations.

Lectins play essential roles in various biological processes, from immune recognition to pathogen invasion, but the complexity of glycan motifs has limited the development of generalizable computational models. LecGlyNet integrates ESM-2–based lectin embeddings with glycan fingerprint descriptors, combined with dynamic thresholding to accurately classify binding states, enabling precise prediction of microarray binding specificity.

The model generalizes across different lectin families and novel lectin–glycan pairs, while interpretability analyses reveal key structural motifs. Molecular simulations further validate the predictions, and benchmarking demonstrates that LecGlyNet is competitive with classical machine learning baselines and the LectinOracle model in both accuracy and interpretability.
LecGlyNet provides an efficient and interpretable framework that facilitates future exploration of oligosaccharide–lectin recognition in health and disease.
