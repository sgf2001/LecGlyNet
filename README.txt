#孙国凤毕业论文数据

dir='/home/wyc/sgf_data/'
#raw_data:从CFG官网下载下来的原始糖微阵列矩阵（1400？843)

######一、change_matirx：从收集到的1400个csv文件提取寡糖序列，凝集素序列以及结合的RFU值的脚本以及相关文件
1../change_matirx/glycan_tree.zip：寡糖描述为指纹结构的脚本
2../change_matirx/glycan_protein_orgiant.csv:没有经历预处理的原始矩阵结果数据
3../change_matirx/glycan_protein_716.csv:经历过预处理的（将相同凝集素序列但不同浓度的凝集素合并，经相同的寡糖序列合并，将错误的寡糖和凝集素序列删除，将寡糖序列中6SO3变成6S)矩阵结果数据

######二、data_class:动态阈值划分凝集素和寡糖结合状态的脚本以及相关文件
1../data_class/data_class.py:动态阈值划分脚本
2../data_class/different_sigma_result：不同阈值下产生的寡糖与凝集素结合状态的二分类结果数据

######三、LecGlyNet_model:数据集创建以及模型搭建、用于调节模型超参数以及进行消融实验
1../LecGlyNet_model/esm-2.py:使用ESM-2模型处理凝集素序列脚本
2.../LecGlyNet_model/esm-2.csv:使用ESM-2模型特征提取凝集素序列
3.../LecGlyNet_model/LecglyNet.ipynb:模型搭建脚本
4../LecGlyNet_model/gly_tree.txt:使用gly_tree脚本统计出的每条寡糖序列的单糖、二糖、三糖的种类
5../LecGlyNet_model/glycan_feature.py:使用指纹结构编码寡糖序列脚本
6../LecGlyNet_model/glycan_finger_feature.csv:使用指纹结构编码寡糖序列的结果
7../LecGlyNet_model/dataset.py:将esm-2凝集素特征和指纹结构编码的寡糖特征融合在一起的脚本


######四、explain_LecGlyNet:解释模型的脚本以及相关文件
1../explain_LecGlyNet/glycan/important_feature.csv:寡糖特征重要性实验结果
2../explain_LecGlyNet/lectin/2n7b_5A.txt:siglec-8与寡糖5A范围内的氨基酸
3../explain_LecGlyNet/lectin/2n7b_8A.txt:siglec-8与寡糖8A范围内的氨基酸
4../explain_LecGlyNet/lectin/siglec-8.pdb:siglec-8凝集素PDB结构
5../explain_LecGlyNet/lectin/Siglec-8_array.xls:siglec-8与寡糖结合的RFU数据
6../explain_LecGlyNet/lectin/siglec-8_sigma12.csv:使用sigma阈值为12划分siglec-8与寡糖的结合状态
7../explain_LecGlyNet/lectin/siglec_8_sequence.csv:原始siglec_8序列以及三种突变后的序列

######五、model_generalization_ability：测试模型泛化能力的脚本以及相关文件
1../model_generalization_ability/lectin.csv:四种凝集素家族糖微阵列数据

######六、model comparies:与其他模型对比的脚本以及相关文件
1../model_comparies/machine_learning/machine_learning.ipynb:使用RandomizedSearchCV工具对四种机器学习优化参数脚本
2../model_comparies/deep_learning/only_glycan:LecGlyNet测试的coff等人提供的20种凝集素的糖微阵列数据
3../model_comparies/deep_learning/Lectinoracle/oligomannose_microarrays:寡甘露糖芯片数据
4../model_comparies/deep_learning/Lectinoracle/LecGLyNet VS Lectinoracle.csv：ACC和Pre两种评价指标下LecGLyNet和Lectinoracle比对结果

######七、MD:分子动力学模拟验证模型的准确性的脚本以及相关文件
1../MD/HSA_siglec_sequence.txt:HSA_siglec序列文件
2../MD/dataset_hsa_siglec.csv:HSA_siglec与数据集中716条寡糖序列特征数据
2../MD/LecGlyNet_HSA_siglec.csv:LecGlyNet模型预测HSA_siglec的结合和非结合寡糖末端基序统计
3../MD/HSA.pdb:HSA_siglecPDB文件
4../MD/HSAsLex.pdb:HSA_siglec晶体结构的寡糖PDB文件
5../MD/docking_glycan:分子对接后的不同5个寡糖序列和凝集素结合的PDB结构
6../MD/MD_result_RMSD:5个寡糖序列100ns模拟结果（待办）
文件名中的代表的糖
glycan1--->Neu5Aca2-3Galb1-3GalNAca
glycan2--->Neu5Aca2-3Galb1-3GlcNAcb
glycan3--->Neu5Aca2-3Galb1-4GlcNAcb
glycan4--->Neu5Aca2-6Galb1-4GlcNAcb
glycan5--->Neu5Aca2-6Galb1-3GlcNAcb



