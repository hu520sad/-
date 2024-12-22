# 使用官方的 Python 镜像
FROM python:3.9

# 设置工作目录
WORKDIR /app

# 拷贝项目文件
COPY . .

# 更新 pip 到最新版本
RUN python -m pip install --upgrade pip

# 安装依赖
RUN pip install -r requirements.txt

# 暴露 5000 端口
EXPOSE 5000

# 启动 Flask
CMD ["python", "server.py"]
