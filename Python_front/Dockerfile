# 使用官方的 Node 镜像
FROM node:18

# 设置工作目录
WORKDIR /app

# 拷贝项目文件
COPY . .

# 安装依赖
RUN npm install

# 构建项目
RUN npm run build

# 启动 Nginx 或静态文件服务
CMD ["npm", "run", "dev"]

