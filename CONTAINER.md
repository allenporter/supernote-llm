# Container

Messing around to see if intel acceleration can provide any performance wins.
So far, not for my hardware.

Container: `intel/oneapi-runtime:latest`
```
Packages:
- python3
- python3-pip
- vim
- intel-oneapi-compiler-dpcpp-cpp-and-cpp-classic (?)
```

Compile flags from https://github.com/ggerganov/llama.cpp?tab=readme-ov-file#intel-onemkl

```bash
PATH="${PATH}:/opt/intel/oneapi/compiler/2023.2.3/linux/bin/"
CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=Intel10_64lp -DCMAKE_C_COMPILER=icx -DCMAKE_CXX_COMPILER=icpx -DLLAMA_NATIVE=ON" pip3 install -r requirements.txt
```

```bash
$ python3 -m llama_cpp.server --model=...
```
