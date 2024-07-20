<template>
  <div ref="barChart" style="width: 100%; height: 600px;"></div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  name: 'BarChart',
  props: {
    categories: {
      type: Array,
      required: true
    },
    data: {
      type: Array,
      required: true
    },
    title: {
      type: String,
    },
    value: {
      type: String,
      default: "Mean Value",
    },
    xAxisLabel: {
      type: String,
    },
    yAxisLabel: {
      type: String,
    }
  },
  mounted() {
    this.drawChart();
  },
  methods: {
    drawChart() {
      var myChart = echarts.init(this.$refs.barChart);

      var option = {
        title: {
          text: this.title
        },
        tooltip: {
          trigger: 'axis',
          axisPointer: {
            type: 'shadow'
          }
        },
        xAxis: {
          type: 'category',
          data: this.categories,
          axisLabel: {
            interval: 0,
            rotate: 45, // 增加旋转角度
            margin: 10, // 增加标签与轴线的间距
            textStyle: {
              fontSize: 15, // 调整字体大小
              color: "rgb(156, 147, 147)",
            }
          },
          splitLine: {
            lineStyle: {
              color: 'rgba(255, 255, 255, 0.1)' // 设置背景线条的颜色
            }
          }
        },
        yAxis: {
          type: 'value',
          name: this.yAxisLabel,
          splitLine: {
            lineStyle: {
              color: 'rgba(255, 255, 255, 0.1)' // 设置背景线条的颜色
            }
          }
        },
        series: [{
          name: this.value,
          type: 'bar',
          data: this.data,
          itemStyle: {
            color: '#b1ed4a'
          },
          label: {
            show: true,
            position: 'top',
            color: 'rgb(156, 147, 147)'
          }
        }]
      };

      myChart.setOption(option);
    }
  },
  watch: {
    categories: 'drawChart',
    data: 'drawChart'
  }
};
</script>

<style scoped>
</style>