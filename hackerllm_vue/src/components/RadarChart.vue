<template>
    <div ref="chart" style="width: 35%; height: 400px;"></div>
  </template>
  
  <script>
  import * as echarts from 'echarts';
  
  export default {
    name: 'RadarChart',
    props: {
      indicator: {
        type: Array,
        required: true
      },
      data: {
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
          tooltip: {},
          radar: {
            indicator: this.indicator,
            center: ['50%', '50%'],
            radius: '70%',
            splitNumber: 5,
            shape: 'circle',
            axisName: {
              formatter: function(value) {
                return value;
              },
              color: 'rgb(156, 147, 147)'
            },
            splitLine: {
              lineStyle: {
                color: [
                  '#373f4e',
                  '#373f4e',
                  '#373f4e',
                  '#373f4e',
                  '#373f4e'
                ].reverse()
              }
            },
            splitArea: {
              areaStyle: {
                color: ['#1d2532', '#161d2a'].reverse()
              }
            },
            axisLine: {
              lineStyle: {
                color: '#373f4e'
              }
            }
          },
          series: [{
            name: 'Radar Data',
            type: 'radar',
            data: [{
              value: this.data,
              name: 'Data',
              areaStyle: {
                color: '#3e5137'
              },
              lineStyle: {
                color: '#b1ed4a'
              }
            }]
          }]
        };
  
        chart.setOption(option);
      }
    }
  };
  </script>
  
  <style scoped>
  </style>
  