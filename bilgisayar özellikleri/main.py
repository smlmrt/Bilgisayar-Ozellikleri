import os

b = os.uname()
print(b)
print("""
    işletim sistemi : {} {}
    Bilgisayar adı : {}
    Sürüm : {}
    Sürüm tarihi : {}
    """.format(
    b.sysname, b.machine,
    b.nodename,
    b.release,
    b.version))
