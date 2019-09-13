phone = "(080)62164823"
print(phone.find("080", 1, 4))

area_code = phone[1:4]
print(area_code)

parts = phone.split(")")
print(parts[0])
