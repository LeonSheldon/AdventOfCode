f = open('input5.txt', 'r')
strings = f.readlines()
f.close()
nice = 0
ix = 0

def isnice(s):
   vowels = 0
   previous = '0'
   double = False
   for x in s:
      if x in ['a', 'e', 'i', 'o', 'u']:
         vowels += 1
      if x == previous:
         double = True
      if (previous, x) == ('a', 'b') or (previous, x) == ('c', 'd') or (previous, x) == ('p', 'q') or (previous, x) == ('x', 'y'):
         return False
      previous = x
   print (double ,(vowels > 2))
   if double and (vowels > 2):
      return True
   return False

def isnice_(s):
   rule1 = False
   rule2 = False
   pairs = []
   previous = '0'
   prevpair = '00'
   for x in s:
      print previous + x
      if previous + x in pairs[:-1]:
         rule1 = True
      if prevpair[0] == x:
         rule2 = True
      prevpair = previous + x
      previous = x
      pairs.append(prevpair)
   print (rule1, rule2)
   return rule1 and rule2



l = len(strings)

while not ix == l:
   if isnice_(strings[ix]):
      nice += 1
      print nice
   ix += 1

print nice
