import sys


class glycan2:
    def __init__(self, label):
        self.label = label
        self.anomer = {'a': None,
                       'b': None,
                       'c': None}
        self.parent = []
        self.children_2 = []
        self.children_3 = []
        self.children_4 = []
        self.childflagnum = 0
        self.childrenlistdic = {"2": self.children_2,
                                "3": self.children_3,
                                "4": self.children_4
                                }


def builtGlycan2Node(label1, sugarlabvalue):
    Glycan2Node = glycan2(label1[1:-2])
    if label1[-2] == "a":
        Glycan2Node.anomer["a"] = "a"
    elif label1[-2] == "b":
        Glycan2Node.anomer["b"] = "b"
    elif label1[-2] == "c":
        Glycan2Node.anomer["c"] = "c"
    else:
        sys.exit()
    try:
        if label1[-1] == "1":
            Glycan2Node.parent.append("1")
        elif label1[-1] == "0":
            Glycan2Node.parent = "root"
    except IndexError:
        sys.exit()
    Modification_groups = label1[1:len(label1[1:-2]) - len(sugarlabvalue) + 1]
    search_index = []
    if 'S' or 's' in Modification_groups:
        for index, letter in enumerate(Modification_groups):
            if letter == 'S':
                search_index.append(Modification_groups[index - 1])  # [1]
            for SO3_index in search_index:
                for chidrenkey, chidrenvalue in Glycan2Node.childrenlistdic.items():
                    if SO3_index == chidrenkey:
                        chidrenvalue.append("SO3")
                search_index = []

    if 'P' or 'p' in Modification_groups:
        for index, letter in enumerate(Modification_groups):
            if letter == 'P':
                search_index.append(Modification_groups[index - 1])  # [1]
                for p_indx in search_index:
                    for chidrenkey, chidrenvalue in Glycan2Node.childrenlistdic.items():
                        if p_indx == chidrenkey:
                            chidrenvalue.append("P")
                    search_index = []
    if label1[0]!= '0' and label1[0] not in Glycan2Node.childrenlistdic.keys():

        sys.exit()
    for childkey, childvalue in Glycan2Node.childrenlistdic.items():
        if label1[0] == childkey and len(childvalue) == 0:
            childvalue.append(childkey)
            Glycan2Node.childflagnum += 1

    return Glycan2Node


if __name__ == '__main__':
    builtGlycan2Node()
