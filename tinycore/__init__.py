import requests

class PackageInfo:
    def __init__(self, content):
        self.content = content

class Repo:
    def __init__(self, version, arch):
        self.version = version
        self.arch = arch
        self.packages  = {}
        self.package_list = []

class RemoteRepo(Repo):
    def __init__(self, url, version, arch):
        Repo.__init__(self,version, arch)
        self.url = url + "/" + version + "/" +  arch + "/tcz/"
        print(self.url)

    def update(self):
        self.package_list = [s.decode()  for s in requests.get(self.url).content.splitlines()]
        for pkg in self.package_list:
            self.packages[pkg] = Package(pkg)
            self.packages[pkg].get_remote(self.url)


    def download(self, name=None):
        if name != None:
            if name in self.packages.keys():
                self.packages[name].get_remote(self.url)

class LocalRepo(Repo):
    def __init__(self, dir, version, arch):
        self.dir = dir
        Repo.__init__(self, version, arch)

class Package:
    def __init__(self, name):
        self.name = name
        self.deps = []

    def get_remote(self, url):
        print(url + self.name + ".dep")
        self.info = PackageInfo(requests.get(url + self.name + ".info").content.splitlines())
        print(self.deps)
        print(self.info.content)

    def get_local(self, dir):
        self.deps = [s.decode()  for s in open(dir + self.name + ".dep", "r").readlines()]
        self.info = PackageInfo(open(dir + self.name + ".info", "r").readlines())