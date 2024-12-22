<script setup>
import { onMounted, ref, onActivated, onDeactivated } from "vue";
import * as echarts from "echarts";
import { getPythonData } from "@/service/module/data";

// 添加组件名称
defineOptions({
  name: "echarts",
});

const chartData = ref([]);
const charts = ref([]); // 存储图表实例

// 初始化图表
const initCharts = (data) => {
  // 工作地点分布图
  const locationChart = echarts.init(document.getElementById("locationChart"));
  const locationData = {};
  data.forEach((item) => {
    const location = item.location_detail.split("-")[0];
    locationData[location] = (locationData[location] || 0) + 1;
  });

  locationChart.setOption({
    title: { text: "工作地点分布" },
    tooltip: {},
    xAxis: {
      data: Object.keys(locationData),
      axisLabel: { interval: 0, rotate: 45 },
    },
    yAxis: {},
    series: [
      {
        name: "职位数量",
        type: "bar",
        data: Object.values(locationData),
        itemStyle: {
          color: "#91cc75",
        },
      },
    ],
  });

  // 学历要求统计图
  const educationChart = echarts.init(document.getElementById("educationChart"));
  const educationData = {};
  data.forEach((item) => {
    educationData[item.academic] = (educationData[item.academic] || 0) + 1;
  });

  educationChart.setOption({
    title: { text: "学历要求分布" },
    tooltip: {
      trigger: "item",
      formatter: "{b}: {c} ({d}%)",
    },
    series: [
      {
        type: "pie",
        radius: "60%",
        data: Object.entries(educationData).map(([name, value]) => ({
          name,
          value,
        })),
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: "rgba(0, 0, 0, 0.5)",
          },
        },
      },
    ],
  });

  // 薪资区间分布图
  const salaryChart = echarts.init(document.getElementById("salaryChart"));
  const salaryRanges = {
    "0-100": 0,
    "100-200": 0,
    "200-300": 0,
    "300-400": 0,
    "400+": 0,
  };

  data.forEach((item) => {
    const salary = parseInt(item.day_salary);
    if (salary <= 100) salaryRanges["0-100"]++;
    else if (salary <= 200) salaryRanges["100-200"]++;
    else if (salary <= 300) salaryRanges["200-300"]++;
    else if (salary <= 400) salaryRanges["300-400"]++;
    else salaryRanges["400+"]++;
  });

  salaryChart.setOption({
    title: { text: "日薪资分布" },
    tooltip: {},
    xAxis: {
      data: Object.keys(salaryRanges),
    },
    yAxis: {},
    series: [
      {
        name: "职位数量",
        type: "bar",
        data: Object.values(salaryRanges),
        itemStyle: {
          color: "#5470c6",
        },
      },
    ],
  });

  // 工作频率分布图
  const frequencyChart = echarts.init(document.getElementById("frequencyChart"));
  const frequencyData = {};
  data.forEach((item) => {
    frequencyData[item.work_week] = (frequencyData[item.work_week] || 0) + 1;
  });

  frequencyChart.setOption({
    title: { text: "工作频率分布" },
    tooltip: {
      trigger: "item",
      formatter: "{b}: {c} ({d}%)",
    },
    series: [
      {
        type: "pie",
        radius: "60%",
        data: Object.entries(frequencyData).map(([name, value]) => ({
          name,
          value,
        })),
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: "rgba(0, 0, 0, 0.5)",
          },
        },
      },
    ],
  });

  // 保存图表实例
  charts.value = [locationChart, educationChart, salaryChart, frequencyChart];
};

// 监听窗口大小变化
const handleResize = () => {
  charts.value.forEach((chart) => {
    chart?.resize();
  });
};

// 组件被激活时（从缓存中恢复）
onActivated(() => {
  window.addEventListener("resize", handleResize);
  // 重新调整图表大小
  charts.value.forEach((chart) => {
    chart?.resize();
  });
});

// 组件被停用时（被缓存）
onDeactivated(() => {
  window.removeEventListener("resize", handleResize);
});

onMounted(async () => {
  try {
    const res = await getPythonData();
    if (res) {
      chartData.value = res;
      // 等待 DOM 更新后初始化图表
      setTimeout(() => {
        initCharts(res);
        window.addEventListener("resize", handleResize);
      }, 0);
    }
  } catch (error) {
    console.error("获取数据失败:", error);
  }
});
</script>

<template>
  <div class="echarts-container">
    <h2>数据可视化分析</h2>

    <div class="chart-grid">
      <a-card class="chart-container">
        <div id="locationChart" style="height: 400px"></div>
      </a-card>

      <a-card class="chart-container">
        <div id="educationChart" style="height: 400px"></div>
      </a-card>

      <a-card class="chart-container">
        <div id="salaryChart" style="height: 400px"></div>
      </a-card>

      <a-card class="chart-container">
        <div id="frequencyChart" style="height: 400px"></div>
      </a-card>
    </div>
  </div>
</template>

<style lang="less" scoped>
.echarts-container {
  padding: 24px;

  h2 {
    margin-bottom: 24px;
    color: #1a237e;
  }

  .chart-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;

    .chart-container {
      background: #fff;
      border-radius: 8px;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
    }
  }
}
</style>
