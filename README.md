# python-cpp-extension

```
git clone git@github.com:banbao990/python-cplusplus.git
git submodule update --init --recursive
```

+ **<span style="color:red">MUST DO THIS</span>**
```bash
python prepare.py
# if complies error, do the following cmd instead
# python prepare.py --clean --all
```



# mi3 环境

## 例子

+ 基本例子

|        module         |    window    |    Linux     |   备注   |
| :-------------------: | :----------: | :----------: | :------: |
|   pytorch-cuda-jit    | $\checkmark$ | $\checkmark$ | 直接执行 |
|   pytorch-optix-jit   | $\checkmark$ | $\checkmark$ | 直接执行 |
| python-cpp-setuptools | $\checkmark$ | $\checkmark$ | 安装执行 |
|   python-cpp-cmake    | $\checkmark$ | $\checkmark$ | 安装执行 |
|      cmake-oidn       | $\checkmark$ | $\checkmark$ | 安装执行 |

+ 其他例子

|   module    |    window    | Linux |   备注   |
| :---------: | :----------: | :---: | :------: |
| cmake-optix | $\checkmark$ |       | 安装执行 |

+ 测试环境
  + windows
    + cuda 12.3、optix SDK 8.0.0、cmake 3.25.1
  + linux
    + cuda 12.1、optix SDK 8.0.0、cmake 3.25.1
+ Optix SDK：[Link](https://developer.nvidia.com/designworks/optix/download)
  + 可以直接通过 `wget` 下载


```txt
https://developer.nvidia.com/downloads/designworks/optix/secure/8.0.0/nvidia-optix-sdk-8.0.0-win64.exe
https://developer.nvidia.com/downloads/designworks/optix/secure/8.0.0/nvidia-optix-sdk-8.0.0-linux64-x86_64.sh
```

+ 直接执行（例子）

```bash
python src/pytorch-cuda-jit/test.py
```

+ 安装执行（例子）

```bash
# install
python src/python-cpp-setuptools/install.py
# run
python src/python-cpp-setuptools/test.py
```




## python

+ 只需要如下配置，即可执行本工程中的代码

```bash
# env
conda create -n mi3 python=3.10
```

```bash
# pytorch
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia

# ninja, opencv, yacs
pip install ninja opencv-python yacs pybind11

# ui
pip install imgui glfw cuda-python PyOpenGL PyOpenGL_accelerate

# mitsuba
pip install mitsuba
```



### 其他库

+ mi 环境中的其他库

```bash


# opengl, cuda
pip install pycuda # 会报错, 解决方案见下面

# tinycudann
git clone --recursive https://github.com/nvlabs/tiny-cuda-nn
cd bindings/torch
python setup.py install

# tqdm, tensorboard
pip install tqdm
pip install tensorboard

# torch_scatter
# https://github.com/rusty1s/pytorch_scatter/issues/186
pip install --no-index torch-scatter -f https://pytorch-geometric.com/whl/torch-2.1.0+cu121.html

# matplotlib, openexr
pip install matplotlib
pip install OpenEXR

# oidn (CPU version)
pip install oidn
```



## 其他问题

### pycuda

+ **这个库能够完全被 `cuda-python` 库取代，现在也不用了**
+ 直接 `pip install pycuda` 报错
  +  `PyCUDA was compiled without GL extension support`

#### windows

+ [解决方案](https://github.com/harskish/ganspace/issues/43)

```txt
I've actually fixed this one. If you are on a windows device, you should pip install pipwin, then use pipwin to install pycuda. And then it installs it correctly.
```

```bash
pip install pipwin
pipwin install pycuda
```

#### linux

+ 从源码安装：[code](https://github.com/inducer/pycuda)
