from sugardir import outputfuc as otp
def preorder_print(sugarnode, singlelist, doublelist, triplelist,testsugar):
    if sugarnode is None:
        return
    else:
        def getsinglesugar(sugarnodelable):
            single_anomer_keys = [key for key,value in sugarnodelable.anomer.items() if value]
            if len(single_anomer_keys) == 0:
                singlesugar = sugarnodelable.label
            else:
                singlesugar = f"{sugarnodelable.label}" + f"{single_anomer_keys[0]}"
            singlelist.append(singlesugar)

        def getdoublesugar(sugarnodelable):
            childnum = 0
            for currentchildkey, currentchildvalue in sugarnodelable.childrenlistdic.items():
                if len(currentchildvalue) != 0 and currentchildvalue[0] != 'SO3' and currentchildvalue[0] != 'P':
                    childnum += 1
                    children_anomer_keys = [key for key, value in currentchildvalue[0].anomer.items() if value][0]
                    parent_anomer_keys = [key for key, value in sugarnodelable.anomer.items() if value]
                    if len(parent_anomer_keys) == 0:
                        doublesugar = f"{currentchildvalue[0].label}" + f"{children_anomer_keys}" + f"{currentchildvalue[0].parent[0]}" + "-" + f"{currentchildkey}" + f"{sugarnode.label}"
                    else:
                        doublesugar = f"{currentchildvalue[0].label}" + f"{children_anomer_keys}" + f"{currentchildvalue[0].parent[0]}" + "-" + f"{currentchildkey}" + f"{sugarnode.label}" + f"{parent_anomer_keys[0]}"#看单糖之间的连接:当前节点的标签+糖苷键类型+父亲节点连接+”-“+在父亲节点的连接方式+父亲节点
                    doublelist.append(doublesugar)

        def gettriplesugar(sugarnodelable):
            childnum = 0
            for currentchildkey, currentchildvalue in sugarnodelable.childrenlistdic.items():
                if len(currentchildvalue) != 0 and currentchildvalue[0] != 'SO3' and currentchildvalue[0] != 'P':

                    childnum += 1
                    anomer_keys = [key for key, value in currentchildvalue[0].anomer.items() if value][0]
                    childsecnum = 0
                    for currentchildseckey, currentchildsecvalue in currentchildvalue[0].childrenlistdic.items():
                        if len(currentchildsecvalue) != 0 and currentchildsecvalue[0] != 'SO3' and currentchildsecvalue[0] != 'P':
                            childsecnum += 1
                            anomersec_keys = [key for key, value in currentchildsecvalue[0].anomer.items() if value][0]
                            parent_anomer_keys = [key for key, value in sugarnodelable.anomer.items() if value]
                            if len(parent_anomer_keys) == 0:
                                triplesugar = f"{currentchildsecvalue[0].label}" + f"{anomersec_keys}" + f"{currentchildsecvalue[0].parent[0]}" + "-" + f"{currentchildseckey}" + f"{currentchildvalue[0].label}" + f"{anomer_keys}" + f"{currentchildvalue[0].parent[0]}" +"-"+ f"{currentchildkey}" + f"{sugarnode.label}"
                            else:
                                triplesugar = f"{currentchildsecvalue[0].label}" + f"{anomersec_keys}" + f"{currentchildsecvalue[0].parent[0]}" + "-" + f"{currentchildseckey}" + f"{currentchildvalue[0].label}" + f"{anomer_keys}" + f"{currentchildvalue[0].parent[0]}" + "-" + f"{currentchildkey}" + f"{sugarnode.label}" + f"{parent_anomer_keys[0]}"
                            triplelist.append(triplesugar)

        getsinglesugar(sugarnode)
        getdoublesugar(sugarnode)
        gettriplesugar(sugarnode)

    for childnode in sugarnode.childrenlistdic.values():
        if len(childnode) != 0 and childnode[0] != 'SO3' and childnode[0] != 'P':
            preorder_print(childnode[0], singlelist, doublelist, triplelist,testsugar)
            

        root_index = testsugar.split('-')
        root_index.remove('')

        root_name = singlelist[0]
        same_rootname = []
        if root_name == 'Ara' or root_name == 'Rha':
            singlelist.remove(root_name)
            rootcount = {root_name: 0}
            a_bcount = {'a': 0, 'b': 0}
            for i in singlelist:
                if root_name == i[0:-1]:
                    same_rootname.append(i)
                    rootcount[root_name] += 1
            for s in same_rootname:
                if s[-1] == 'a':
                    a_bcount['a'] += 1
                elif s[-1] == 'b':
                    a_bcount['b'] += 1

            rootcount_values = rootcount[root_name]

            if rootcount_values / int(len(root_index)) >= 0.5:
                if a_bcount['a'] >= a_bcount['b']:
                    root_name = root_name + 'a'
                elif a_bcount['a'] < a_bcount['b']:
                    root_name = root_name + 'b'
            singlelist.append(root_name)
        else:
            if root_name[-1] == 'a' or root_name[-1] == 'b':
                singlelist = singlelist
            else:  
                singlelist.remove(root_name)
                rootcount = {root_name: 0}
                a_bcount = {'a': 0, 'b': 0}
                for i in singlelist:
                    if root_name == i[0:-1]:
                        same_rootname.append(i)
                        rootcount[root_name] += 1
                for s in same_rootname:
                    if s[-1] == 'a':
                        a_bcount['a'] += 1
                    elif s[-1] == 'b':
                        a_bcount['b'] += 1
         
                rootcount_values = rootcount[root_name]
                if rootcount_values / int(len(root_index)) >= 0.5:
                    if a_bcount['a'] >= a_bcount['b']:
                        root_name = root_name + 'a'
                    elif a_bcount['a'] < a_bcount['b']:
                        root_name = root_name + 'b'
                singlelist.append(root_name)
        otp.countsugar(singlelist)
        # print(doublelist)
        otp.countsugar(doublelist)
        # print(triplelist)
        otp.countsugar(triplelist)
if __name__ == '__main__':
    preorder_print()
