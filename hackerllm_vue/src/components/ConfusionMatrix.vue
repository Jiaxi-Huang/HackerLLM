<template>
    <div ref="chart" style="width: 100%; height: 600px;"></div>
  </template>
  
  <script>
  import * as echarts from 'echarts';
  
  export default {
    name: 'ConfusionMatrix',
    props: {
      data: {
        type: Array,
        required: true
      },
      categories: {
        type: Array,
        required: true
      }
    },
    mounted() {
      this.drawChart();
    },
    methods: {
      drawChart() {
        var chart = echarts.init(this.$refs.chart);
  
        var option = {
          tooltip: {
            position: 'top',
            formatter: function (params) {
              return `fact: ${params.value[1]}<br>predict: ${params.value[0]}<br>sum: ${params.value[2]}`;
            }
          },
          grid: {
            left: '10%',
            right: '10%',
            top: '10%',
            bottom: '20%'
          },
          xAxis: {
            type: 'category',
            data: this.categories,
            splitArea: {
              show: true
            },
            axisLabel: {
              rotate: 45,
              interval: 0
            }
          },
          yAxis: {
            type: 'category',
            data: this.categories,
            splitArea: {
              show: true
            }
          },
          visualMap: {
            min: 0,
            max: 1,
            calculable: true,
            orient: 'horizontal',
            left: 'center',
            bottom: '5%',
            inRange: {
              color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
            }
          },
          series: [{
            name: 'Confusion Matrix',
            type: 'heatmap',
            data: this.data.map((item, i) => item.map((value, j) => [j, i, value])).flat(),
            label: {
              show: true,
              color: '#000'
            },
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
              }
            }
          }]
        };
  
        chart.setOption(option);
      }
    }
  };
  </script>
  
  <style scoped>
  </style>
  