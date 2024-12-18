"""
Created on Thu Dec 12 13:15:17 2024

@author: chana
"""
import time

#จับเวลา
start_time = time.time()

with open("Sorting-Algorithm/province_deta.txt", "r", encoding="utf-8") as file:
    lines = file.readlines() # อ่านไฟล์ทีละบรรทัดแล้วเก็บในลิสต์

def SelectionSort(a_list):
    n = len(a_list)

    for i in range(0, n-1):
        iMin = i

        for j in range(i+1, n):
            
            if a_list[j] > a_list[iMin]:
                iMin = j

        # สลับตำแหน่ง
        temp = a_list[i]
        a_list[i] = a_list[iMin]
        a_list[iMin] = temp

    return a_list

sorted_lines = SelectionSort(lines) #เรียงลำดับ

end_time = time.time()
elapsed_time = end_time - start_time

for line in sorted_lines:
    print(line.strip())  

#print(f"เวลาที่ใช้: {elapsed_time:.2f} วินาที")

#คำนวณเวลา
end_time = time.time()
elapsed_time = end_time - start_time

print(f"เวลาที่ใช้ในการประมวลผล: {elapsed_time:.6f} วินาที")


