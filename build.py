import subprocess

subprocess.run(["conan", "remove", "*/*@build-req-repro/test", "-f"])

print("============================================= PKG1 1.0.0 =============================================")
subprocess.run(["conan", "create", "pkg1", "1.0.0@build-req-repro/test"])

print("============================================= PKG1 1.1.0 =============================================")
subprocess.run(["conan", "create", "pkg1", "1.1.0@build-req-repro/test"])

print("============================================= PKG2 1.0.0 =============================================")
subprocess.run(["conan", "create", "pkg2", "1.0.0@build-req-repro/test"])

print("============================================= PKG2 1.1.0 =============================================")
subprocess.run(["conan", "create", "pkg2", "1.1.0@build-req-repro/test"])

print("============================================= PKG3 1.0.0 =============================================")
subprocess.run(["conan", "create", "pkg3", "1.0.0@build-req-repro/test"])

print("============================================= PKG4 1.0.0 =============================================")
subprocess.run(["conan", "create", "pkg4", "1.0.0@build-req-repro/test"])
