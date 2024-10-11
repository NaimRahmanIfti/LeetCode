list1 = [1,2,4]
list2 = [1,3,4]
m_l =[]
# def merge(list1,list2):
for i in list1:
    print(i)

    for j in list2:
        print(j)
        if i >= j:
            m_l.append(j)

    print(m_l)



