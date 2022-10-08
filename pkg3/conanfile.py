from conan import ConanFile

class Pkg3Conan(ConanFile):
    name = "pkg3"

    def requirements(self):
        self.requires("pkg1/1.1.0@build-req-repro/test")
        
    def build_requirements(self):
        self.test_requires("pkg2/1.0.0@build-req-repro/test")
        self.test_requires("pkg1/1.1.0@build-req-repro/test")
