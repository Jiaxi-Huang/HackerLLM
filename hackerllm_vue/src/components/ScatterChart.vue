<template>
    <div ref="chart" style="width: 100%; height: 900px;"></div>
  </template>
  
  <script>
import * as echarts from 'echarts';
  
  export default {
    name: 'ScatterChart',
    props: {
      data: {
        type: Array,
        required: true
      },
      xAxisLabel: {
        type: String,
        default: 'Ranking'
      },
      yAxisLabel: {
        type: String,
        default: 'Team Ranking'
      },
      title: {
        type: String,
        default: ''
      }
    },
    mounted() {
      this.drawChart();
    },
    methods: {
      drawChart() {
        var chart = echarts.init(this.$refs.chart);
  
        var option = {
          title: {
            text: this.title,
          },
          tooltip: {
            trigger: 'item',
            formatter: function (params) {
              return 'Ranking: ' + params.value[0] + '<br>Team Ranking: ' + params.value[1];
            }
          },
          xAxis: {
            name: this.xAxisLabel,
            type: 'value'
          },
          yAxis: {
            name: this.yAxisLabel,
            type: 'value'
          },
          series: [{
            name: 'Scatter Data',
            type: 'scatter',
            data: this.data,
            itemStyle: {
              color: '#1f78b4'
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
  