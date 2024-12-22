<script setup>
import { ref } from "vue";
import { message } from "ant-design-vue";

defineOptions({
  name: "users",
});

// 用户信息
const userInfo = ref({
  username: "张三",
  role: "普通用户",
  email: "zhangsan@example.com",
  phone: "13800138000",
  createTime: "2024-03-01",
  lastLogin: "2024-03-20 10:30:00",
});

// 修改密码表单
const passwordForm = ref({
  oldPassword: "",
  newPassword: "",
  confirmPassword: "",
});

// 表单验证规则
const passwordRules = {
  oldPassword: [{ required: true, message: "请输入原密码" }],
  newPassword: [
    { required: true, message: "请输入新密码" },
    { min: 6, message: "密码长度不能小于6位" },
  ],
  confirmPassword: [
    { required: true, message: "请确认新密码" },
    {
      validator: (_, value) => {
        if (value && value !== passwordForm.value.newPassword) {
          return Promise.reject("两次输入的密码不一致");
        }
        return Promise.resolve();
      },
    },
  ],
};

// 处理密码修改
const handlePasswordChange = () => {
  message.success("密码修改成功");
  passwordForm.value = {
    oldPassword: "",
    newPassword: "",
    confirmPassword: "",
  };
};

// 处理基本信息更新
const handleInfoUpdate = () => {
  message.success("个人信息更新成功");
};
</script>

<template>
  <div class="user-profile">
    <h2>个人中心</h2>

    <div class="profile-content">
      <!-- 基本信息卡片 -->
      <a-card title="基本信息" class="info-card">
        <a-descriptions :column="1">
          <a-descriptions-item label="用户名">
            {{ userInfo.username }}
          </a-descriptions-item>
          <a-descriptions-item label="用户角色">
            {{ userInfo.role }}
          </a-descriptions-item>
          <a-descriptions-item label="邮箱">
            {{ userInfo.email }}
          </a-descriptions-item>
          <a-descriptions-item label="手机号码">
            {{ userInfo.phone }}
          </a-descriptions-item>
          <a-descriptions-item label="注册时间">
            {{ userInfo.createTime }}
          </a-descriptions-item>
          <a-descriptions-item label="最后登录">
            {{ userInfo.lastLogin }}
          </a-descriptions-item>
        </a-descriptions>

        <template #extra>
          <a-button type="primary" @click="handleInfoUpdate"> 更新信息 </a-button>
        </template>
      </a-card>

      <!-- 修改密码卡片 -->
      <a-card title="修改密码" class="password-card">
        <a-form :model="passwordForm" :rules="passwordRules" layout="vertical">
          <a-form-item label="原密码" name="oldPassword">
            <a-input-password v-model:value="passwordForm.oldPassword" />
          </a-form-item>
          <a-form-item label="新密码" name="newPassword">
            <a-input-password v-model:value="passwordForm.newPassword" />
          </a-form-item>
          <a-form-item label="确认新密码" name="confirmPassword">
            <a-input-password v-model:value="passwordForm.confirmPassword" />
          </a-form-item>
          <a-form-item>
            <a-button type="primary" @click="handlePasswordChange"> 确认修改 </a-button>
          </a-form-item>
        </a-form>
      </a-card>
    </div>
  </div>
</template>

<style lang="less" scoped>
.user-profile {
  padding: 24px;

  h2 {
    margin-bottom: 24px;
    color: #1a237e;
  }

  .profile-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 24px;

    .info-card,
    .password-card {
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
    }

    :deep(.ant-card-head) {
      border-bottom: 1px solid #f0f0f0;
    }

    :deep(.ant-descriptions-item) {
      padding-bottom: 16px;
    }

    .password-card {
      :deep(.ant-form-item:last-child) {
        margin-bottom: 0;
      }
    }
  }
}
</style>
