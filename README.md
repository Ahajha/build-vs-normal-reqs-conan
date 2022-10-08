# build-vs-normal-reqs-conan
Minimal reproducible example of what is at best misguided advice, at worst a bug in Conan

How to reproduce:

`python3 build.py`

The error produced suggests an override of `pkg1`, yet it _is_ overridden both in the normal and build requirements. This is either misguided advice, or perhaps a bug. I'm not sure of how to make this example actually work.