# 使用轻量级的 Python 3.12 镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY requirements.txt .

# 安装依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制所有项目文件到工作目录
COPY . .

# 默认容器启动命令 (运行主程序)
# 在 CI/CD 中，我们通常会覆盖这个命令来运行测试
CMD ["python", "app/app.py"]
