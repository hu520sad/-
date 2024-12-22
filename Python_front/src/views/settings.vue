<script setup>
import { ref } from "vue";
import { message } from "ant-design-vue";

defineOptions({
  name: "settings",
});

// 系统设置表单数据
const formState = ref({
  siteName: "爬虫管理系统",
  siteDescription: "专注于招聘数据分析的管理平台",
  emailNotification: true,
  dataBackup: true,
  backupFrequency: "daily",
  theme: "light",
  language: "zh_CN",
});

// 处理表单提交
const handleSubmit = () => {
  message.success("设置保存成功");
};

// 处理重置
const handleReset = () => {
  formState.value = {
    siteName: "爬虫管理系统",
    siteDescription: "专注于招聘数据分析的管理平台",
    emailNotification: true,
    dataBackup: true,
    backupFrequency: "daily",
    theme: "light",
    language: "zh_CN",
  };
  message.info("设置已重置");
};
</script>

<template>
  <div class="settings-container">
    <h2>系统设置</h2>

    <a-card>
      <a-tabs>
        <!-- 基础设置 -->
        <a-tab-pane key="1" tab="基础设置">
          <a-form :model="formState" layout="vertical" @finish="handleSubmit">
            <a-form-item label="系统名称" name="siteName">
              <a-input v-model:value="formState.siteName" />
            </a-form-item>

            <a-form-item label="系统描述" name="siteDescription">
              <a-textarea v-model:value="formState.siteDescription" :rows="4" />
            </a-form-item>

            <a-form-item label="主题设置" name="theme">
              <a-radio-group v-model:value="formState.theme">
                <a-radio value="light">浅色</a-radio>
                <a-radio value="dark">深色</a-radio>
              </a-radio-group>
            </a-form-item>

            <a-form-item label="语言设置" name="language">
              <a-select v-model:value="formState.language">
                <a-select-option value="zh_CN">简体中文</a-select-option>
                <a-select-option value="en_US">English</a-select-option>
              </a-select>
            </a-form-item>
          </a-form>
        </a-tab-pane>

        <!-- 通知设置 -->
        <a-tab-pane key="2" tab="通知设置">
          <a-form :model="formState" layout="vertical">
            <a-form-item name="emailNotification">
              <a-checkbox v-model:checked="formState.emailNotification"> 启用邮件通知 </a-checkbox>
            </a-form-item>

            <a-form-item
              label="通知邮箱"
              name="notificationEmail"
              v-if="formState.emailNotification"
            >
              <a-input placeholder="请输入接收通知的邮箱地址" />
            </a-form-item>
          </a-form>
        </a-tab-pane>

        <!-- 数据备份 -->
        <a-tab-pane key="3" tab="数据备份">
          <a-form :model="formState" layout="vertical">
            <a-form-item name="dataBackup">
              <a-checkbox v-model:checked="formState.dataBackup"> 启用自动备份 </a-checkbox>
            </a-form-item>

            <a-form-item label="备份频率" name="backupFrequency" v-if="formState.dataBackup">
              <a-select v-model:value="formState.backupFrequency">
                <a-select-option value="daily">每天</a-select-option>
                <a-select-option value="weekly">每周</a-select-option>
                <a-select-option value="monthly">每月</a-select-option>
              </a-select>
            </a-form-item>

            <a-form-item>
              <a-button type="primary" @click="handleSubmit"> 立即备份 </a-button>
            </a-form-item>
          </a-form>
        </a-tab-pane>
      </a-tabs>

      <div class="form-actions">
        <a-button type="primary" @click="handleSubmit"> 保存设置 </a-button>
        <a-button style="margin-left: 8px" @click="handleReset"> 重置 </a-button>
      </div>
    </a-card>
  </div>
</template>

<style lang="less" scoped>
.settings-container {
  padding: 24px;

  h2 {
    margin-bottom: 24px;
    color: #1a237e;
  }

  :deep(.ant-card) {
    border-radius: 8px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
  }

  .form-actions {
    margin-top: 24px;
    padding-top: 24px;
    border-top: 1px solid #f0f0f0;
  }

  :deep(.ant-tabs-nav) {
    margin-bottom: 24px;
  }
}
</style>
