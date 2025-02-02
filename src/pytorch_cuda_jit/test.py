import torch
from torch.utils.cpp_extension import load
from glob import glob
import os
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(CURRENT_DIR, "../../"))

from src.config import check_user_settings
check_user_settings()
from src.config import _C as cfg

os.environ['PATH'] = os.environ['PATH'] + os.pathsep + cfg.PATH

os.environ["TORCH_EXTENSIONS_DIR"] = os.path.join("build")
Debug = False  # compile with debug flag
verbose = True  # show compile command
cuda_files = glob("bind.cu", root_dir=CURRENT_DIR)  # source files
cuda_files = [os.path.join(CURRENT_DIR, f) for f in cuda_files]
include_dirs = [os.path.join(CURRENT_DIR, "include")]  # include directories
cflags = ["--extended-lambda", "--expt-relaxed-constexpr"]  # nvcc flags

if sys.platform == "win32":
    if Debug:
        cflags.extend(["/DEBUG:FULL", "/Od"])
    else:
        cflags.extend(["/DEBUG:NONE", "/O2"])
elif sys.platform == "linux":
    if Debug:
        cflags.extend(["-G", "-g", "-O0"])
    else:
        cflags.extend(["-O3"])

cuda_module = load(
    name="cuda_module",
    sources=cuda_files,
    extra_include_paths=include_dirs,
    extra_cflags=cflags,
    verbose=verbose,
)

N = 10000
a = torch.arange(N, device="cuda", dtype=torch.float32)
b = torch.arange(N, device="cuda", dtype=torch.float32)

c = cuda_module.custom_cuda_func(a, b)

res = torch.allclose(c, a + b)
print("\033[9{}mTest Result: {}\033[00m".format(2 if res else 1, res))
