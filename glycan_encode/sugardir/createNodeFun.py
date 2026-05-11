import sys
import sugardir.sugar_1 as sugar1
import sugardir.sugar_2 as sugar2
import sugardir.sugar_3 as sugar3
import sugardir.sugar_4 as sugar4
import sugardir.sugar_5 as sugar5
import sugardir.sugar_6 as sugar6
import sugardir.sugar_7 as sugar7
import sugardir.sugar_8 as sugar8

sugatlistdic = {"glycan_1": ['Gal', 'Glc', 'Gul', 'Man','HexA'],
                "glycan_2": ['Xyl', 'Ara', 'Fuc', 'Rha', 'GlcA', 'IdoA'],
                "glycan_3": ['GalNAc', 'GlcNAc','GlcNS'],
                "glycan_4": ['MurNAc'],
                "glycan_5": ['Neu5Ac', 'Neu5Gc'],
                "glycan_6": ['KDN'],
                "glycan_7": ['KDO'],
                "glycan_8": ['Neu5,9Ac2']}

sugatlistdic = {key: [value.lower() for value in values] for key, values in sugatlistdic.items()}
def createNode(sugarlab,sugarlabvalue,sugarnodelist,num,depth):

    for key, value in sugatlistdic.items():
        for value_key in value:
            if value_key == sugarlabvalue:
                sugarkey = key
                if sugarkey == "glycan_1":
                    if not sugarnodelist:
                        root = sugar1.builtGlycan1Node(sugarlab,sugarlabvalue)
                        root.anomer.items()
                        root.parent = "root"
                        root.anomer["c"] = None
                        sugarnodelist.append(root)
                        num[f'num{depth}'] += 1


                    else:
                        Node1 = sugar1.builtGlycan1Node(sugarlab,sugarlabvalue)
                        sugarnodelist.append(Node1)
                        num[f'num{depth}'] += 1
                        if len(sugarnodelist[-1].parent) != 0 and sugarnodelist[-1].parent[0] == "1":
                            sugarnodelist[-1].parent.append(sugarnodelist[-2])
                        else:
                            print("error")


                        if sugarnodelist[-2].childflagnum <= 1:
                            for chidrenkey, chidrenvalue in sugarnodelist[-2].childrenlistdic.items():
                                if len(chidrenvalue) != 0 and chidrenvalue[0] == chidrenkey:
                                    del chidrenvalue[0]
                                    chidrenvalue.append(sugarnodelist[-1])
                                    sugarnodelist[-2].childflagnum -= 1
                        else:
                            print("error")
                            sys.exit()

                elif sugarkey == "glycan_2":
                    if not sugarnodelist:
                        root = sugar2.builtGlycan2Node(sugarlab,sugarlabvalue)
                        root.parent = "root"
                        root.anomer["c"] = None
                        sugarnodelist.append(root)
                        num[f'num{depth}'] += 1

                    else:
                        Node1 = sugar2.builtGlycan2Node(sugarlab,sugarlabvalue)
                        sugarnodelist.append(Node1)
                        num[f'num{depth}'] += 1
                        if len(sugarnodelist[-1].parent) != 0 and sugarnodelist[-1].parent[0] == "1":
                            sugarnodelist[-1].parent.append(sugarnodelist[-2])
                        else:
                            print("error")

                        if sugarnodelist[-2].childflagnum <= 1:
                            for chidrenkey, chidrenvalue in sugarnodelist[-2].childrenlistdic.items():
                                if len(chidrenvalue) != 0 and chidrenvalue[0] == chidrenkey:
                                    del chidrenvalue[0]
                                    chidrenvalue.append(sugarnodelist[-1])
                                    sugarnodelist[-2].childflagnum -= 1
                        else:
                            print("error")
                            continue


                elif sugarkey == "glycan_3":
                    if not sugarnodelist:
                        root = sugar3.builtGlycan3Node(sugarlab,sugarlabvalue)
                        root.parent = "root"
                        root.anomer["c"] = None
                        sugarnodelist.append(root)
                        num[f'num{depth}'] += 1

                    else:
                        Node1 = sugar3.builtGlycan3Node(sugarlab,sugarlabvalue)
                        sugarnodelist.append(Node1)
                        num[f'num{depth}'] += 1
                        if len(sugarnodelist[-1].parent) != 0 and sugarnodelist[-1].parent[0] == "1":
                            sugarnodelist[-1].parent.append(sugarnodelist[-2])
                        else:
                            print("error")
                        if sugarnodelist[-2].childflagnum == 1:
                            for chidrenkey, chidrenvalue in sugarnodelist[-2].childrenlistdic.items():
                                if len(chidrenvalue) != 0 and chidrenvalue[0] == chidrenkey:
                                    del chidrenvalue[0]
                                    chidrenvalue.append(sugarnodelist[-1])
                                    sugarnodelist[-2].childflagnum -= 1
                        else:
                            print("error")
                            continue


                elif sugarkey == "glycan_4":
                    if not sugarnodelist:
                        root = sugar4.builtGlycan4Node(sugarlab,sugarlabvalue)
                        root.parent = "root"
                        root.anomer["c"] = None
                        sugarnodelist.append(root)
                        num[f'num{depth}'] += 1

                    else:
                        Node1 = sugar4.builtGlycan4Node(sugarlab,sugarlabvalue)
                        sugarnodelist.append(Node1)
                        num[f'num{depth}'] += 1
                        if len(sugarnodelist[-1].parent) != 0 and sugarnodelist[-1].parent[0] == "1":
                            sugarnodelist[-1].parent.append(sugarnodelist[-2])
                        else:
                            print("error")


                        if sugarnodelist[-2].childflagnum <= 1:
                            for chidrenkey, chidrenvalue in sugarnodelist[-2].childrenlistdic.items():
                                if len(chidrenvalue) != 0 and chidrenvalue[0] == chidrenkey:
                                    del chidrenvalue[0]
                                    chidrenvalue.append(sugarnodelist[-1])
                                    sugarnodelist[-2].childflagnum -= 1
                        else:
                            print("error")
                            continue

                elif sugarkey == "glycan_5":
                    if not sugarnodelist:
                        root = sugar5.builtGlycan5Node(sugarlab,sugarlabvalue)
                        root.parent = "root"
                        root.anomer["c"] = None
                        sugarnodelist.append(root)
                        num[f'num{depth}'] += 1

                    else:
                        Node1 = sugar5.builtGlycan5Node(sugarlab,sugarlabvalue)
                        sugarnodelist.append(Node1)
                        num[f'num{depth}'] += 1
                        if len(sugarnodelist[-1].parent) != 0 and sugarnodelist[-1].parent[0] == "2":
                            sugarnodelist[-1].parent.append(sugarnodelist[-2])
                        else:
                            print("error")

                        if sugarnodelist[-2].childflagnum <= 1:
                            for chidrenkey, chidrenvalue in sugarnodelist[-2].childrenlistdic.items():
                                if len(chidrenvalue) != 0 and chidrenvalue[0] == chidrenkey:
                                    del chidrenvalue[0]
                                    chidrenvalue.append(sugarnodelist[-1])
                                    sugarnodelist[-2].childflagnum -= 1
                        else:
                            print("error")
                            continue


                elif sugarkey == "glycan_6":
                    if not sugarnodelist:
                        root = sugar6.builtGlycan6Node(sugarlab,sugarlabvalue)
                        root.parent = "root"
                        root.anomer["c"] = None
                        sugarnodelist.append(root)
                        num[f'num{depth}'] += 1

                    else:
                        Node1 = sugar6.builtGlycan6Node(sugarlab,sugarlabvalue)
                        sugarnodelist.append(Node1)
                        num[f'num{depth}'] += 1

                        if len(sugarnodelist[-1].parent) != 0 and sugarnodelist[-1].parent[0] == "2":
                            sugarnodelist[-1].parent.append(sugarnodelist[-2])
                        else:
                            print("error")

                        if sugarnodelist[-2].childflagnum <= 1:
                            for chidrenkey, chidrenvalue in sugarnodelist[-2].childrenlistdic.items():
                                if len(chidrenvalue) != 0 and chidrenvalue[0] == chidrenkey:
                                    del chidrenvalue[0]
                                    chidrenvalue.append(sugarnodelist[-1])
                                    sugarnodelist[-2].childflagnum -= 1
                        else:
                            print("error")
                            continue


                elif sugarkey == "glycan_7":
                    if not sugarnodelist:
                        root = sugar7.builtGlycan7Node(sugarlab,sugarlabvalue)
                        root.parent = "root"
                        root.anomer["c"] = None
                        sugarnodelist.append(root)
                        num[f'num{depth}'] += 1

                    else:
                        Node1 = sugar7.builtGlycan7Node(sugarlab,sugarlabvalue)
                        sugarnodelist.append(Node1)
                        num[f'num{depth}'] += 1
                        if len(sugarnodelist[-1].parent) != 0 and sugarnodelist[-1].parent[0] == "2":
                            sugarnodelist[-1].parent.append(sugarnodelist[-2])
                        else:
                            print("error")

                        if sugarnodelist[-2].childflagnum <= 1:
                            for chidrenkey, chidrenvalue in sugarnodelist[-2].childrenlistdic.items():
                                if len(chidrenvalue) != 0 and chidrenvalue[0] == chidrenkey:
                                    del chidrenvalue[0]
                                    chidrenvalue.append(sugarnodelist[-1])
                                    sugarnodelist[-2].childflagnum -= 1
                        else:
                            print("error")
                            continue
              

                elif sugarkey == "glycan_8":
                    if not sugarnodelist:
                        root = sugar8.builtGlycan8Node(sugarlab,sugarlabvalue)
                        root.parent = "root"
                        root.anomer["c"] = None
                        sugarnodelist.append(root)
                        num[f'num{depth}'] += 1
                    else:
                        Node1 = sugar8.builtGlycan8Node(sugarlab,sugarlabvalue)
                        sugarnodelist.append(Node1)
                        num[f'num{depth}'] += 1
                        if len(sugarnodelist[-1].parent) != 0 and sugarnodelist[-1].parent[0] == "2":
                            sugarnodelist[-1].parent.append(sugarnodelist[-2])
                        else:
                            print("error")

                        if sugarnodelist[-2].childflagnum <= 1:
                            for chidrenkey, chidrenvalue in sugarnodelist[-2].childrenlistdic.items():
                                if len(chidrenvalue) != 0 and chidrenvalue[0] == chidrenkey:
                                    del chidrenvalue[0]
                                    chidrenvalue.append(sugarnodelist[-1])
                                    sugarnodelist[-2].childflagnum -= 1
                        else:
                            print("error")
                            continue

if __name__ == '__main__':
    createNode()
