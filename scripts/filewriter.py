val = int(''.join(open("scripts/file", "r").readlines()))
val += 1
print(val)
open("scripts/file", "w").write(str(val))

exit()
