# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:47:25 2024

@author: chana
"""

# เปิดไฟล์ .txt
with open("Sorting-Algorithm/Thai address data/province.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # อ่านไฟล์ทีละบรรทัดแล้วเก็บในลิสต์

# เปิดไฟล์ province_deta.txt สำหรับเขียนข้อมูล
with open("province_deta.txt", "w", encoding="utf-8") as output_file:
    # วนลูปผ่านแต่ละบรรทัด
    for line in lines:
        # ตรวจสอบว่ามีคำว่า VALUES ในแต่ละบรรทัด
        if "VALUES" in line:
            # ตัดส่วน VALUES ออก
            values_part = line.split("VALUES")[1]

            # ลบเครื่องหมายวงเล็บ, ช่องว่าง, และ ;
            values_part = values_part.strip(" ();\n").replace("'", "")

            # แยกค่าด้วยเครื่องหมายคอมมา
            values = values_part.split(", ")

            # จัดรูปแบบผลลัพธ์
            #mcode = values[0]
            #mname = values[1]
            #mno = values[2]
            #mtype = values[3]
            pcode = values[0]
            pname = values[1]
            #type_soilder = values[2]
            #acode = values[6]
            #aname = values[7]
            #tcode = values[8]
            #tname = values[9]
            #orgname = values[11]
            #orgtype = values[12]

            # สร้างสตริงผลลัพธ์ตามที่ต้องการ
            #output = f"{pcode} {pname} {type_soilder}\n"
            output = f"{pcode} {pname}\n"

            # เขียนข้อมูลลงไฟล์ _deta.txt
            output_file.write(output)

print("OK!")