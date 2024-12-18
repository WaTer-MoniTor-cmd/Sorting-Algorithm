
"""
Created on Thu Dec 12 14:06:26 2024

@author: chana
"""
import time

#จับเวลา
start_time = time.time()

with open("Sorting-Algorithm/province_deta.txt", "r", encoding="utf-8") as file:
    lines = file.readlines() # อ่านไฟล์ทีละบรรทัดแล้วเก็บในลิสต์
    
def BubbleSort(a_list):
    n = len(a_list)
    for k in range(1,n):
        flag = 0
        for i in range(0,n-k):
            if a_list[i] < a_list[i+1]:
                tmp = a_list[i]
                a_list[i] = a_list[i+1]
                a_list[i+1] = tmp
                flag = 1
        if flag == 0:
            break
    return a_list

sorted_lines = BubbleSort(lines)

#คำนวณเวลา
end_time = time.time()
elapsed_time = end_time - start_time

for line in sorted_lines:
    print(line.strip()) 

print(f"เวลาที่ใช้: {elapsed_time:.6f} วินาที")
