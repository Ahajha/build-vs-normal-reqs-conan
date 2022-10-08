from conan import ConanFile

class Pkg3Conan(ConanFile):
    name = "pkg3"

    def requirements(self):
        self.requires("pkg2/1.0.0@build-req-repro/test")
