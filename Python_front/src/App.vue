<script setup>
import { Layout, Menu } from "ant-design-vue";
import {
  HomeOutlined,
  BarChartOutlined,
  TeamOutlined,
  SettingOutlined,
  BellOutlined,
  UserOutlined,
  LogoutOutlined,
} from "@ant-design/icons-vue";
import { ref, computed } from "vue";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();

// 根据当前路由路径设置选中的菜单项
const selectedKeys = computed(() => {
  const path = route.path;
  if (path === "/python") return ["1"];
  if (path === "/echarts") return ["2"];
  if (path === "/users") return ["3"];
  if (path === "/settings") return ["4"];
  return ["1"];
});

// 计算是否显示侧边栏
const showSidebar = computed(() => {
  return route.path !== "/login";
});

// 处理菜单点击
const handleMenuClick = (menu) => {
  switch (menu.key) {
    case "1":
      router.push("/python");
      break;
    case "2":
      router.push("/echarts");
      break;
    case "3":
      router.push("/users");
      break;
    case "4":
      router.push("/settings");
      break;
  }
};

// 模拟通知数据
const notifications = ref(3);

// 处理退出登录
const handleLogout = () => {
  router.push("/login");
};

// 添加需要缓存的路由名称
const includedRoutes = ["python", "echarts"];
</script>

<template>
  <div class="app-container">
    <!-- 使用条件渲染来控制布局 -->
    <template v-if="showSidebar">
      <Layout class="layout">
        <Layout.Sider class="sider" width="240">
          <div class="logo">
            <span>爬虫管理系统</span>
          </div>
          <Menu
            v-model:selectedKeys="selectedKeys"
            theme="dark"
            mode="inline"
            @click="handleMenuClick"
          >
            <Menu.Item key="1">
              <HomeOutlined />
              <span>数据展示</span>
            </Menu.Item>
            <Menu.Item key="2">
              <BarChartOutlined />
              <span>数据分析</span>
            </Menu.Item>
            <Menu.Item key="3">
              <TeamOutlined />
              <span>个人中心</span>
            </Menu.Item>
            <Menu.Item key="4">
              <SettingOutlined />
              <span>系统设置</span>
            </Menu.Item>
          </Menu>
        </Layout.Sider>
        <Layout>
          <Layout.Header class="header">
            <div class="header-right">
              <!-- 通知图标 -->
              <a-badge :count="notifications" class="notification-badge">
                <a-button type="link" class="icon-button">
                  <BellOutlined />
                </a-button>
              </a-badge>

              <!-- 用户下拉菜单 -->
              <a-dropdown>
                <a class="user-dropdown">
                  <UserOutlined />
                  <span class="username">张三</span>
                </a>
                <template #overlay>
                  <a-menu>
                    <a-menu-item key="profile" @click="router.push('/users')">
                      <UserOutlined />
                      个人中心
                    </a-menu-item>
                    <a-menu-item key="logout" @click="handleLogout">
                      <LogoutOutlined />
                      退出登录
                    </a-menu-item>
                  </a-menu>
                </template>
              </a-dropdown>
            </div>
          </Layout.Header>
          <Layout.Content class="content">
            <keep-alive include="python echarts">
              <router-view></router-view>
            </keep-alive>
          </Layout.Content>
        </Layout>
      </Layout>
    </template>

    <!-- 登录页面不显示侧边栏且不缓存 -->
    <template v-else>
      <router-view></router-view>
    </template>
  </div>
</template>

<style lang="less" scoped>
.app-container {
  height: 100vh;
  background: #f0f2f5;
}

.layout {
  min-height: 100vh;
  background: rgba(255, 255, 255, 0.9);
}

.sider {
  position: relative;
  z-index: 10;
  box-shadow: 2px 0 8px rgba(0, 0, 0, 0.15);

  .logo {
    height: 64px;
    padding: 16px;
    display: flex;
    align-items: center;
    background: #001529;
    overflow: hidden;

    .logo-img {
      width: 32px;
      height: 32px;
      margin-right: 8px;
    }

    span {
      color: white;
      font-size: 18px;
      font-weight: bold;
      white-space: nowrap;
    }
  }

  :deep(.ant-menu-item) {
    margin: 4px 0;

    &.ant-menu-item-selected {
      background: linear-gradient(90deg, #1890ff 0%, #096dd9 100%);
    }
  }
}

.header {
  background: white;
  padding: 0 24px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  display: flex;
  justify-content: flex-end;
  align-items: center;

  .header-right {
    display: flex;
    align-items: center;
    gap: 16px;

    .notification-badge {
      cursor: pointer;
    }

    .icon-button {
      font-size: 18px;
      padding: 0;
    }

    .user-dropdown {
      display: flex;
      align-items: center;
      gap: 8px;
      color: rgba(0, 0, 0, 0.85);
      cursor: pointer;
      padding: 4px 8px;
      border-radius: 4px;
      transition: all 0.3s;

      &:hover {
        background: rgba(0, 0, 0, 0.025);
      }

      .username {
        margin-left: 4px;
      }
    }
  }
}

.content {
  margin: 24px;
  padding: 24px;
  background: rgba(255, 255, 255, 0.95);
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
  backdrop-filter: blur(10px);
}

// 动画效果
:deep(.ant-menu-item),
.user-dropdown,
.icon-button {
  transition: all 0.3s;
}
</style>
