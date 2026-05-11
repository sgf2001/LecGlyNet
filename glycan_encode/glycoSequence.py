import sys
from sugardir import createNodeFun as nodebuilt
from sugardir import iterate_tree
from sugardir import outputfuc as output




label = []
num = {}
depth = 0
num[f'num{depth}'] = 0
glycan = ['Gal', 'Glc', 'Glu', 'Man', 'HexA', 'Xyl', 'Ara', 'Fuc', 'Rha', 'GlcA', 'IdoA', 'GalNAc', 'GlcNAc',
          'GlcNS', 'Neu5Ac', 'Neu5Gc', 'KDN', 'KDO', 'Neu5,9Ac2','GlcN(Gc)']
extra = ["Sp",'Gly','T','LVaNKT','MDPlys','6AA','N','Asn','(OCH2CH2)6NH2','NLTAVL','MDPLys','LVANKT']
with open(r"./data/new_glycan_0916.csv", "r") as sugarfile:
    for sugar in sugarfile:
        testsugar = sugar.replace('"', "").strip('\n')
        print(testsugar)
        sugarnodelist = []
        count = 0
        for char in testsugar:
            if char == ")":
                count += 1
            elif char == "(":
                count -= 1
        if count != 0:
            print("error")
        glycan_list = testsugar.split('-')
        if 'Sp' in glycan_list[-1]:
            glycan_list[-1] = 'Sp'
        for i in extra:
            if i == glycan_list[-1]:
                testsugar = '-'.join(glycan_list[0:-1])

        index = testsugar[-3:len(testsugar)]
        if index == 'Rha':
            testsugar = "-0" + testsugar + "c0"  
        elif index == 'Ara':
            testsugar = "-0" + testsugar + "c0"  
        elif testsugar[-1] == "a" or testsugar[-1] == "b":
            testsugar = "-0" + testsugar + "0"
        else:
            testsugar = "-0" + testsugar + "c0"


        for s in testsugar[::-1]:
            label.append(s)
            if s == "-":
                sugarlab = label[:-1][::-1]
                sugarlab = "".join(sugarlab)
                # (Neu5Aca2-3Galb1-3)((Neu5Aca2-3Galb1-4(Fuca1-3))GlcNAcb1-6)GalNAca1-4Glc
                if "(" not in sugarlab:
                    sugarlabreplace = sugarlab.replace(")", "").replace("(", "")
                    monosaccharide = ''
                    for i in sugarlabreplace[0:-2][::-1]: 
                        monosaccharide = i + monosaccharide  
                        if monosaccharide in glycan:  
                            sugarlabvalue = monosaccharide.lower()
                            monosaccharide = ''
                    nodebuilt.createNode(sugarlabreplace, sugarlabvalue, sugarnodelist, num, depth)

                    for char in sugarlab[::-1]:  
                        if char == ")":
                            depth += 1  #
                            num[f'num{depth}'] = 0 
                    label = []  
                else:
                    tempchild = str(sugarlab[0])  
                    sugarlab1 = "0" + sugarlab[1:]
                    sugarlabreplace = sugarlab1.replace(")", "").replace("(", "")
                    monosaccharide = ''
                    for i in sugarlabreplace[0:-2][::-1]:  
                        monosaccharide = i + monosaccharide  
                        if monosaccharide in glycan:  
                            sugarlabvalue = monosaccharide.lower()
                            monosaccharide = ''
                    nodebuilt.createNode(sugarlabreplace, sugarlabvalue, sugarnodelist, num, depth)
                    for char in sugarlab[::-1]:
                        if char == "(":
                            while num[f'num{depth}'] > 0:  
                                sugarnodelist.pop()
                                num[f'num{depth}'] -= 1  
                            depth -= 1  
                        elif char == ")":  
                            depth += 1
                            num[f'num{depth}'] = 0
                        else:
                            continue
                    if sugarnodelist[-1].childflagnum == 0:  
                        for chidrenkey, chidrenvalue in sugarnodelist[-1].childrenlistdic.items():  
                            if tempchild == chidrenkey and len(chidrenvalue) != 0:  
                                print("error", "".join(label)[::-1])
                                sys.exit()
                            elif tempchild == chidrenkey and len(chidrenvalue) == 0:  
                                chidrenvalue.append(tempchild)  
                                sugarnodelist[-1].childflagnum += 1  
                    label = []
        singlelist = []
        doublelist = []
        triplelist = []
        NodeGrp = []

        root = sugarnodelist[0] 
        iterate_tree.preorder_print(root, singlelist, doublelist, triplelist, testsugar) 


        def getNodeGrp():
            for sugar in doublelist:
                sugartem = sugar.split("-")
                anomernode = sugartem[0][-1] + "-" + sugartem[1][0]
                node1 = "(" + sugartem[0][:-1] + "," + anomernode + ")"
                node2 = "(" + anomernode + "," + sugartem[1][1:] + ")"
                NodeGrp.append(node1)
                NodeGrp.append(node2)
            #print(NodeGrp)
            print("\n")


        getNodeGrp()
        output.writesugar(sugar, singlelist, doublelist, triplelist, NodeGrp)
