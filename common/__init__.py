import os
import sys
# 配置模块的读取路径
base_path = os.path.dirname(os.getcwd())
sys.path.append(base_path)
print(base_path)
