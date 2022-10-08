from conan import ConanFile

class Pkg2Conan(ConanFile):
    name = "pkg2"

    def requirements(self):
        self.requires("pkg1/1.0.0@build-req-repro/test")
