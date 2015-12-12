import md5

prepended = "yzbqklnj"

i = 0

while True:
   m = md5.new()
   m.update(prepended + str(i))
   if m.hexdigest()[0:6] == "000000":
      print(i)
      break
   i += 1

