from tinycore import  RemoteRepo

r = RemoteRepo("http://www.tinycorelinux.net", "11.x", "x86_64")
r.update()
print(r.package_list[0])
r.download(name=r.package_list[0])

