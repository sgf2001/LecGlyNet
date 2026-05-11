import sys


class glycan4:
    def __init__(self, label):
        self.label = label
        self.anomer = {'a': None,
                       "b": None,
                       'c': None}
        self.parent = []

        self.children_4 = []
        self.children_6 = []
        self.childflagnum = 0
        self.childrenlistdic = {"4": self.children_4,
                                "6": self.children_6
                                }


def builtGlycan4Node(label1, sugarlabvalue):
    Glycan4Node = glycan4(label1[1:-2])
    if label1[-2] == "a":
        Glycan4Node.anomer["a"] = "a"
    elif label1[-2] == "b":
        Glycan4Node.anomer["b"] = "b"
    elif label1[-2] == "c":
        Glycan4Node.anomer["c"] = "c"
    else:
        sys.exit()

    try:
        if label1[-1] == "1":
            Glycan4Node.parent.append("1")
        elif label1[-1] == "0":
            Glycan4Node.parent = "root"
    except IndexError:
        sys.exit()

    Modification_groups = label1[1:len(label1[1:-2]) - len(sugarlabvalue) + 1]
    search_index = []
    if 'S' or 's' in Modification_groups:
        for index, letter in enumerate(Modification_groups):
            if letter == 'S':
                search_index.append(Modification_groups[index - 1])  # [1]
            for SO3_index in search_index:
                for chidrenkey, chidrenvalue in Glycan4Node.childrenlistdic.items():
                    if SO3_index == chidrenkey:
                        chidrenvalue.append("SO3")
                search_index = []
 
    if 'P' or 'p' in Modification_groups:
        for index, letter in enumerate(Modification_groups):
            if letter == 'P':
                search_index.append(Modification_groups[index - 1])  # [1]
                for p_indx in search_index:
                    for chidrenkey, chidrenvalue in Glycan4Node.childrenlistdic.items():
                        if p_indx == chidrenkey:
                            chidrenvalue.append("P")
                    search_index = []
    if label1[0]!= '0' and label1[0] not in Glycan4Node.childrenlistdic.keys():

        sys.exit()
    for childkey, childvalue in Glycan4Node.childrenlistdic.items():
        if label1[0] == childkey and len(childvalue) == 0:
            childvalue.append(childkey)
            Glycan4Node.childflagnum += 1

    return Glycan4Node


if __name__ == '__main__':
    builtGlycan4Node()
