# GPT服务器

# 环境

### 数据库

redis-5.0.14

https://github.com/tporadowski/redis/releases

### 本地GPT框架

llama.cpp-python

注意需要使用CUDA后端

```
pip install llama-cpp-python[server] --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu122
```

使用llama3-8b

评估效果不佳，无法通过最简单的测试

# 网络

端口：5101

### 本地GPT服务器启动参数

```
python -m llama_cpp.server --model D:\GitHub\Llama3-8B-Chinese-Chat.q4_k_m.GGUF
```

```
python -m llama_cpp.server --config_file ./server_cfg.json
```

https://llama-cpp-python.readthedocs.io/en/latest/server/#configuration-and-multi-model-support

# Nuitka编译打包

TODO:command
