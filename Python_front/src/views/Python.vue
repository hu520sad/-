<script setup>
import { getPythonData } from "@/service/module/data";
import { onMounted, ref, h } from "vue";
import { Tooltip } from "ant-design-vue";

// 添加组件名称
defineOptions({
  name: "python",
});

const tableData = ref([]);
const loading = ref(true);

const columns = [
  {
    title: "职位信息",
    children: [
      {
        title: "职位名称",
        dataIndex: "title",
        key: "title",
        width: 120,
      },
      {
        title: "薪资",
        dataIndex: "day_salary",
        key: "day_salary",
        width: 120,
      },
      {
        title: "工作地点",
        dataIndex: "location_detail",
        key: "location_detail",
        ellipsis: true,
        width: 200,
      },
    ],
  },
  {
    title: "要求信息",
    children: [
      {
        title: "学历要求",
        dataIndex: "academic",
        key: "academic",
        width: 100,
      },
      {
        title: "实习时长",
        dataIndex: "practice_time",
        key: "practice_time",
        width: 120,
      },
      {
        title: "工作频率",
        dataIndex: "work_week",
        key: "work_week",
        width: 100,
      },
    ],
  },
  {
    title: "职位详情",
    dataIndex: "job_detail",
    key: "job_detail",
    ellipsis: true,
    customRender: ({ text }) => {
      return h(
        Tooltip,
        {
          title: text,
          placement: "topLeft",
        },
        () => h("span", text)
      );
    },
  },
  {
    title: "更新时间",
    dataIndex: "update_time",
    key: "update_time",
    width: 160,
  },
  {
    title: "操作",
    key: "action",
    fixed: "right",
    width: 100,
    customRender: ({ record }) => {
      return h(
        "a",
        {
          href: record.page_url,
          target: "_blank",
        },
        "查看详情"
      );
    },
  },
];

onMounted(async () => {
  try {
    const res = await getPythonData();
    console.log("API Response:", res);
    if (res) {
      tableData.value = res.map((item, index) => ({
        ...item,
        key: index,
      }));
    }
  } catch (error) {
    console.error("Failed to fetch data:", error);
  } finally {
    loading.value = false;
  }
});
</script>

<template>
  <div class="python-container">
    <div class="header-section">
      <h2>实习岗位数据展示</h2>
      <div class="stats-cards">
        <a-card class="stat-card">
          <template #title>总数据量</template>
          <template #extra>
            <a-tag color="blue">{{ tableData.length }}</a-tag>
          </template>
          <p>当前爬取的岗位数量</p>
        </a-card>
      </div>
    </div>

    <a-card class="table-card">
      <a-table
        :columns="columns"
        :data-source="tableData"
        :loading="loading"
        :scroll="{ x: 1500 }"
        :pagination="{
          total: tableData.length,
          pageSize: 10,
          showSizeChanger: true,
          showQuickJumper: true,
        }"
      >
      </a-table>
    </a-card>
  </div>
</template>

<style lang="less" scoped>
.python-container {
  padding: 24px;

  .header-section {
    margin-bottom: 24px;

    h2 {
      margin-bottom: 16px;
      color: #1a237e;
    }

    .stats-cards {
      display: flex;
      gap: 16px;
      margin-bottom: 24px;

      .stat-card {
        flex: 1;
        max-width: 300px;
      }
    }
  }

  .table-card {
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
  }

  :deep(.ant-table) {
    background: #fff;
  }

  :deep(.ant-table-thead > tr > th) {
    background: #f5f5f5;
  }

  :deep(.ant-table-tbody > tr:hover > td) {
    background: #f0f7ff;
  }
}
</style>
