<script setup>
import { Form, Input, Button, Card } from "ant-design-vue";
import { UserOutlined, LockOutlined } from "@ant-design/icons-vue";
import { reactive } from "vue";
import { message } from "ant-design-vue";
import { useRouter } from "vue-router";
const [messageApi, contextHolder] = message.useMessage();

//屏幕背景动态
const particles = Array.from({ length: 12 }, (_, i) => ({
  id: i,
  left: Math.floor(Math.random() * 100),
  delay: Math.random(),
  duration: 5 + Math.random() * 5,
}));

const beams = Array.from({ length: 5 }, (_, i) => ({
  id: i,
  left: Math.floor(Math.random() * 100),
  delay: Math.random() * 2,
}));

//登录
const formState = reactive({
  username: "",
  password: "",
});
const router = useRouter();
function onLogin(values) {
  console.log(values);
  const { username, password } = values;

  if (username == "admin" && password == "123456") {
    info("登录成功");
    router.push("/");
  } else {
    info("用户名或密码错误");
  }
}
const onFinish = (values) => {
  onLogin(values);
};
const onFinishFailed = (errorInfo) => {
  console.log("Failed:", errorInfo);
  info();
};
const info = (msg = "请输入用户名或密码") => {
  messageApi.info(msg);
};
</script>

<template>
  <context-holder />
  <div class="login-container">
    <div class="particles">
      <div
        v-for="particle in particles"
        :key="particle.id"
        class="particle"
        :style="{
          left: `${particle.left}%`,
          animationDelay: `${particle.delay}s`,
          animationDuration: `${particle.duration}s`,
        }"
      ></div>
    </div>
    <div class="light-beams">
      <div
        v-for="beam in beams"
        :key="beam.id"
        class="beam"
        :style="{
          left: `${beam.left}%`,
          animationDelay: `${beam.delay}s`,
        }"
      ></div>
    </div>
    <div class="login-content">
      <Card class="login-card" :bordered="false">
        <div class="login-header">
          <div class="login-title">爬虫管理系统</div>
          <div class="login-subtitle">Crawler Management System</div>
        </div>

        <Form
          layout="vertical"
          class="login-form"
          :model="formState"
          @finish="onFinish"
          autocomplete="off"
          @finishFailed="onFinishFailed"
        >
          <Form.Item
            name="username"
            :rules="[{ required: true, message: 'Please input your username!' }]"
          >
            <Input v-model:value="formState.username" size="large" placeholder="用户名">
              <template #prefix>
                <UserOutlined />
              </template>
            </Input>
          </Form.Item>

          <Form.Item
            name="password"
            :rules="[{ required: true, message: 'Please input your password!' }]"
          >
            <Input.Password v-model:value="formState.password" size="large" placeholder="密码">
              <template #prefix>
                <LockOutlined />
              </template>
            </Input.Password>
          </Form.Item>

          <Form.Item>
            <Button html-type="submit" type="primary" size="large" block class="login-button">
              登录
            </Button>
          </Form.Item>
        </Form>
      </Card>
    </div>
  </div>
</template>

<style lang="less" scoped>
.login-container {
  height: 100vh;
  width: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
  background: linear-gradient(135deg, #1a237e 0%, #0277bd 100%);
  position: relative;
  overflow: hidden;

  &::before {
    content: "";
    position: absolute;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 60%);
    animation: rotate 30s linear infinite;
  }
}

// 粒子效果
.particles {
  position: absolute;
  width: 100%;
  height: 100%;
  z-index: 0;
}

.particle {
  position: absolute;
  width: 4px;
  height: 4px;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 50%;
  animation: particleFloat 5s ease-in-out infinite;
}

// 光束效果
.light-beams {
  position: absolute;
  width: 100%;
  height: 100%;
  z-index: 0;
}

.beam {
  position: absolute;
  width: 2px;
  height: 100%;
  background: linear-gradient(to bottom, transparent, rgba(255, 255, 255, 0.1), transparent);
  animation: beamMove 8s ease-in-out infinite;
}

// 登录卡片
.login-content {
  position: relative;
  z-index: 1;
  width: 100%;
  max-width: 420px;
  padding: 0 20px;
}

.login-card {
  backdrop-filter: blur(10px);
  background: rgba(255, 255, 255, 0.85);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  position: relative;
  overflow: hidden;

  &::before {
    content: "";
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: radial-gradient(circle, rgba(255, 255, 255, 0.1) 0%, transparent 60%);
    animation: cardGlow 10s linear infinite;
  }

  :deep(.ant-card-body) {
    padding: 40px;
    position: relative;
  }
}

// 登录表单样式
.login-header {
  text-align: center;
  margin-bottom: 40px;
}

.login-title {
  font-size: 28px;
  font-weight: bold;
  background: linear-gradient(45deg, #1a237e, #0277bd);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  margin-bottom: 8px;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.login-subtitle {
  font-size: 16px;
  color: #666;
  letter-spacing: 1px;
}

.login-form {
  :deep(.ant-input-affix-wrapper) {
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    background: rgba(255, 255, 255, 0.9);
    transition: all 0.3s;

    &:hover,
    &:focus {
      border-color: #1a237e;
      box-shadow: 0 0 0 2px rgba(26, 35, 126, 0.1);
    }
  }

  .login-button {
    height: 45px;
    border-radius: 8px;
    font-size: 16px;
    background: linear-gradient(45deg, #1a237e, #0277bd);
    border: none;
    box-shadow: 0 4px 15px rgba(26, 35, 126, 0.2);
    transition: all 0.3s;
    position: relative;
    overflow: hidden;

    &::before {
      content: "";
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
      transform: rotate(45deg);
      animation: buttonShine 3s ease-in-out infinite;
    }

    &:hover {
      transform: translateY(-2px);
      box-shadow: 0 6px 20px rgba(26, 35, 126, 0.3);
    }
  }
}

// 动画关键帧
@keyframes particleFloat {
  0%,
  100% {
    transform: translateY(0) scale(1);
    opacity: 0.5;
  }

  50% {
    transform: translateY(-100px) scale(1.2);
    opacity: 1;
  }
}

@keyframes beamMove {
  0% {
    transform: translateX(-100px) rotate(45deg);
    opacity: 0;
  }

  30% {
    transform: translateX(100px) rotate(45deg);
    opacity: 1;
  }

  100% {
    transform: translateX(300px) rotate(45deg);
    opacity: 0;
  }
}

@keyframes rotate {
  from {
    transform: rotate(0deg);
  }

  to {
    transform: rotate(360deg);
  }
}

@keyframes cardGlow {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

@keyframes buttonShine {
  0% {
    left: -50%;
  }

  100% {
    left: 100%;
  }
}
</style>
