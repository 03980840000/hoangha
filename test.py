import random
hoten = input("nhập họ tên: "
ngaysinh = input ("nhập ngày sinh: ")
diemqt = float(input("nhập điểm quá trình"))
diemt = float(input("nhập điểm thi"))
masv = str(random.randint(1,99))
dem = int(len(masv))
if dem == 1:
    masv = "PXU" + "0" + masv
else:
    masv = "PXU" + masv

print("mã sinh viên: "+str(masv))
print("họ tên là: ",hoten)
print("ngày sinh là: ",ngaysinh)
print("điểm thi: ",diemt)
print("điểm quá trình ",diemqt)
print("điểm tổng kết: ",(diemqt+diemt)/2)