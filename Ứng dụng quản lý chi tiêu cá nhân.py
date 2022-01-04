def chitieu(mytemplist,item):
    mytemplist.append(item)
def timindex(mytemplist,itemname):
    result = -1
    length = len(mytemplist)
    for i in range(length):
        if mytemplist[i]['name']==itemname:
            result=i
    return result
def xoaiteam(mytemplist,itemname):
    if findindexitem(mytemplist,itemname)>-1:
        del mytemplist[findindexitem(mytemplist,itemname)]
    else:
        print(itemname + "không có phần tử trong mảng")
print("chi tiêu của bạn: ",chitieu)
print("Bạn muốn làm gì ? -\n"
        "1.add\n"\
        "2.Remove")
tuychon=int(input("chọn 1 hoặc 2"))
nameinput=input("Item name: ")
if tuychon==1:
    chiphi = int(input("Item cost: "))
    ngaynhap=input("Date: ")
    item={'name':nameinput,'chiphi':chiphi,'date':ngaynhap}
    additem(chitieu,item)
    print("chi tiêu của bạn",chitieu)
elif tuychon == 2:
    xoaiteam(chitieu,nameinput)
    print("chi tiêu của bạn",chitieu)
else:
    print('Đầu vào không hợp lệ')