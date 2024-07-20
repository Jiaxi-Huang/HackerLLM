<template>
    <v-main style="margin-top: 0; margin-bottom: 0; padding-top: 0; padding-bottom: 0;">
        <v-row>
          <div class="spacer"></div>
          <v-col>
              <span class="articleTitle">Data Analysis</span><br>
              <span class="articleSubTitle">What we have got</span>
              <v-divider></v-divider>
                  <v-row>
                    <v-col cols="12" md="4" offset="10">
                        <div style="height: 10px;"></div>
                    </v-col>
                  <v-col cols="11">
                  <p class="article">
                    This part analyzes the performance and strategies of the top 800 hackers based on data from machine usage, challenge completion, and sherlock completion. The data was filtered to exclude records with below-average completion rates. Descriptive statistics and principal component analysis (PCA) were used to identify key technologies and challenges. It recommends focusing on technologies like Reconnaissance and Password Cracking and prioritizing challenges such as Web, Crypto, and Reversing. It also highlights the importance of Linux and Windows knowledge due to their high attack rates. Correlation and clustering analyses suggest prioritizing related challenge and sherlock types to maximize learning efficiency. A moderate positive correlation between individual and team rankings indicates that better individual performance aligns with higher team success.
                  </p>
                </v-col>
                </v-row>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
          <div style="height: 100px;"></div>
          </v-col>
        </v-row>
        <v-row>
          <v-col offset="1">
              <span class="second-level-title">Machine Attack Part</span>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="6" offset="1">
            <BarChart :categories="MachineBarCategories" :data="MachineBarChartData" :title="MachineAttackPaths" />
          </v-col>
          <v-col cols="5">
            <p class="article">
              <br>

            </p>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="6" offset="1">
            <BarChart :categories="MachineMeanBarCategories" :data="MachineMeanBarChartData" :title="MachineAttackPaths" />
          </v-col>
          <v-col cols="4">
            <p class="article">
                <br>Analysis<br>
Considering the total frequency (count) of each technique's appearance among the top 800 individuals and the average completion number (mean), a principal component analysis (PCA) was conducted based on count and mean. <br>
The principal component is derived as 0.707count + 0.707mean, with a cumulative contribution rate reaching 0.91.<br>
The visualization results sorted in descending order by the principal component are shown in the chart.
            </p>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="6" offset="1">
            <RadarChart :indicator="MachineRadarIndicator" :data="MachineRadarData" />
          </v-col>
          <v-col cols="4">
            <p class="article">
                <br>
                Conclusion<br>
    The top 7 techniques are recommended for learning:<br>
    <ol>
        <li>Reconnaissance</li>
        <li>Password Reuse</li>
        <li>Password Cracking</li>
        <li>Injections</li>
        <li>Software & OS Exploitation</li>
        <li>Common Applications</li>
        <li>Web Site Structure Discovery</li>
        <li>Security Tools</li>
    </ol>
            </p>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
          <div style="height: 100px;"></div>
          </v-col>
        </v-row>
        <v-row>
          <v-col offset="1">
              <span class="second-level-title">Challenge Part</span>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="5" offset="1">
            <BarChart :categories="ChallengeBarCategories" :data="ChallengeBarChartData" :title="ChallengeCategories"/>
          </v-col>
          <v-col cols="5">
            <RadarChart :indicator="ChallengeRadarIndicator" :data="ChallengeRadarData" />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="10" offset="1">
            <p class="article">
              <br>
              Conclusion based on the average completion numbers: <br>The recommended order for completing challenges is Web, Crypto, Reversing, Misc, Forensics, Pwn, Hardware, Mobile, GamePwn, OSINT, Blockchain, and AI - ML.
            </p>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
          <div style="height: 100px;"></div>
          </v-col>
        </v-row>
        <v-row>
          <v-col offset="1">
              <span class="second-level-title">Sherlock Part</span>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="5" offset="1">
            <BarChart :categories="SherlockMeanBarCategories" :data="SherlockMeanBarChartData" :title="SherlockCategories"/>
          </v-col>
          <v-col cols="5">
            <RadarChart :indicator="SherlockRadarIndicator" :data="SherlockRadarData" />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="10" offset="1">
            <p class="article">
              <br>Conclusion based on the average completion numbers:<br> The recommended order for completing sherlocks is DFIR, SOC, Malware Analysis, Campaign, Cloud, and Threat Intelligence.
            </p>
          </v-col>

        </v-row>
        <v-row>
          <v-col>
          <div style="height: 100px;"></div>
          </v-col>
        </v-row>
        <v-row>
          <v-col offset="1">
              <span class="second-level-title">Target Operating System Part</span>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="5" offset="1">
            <BarChart :categories="SystemBarCategories" :data="SystemBarChartData" :title="SystemCategories"/>
          </v-col>
          <v-col cols="5">
            <p class="article">
              <br>Conclusion: The top 800 hackers typically target Linux and Windows systems. It is recommended to study knowledge related to Linux and Windows systems.

The average number of attacks for each system is as follows:
                <ol>
                  <li>Linux: 64.11</li>
                  <li>Windows: 24.38</li>
                  <li>Other: 0.78</li>
                  <li>FreeBSD: 0.51</li>
                  <li>OpenBSD: 0.49</li>
                  <li>Android: 0.32</li>
                  <li>Solaris: 0.16</li>
                </ol>

            </p>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
          <div style="height: 100px;"></div>
          </v-col>
        </v-row>
        <v-row>
          <v-col offset="1">
              <span class="second-level-title">Challenge Correlation Analysis</span>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <ConfusionMatrix :data="ChallengeMatrixData" :categories="ChallengeMatrixCategories" />
          </v-col>          
        </v-row>
        <v-row>
          <v-col cols="10" offset="1">
            <p class="article">The challenge types Reversing, Crypto, Pwn, Web, Misc, Forensics, Mobile, Hardware, and GamePwn exhibit a strong correlation. These challenges likely assess similar abilities and require similar skills and knowledge, meaning that completing one of these challenges can aid in completing the others.

The challenge type OSINT shows a weak correlation with other challenges. This type may involve a completely different field or skill set, so completing OSINT provides limited assistance in completing other challenges.

Conclusion: It is advisable to prioritize challenges with strong correlations: Web, Crypto, Reversing, Misc, Forensics, Pwn, Hardware, Mobile, GamePwn.






</p>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
          <div style="height: 100px;"></div>
          </v-col>
        </v-row>
        <v-row>
          <v-col offset="1">
              <span class="second-level-title">Sherlock Correlation Analysis</span>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <ConfusionMatrix :data="SherlockMatrixData" :categories="SherlockMatrixCategories" />
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="10" offset="1">
            <p class="article">The sherlock types DFIR, Cloud, Malware Analysis, Threat Intelligence, and Campaign exhibit a strong correlation. These sherlocks likely assess similar abilities and require similar skills and knowledge, meaning that completing one of these sherlocks can aid in completing the others.

The sherlock type SOC shows a weak correlation with other sherlocks. This type may involve a completely different field or skill set, so completing SOC provides limited assistance in completing other sherlocks.

Conclusion: It is advisable to prioritize sherlocks with strong correlations: DFIR, Malware Analysis, Campaign, Cloud, and Threat Intelligence.</p>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
          <div style="height: 100px;"></div>
          </v-col>
        </v-row>
        <v-row>
          <v-col offset="1">
              <span class="second-level-title">Rankings Correlation Analysis</span>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <ScatterChart :data="RankScatterData" xAxisLabel="Ranking" yAxisLabel="Team Ranking" />
          </v-col>
        </v-row>
        <v-row>
          <v-col  cols="10" offset="1">
            <p class="article">The correlation coefficient between individual ranking and team ranking is 0.57, indicating a moderate positive correlation between individual ranking and team ranking.</p>
          </v-col>
        </v-row>
    </v-main>
</template>



<script>
import BarChart from './BarChart.vue';
import ConfusionMatrix from './ConfusionMatrix.vue';
import RadarChart from './RadarChart.vue'
import ScatterChart from './ScatterChart.vue'
export default {
  components: {
    ConfusionMatrix,
    BarChart,
    RadarChart,
    ScatterChart,
  },
  data() {
    return {
        //Challenge Part
        ChallengeMatrixData: [
        [1, 0.86, 0.84, 0.73, 0.83, 0.84, 0.8, 0.47, 0.84, 0.79, 0.64, 0.6],
        [0.86, 1, 0.83, 0.72, 0.85, 0.79, 0.78, 0.47, 0.84, 0.79, 0.64, 0.63],
        [0.84, 0.83, 1, 0.67, 0.73, 0.7, 0.69, 0.43, 0.74, 0.7, 0.57, 0.6],
        [0.73, 0.72, 0.67, 1, 0.74, 0.73, 0.72, 0.47, 0.67, 0.61, 0.53, 0.52],
        [0.83, 0.85, 0.73, 0.74, 1, 0.78, 0.8, 0.63, 0.79, 0.77, 0.55, 0.55],
        [0.84, 0.79, 0.7, 0.73, 0.78, 1, 0.74, 0.49, 0.74, 0.66, 0.55, 0.53],
        [0.8, 0.78, 0.69, 0.72, 0.8, 0.74, 1, 0.49, 0.79, 0.78, 0.6, 0.54],
        [0.47, 0.47, 0.43, 0.47, 0.63, 0.49, 0.49, 1, 0.43, 0.41, 0.23, 0.24],
        [0.84, 0.84, 0.74, 0.67, 0.79, 0.74, 0.79, 0.43, 1, 0.82, 0.69, 0.59],
        [0.79, 0.79, 0.7, 0.61, 0.77, 0.66, 0.78, 0.41, 0.82, 1, 0.67, 0.59],
        [0.64, 0.64, 0.57, 0.53, 0.55, 0.55, 0.6, 0.23, 0.69, 0.67, 1, 0.57],
        [0.6, 0.63, 0.6, 0.52, 0.55, 0.53, 0.54, 0.24, 0.59, 0.59, 0.57, 1]
      ],
      ChallengeMatrixCategories: ['Reversing', 'Crypto', 'Pwn', 'Web', 'Misc', 'Forensics', 'Mobile', 'OSINT', 'Hardware', 'GamePwn', 'Blockchain', 'AI - ML'],
      
      //Sherlock混淆矩阵数据
      SherlockMatrixData: [
        [1, 0.81, 0.83, 0.46, 0.7, 0.67], 
        [0.81, 1, 0.79, 0.35, 0.69, 0.66],
        [0.83, 0.79, 1, 0.42, 0.69, 0.58],
        [0.46, 0.35, 0.42, 1, 0.33, 0.32],
        [0.7, 0.69, 0.69, 0.33, 1, 0.54],
        [0.67, 0.66, 0.58, 0.32, 0.54, 1]
      ],
      SherlockMatrixCategories: ['DFIR', 'Cloud', 'Malware Analysis', 'SOC', 'Threat Intelligence', 'Campaign'],
      
      MachineAttackPaths: "Machine Attack Paths",
      ChallengeCategories: "Challenge Categories",
      SherlockCategories: "Sherlock Categories",
      SystemCategories: "System Categories",

      //machine板块柱状图
      MachineBarCategories: ['Reconnaissance', 'Password Reuse', 'Password Cracking', 'Injections', 'Software & OS exploitation', 'Common Applications', 'Web Site Structure Discovery', 'Security Tools', 'Source Code Analysis', 'SUDO Exploitation', 'Authentication', 'Databases', 'Custom Applications', 'Configuration and Authorization', 'Protocols', 'Broken Authentication and Authorization', 'Fuzzing', 'User Enumeration', 'Active Directory', 'Reverse Engineering'],
      MachineBarChartData: [778.37, 759.59, 748.97, 745.81, 707.69, 700.23, 672.15, 422.61, 374.41, 327.21, 323.61, 297.85, 220.55, 142.28, 95.58, 89.88, 85.97, 79.15, 47.87, 36.32],

      //machine mean板块柱状图
      MachineMeanBarCategories: ['Reconnaissance', 'Software & OS exploitation', 'Injections', 'Security Tools', 'Password Reuse', 'Password Cracking', 'Web Site Structure Discovery', 'Common Applications'],
      MachineMeanBarChartData: [48.86, 34.91, 30.81, 30.71, 27.37, 26.32, 23.68, 22.39],

      //chanllenge模块柱状图
      ChallengeBarCategories: ['Web', 'Crypto', 'Reversing', 'Misc', 'Forensics', 'Pwn', 'Hardware', 'Mobile', 'GamePwn', 'OSINT', 'Blockchain', 'AI - ML'],
      ChallengeBarChartData: [15.26, 8.22, 7.59, 6.50, 6.45, 6.41, 4.20, 2.78, 1.76, 1.40, 1.05, 0.17],
      
      //sherlock mean板块柱状图
      SherlockMeanBarCategories: ['DFIR', 'SOC', 'Malware Analysis', 'Campaign', 'Cloud', 'Threat Intelligence'],
      SherlockMeanBarChartData: [3.65, 0.82, 0.49, 0.29, 0.16, 0.11],
      
      //system 板块柱状图
      SystemBarCategories: ['Linux', 'Windows', 'Other', 'FreeBSD', 'OpenBSD', 'Android', 'Solaris'],
      SystemBarChartData: [64.11, 24.38, 0.78, 0.51, 0.49, 0.32, 0.16],

      //machine板块雷达图
      MachineRadarIndicator: [
        { name: 'Software & OS exploitation', max: 35 },
        { name: 'Security Tools', max: 35 },
        { name: 'Common Applications', max: 35 },
        { name: 'Web Site Structure Discovery', max: 35 },
        { name: 'Injections', max: 35 },
        { name: 'Password Cracking', max: 35 },
        { name: 'Password Reuse', max: 35 },
        { name: 'Reconnaissance', max: 35 }
      ],
      MachineRadarData: [24.1, 27.5, 30.3, 21.5, 22.7, 22.7, 23.8, 24.1],

      //chanllenge模块雷达图
      ChallengeRadarIndicator: [
        { name: 'Web', max: 30 },
        { name: 'Misc', max: 30 },
        { name: 'GamePwn', max: 30 },
        { name: 'Mobile', max: 30 },
        { name: 'OSINT', max: 30 },
        { name: 'AI - ML', max: 30 },
        { name: 'Pwn', max: 30 },
        { name: 'Blockchain', max: 30 },
        { name: 'Crypto', max: 30 },
        { name: 'Forensics', max: 30 },
        { name: 'Reversing', max: 30 },
        { name: 'Hardware', max: 30 }
      ],
      ChallengeRadarData: [16.0, 13.2, 10.0, 16.4, 28.0, 2.9, 6.3, 8.0, 9.8, 10.7, 12.3, 10.0],
      
      //Sherlock模块雷达图
      SherlockRadarIndicator: [
        { name: 'Threat Intelligence', max: 50 },
        { name: 'DFIR', max: 50 },
        { name: 'SOC', max: 50 },
        { name: 'Campaign', max: 50 },
        { name: 'Cloud', max: 50 },
        { name: 'Malware Analysis', max: 50 }
      ],
      SherlockRadarData: [12.5, 11.3, 41.2, 5.9, 7.9, 9.6],
      
      //排名相关性散点图
      RankScatterData: [[1.0, 1.0], [4.0, 4.0], [6.0, 5.0], [6.0, 4.0], [7.0, 4.0], [10.0, 3.0], [11.0, 2.0], [12.0, 8.0], [15.0, 2.0], [18.0, 30.0], [16.0, 9.0], [21.0, 4.0], [22.0, 12.0], [24.0, 10.0], [25.0, 15.0], [28.0, 1.0], [30.0, 8.0], [32.0, 11.0], [770.0, 3.0], [35.0, 11.0], [38.0, 19.0], [39.0, 4.0], [41.0, 1.0], [44.0, 13.0], [47.0, 2.0], [48.0, 24.0], [51.0, 10.0], [426.0, 31.0], [53.0, 25.0], [54.0, 28.0], [55.0, 2.0], [56.0, 17.0], [57.0, 29.0], [447.0, 176.0], [62.0, 26.0], [66.0, 4.0], [65.0, 5.0], [70.0, 4.0], [555.0, 31.0], [73.0, 26.0], [734.0, 302.0], [76.0, 36.0], [75.0, 38.0], [78.0, 23.0], [778.0, 338.0], [797.0, 354.0], [525.0, 32.0], [80.0, 39.0], [81.0, 25.0], [85.0, 3.0], [712.0, 235.0], [87.0, 11.0], [93.0, 41.0], [94.0, 42.0], [496.0, 21.0], [98.0, 12.0], [99.0, 9.0], [102.0, 31.0], [123.0, 32.0], [104.0, 48.0], [105.0, 9.0], [107.0, 12.0], [491.0, 43.0], [117.0, 11.0], [120.0, 61.0], [121.0, 2.0], [124.0, 30.0], [126.0, 63.0], [127.0, 2.0], [117.0, 37.0], [125.0, 54.0], [131.0, 41.0], [118.0, 56.0], [133.0, 47.0], [136.0, 17.0], [154.0, 34.0], [246.0, 23.0], [145.0, 71.0], [698.0, 18.0], [207.0, 93.0], [153.0, 13.0], [151.0, 75.0], [216.0, 86.0], [156.0, 47.0], [159.0, 77.0], [161.0, 79.0], [178.0, 87.0], [162.0, 76.0], [163.0, 74.0], [165.0, 49.0], [158.0, 70.0], [168.0, 13.0], [169.0, 80.0], [171.0, 69.0], [171.0, 34.0], [352.0, 88.0], [173.0, 83.0], [174.0, 19.0], [468.0, 7.0], [231.0, 9.0], [181.0, 82.0], [183.0, 89.0], [502.0, 50.0], [189.0, 44.0], [194.0, 6.0], [695.0, 62.0], [196.0, 85.0], [198.0, 9.0], [220.0, 98.0], [760.0, 25.0], [201.0, 90.0], [203.0, 52.0], [291.0, 23.0], [204.0, 87.0], [299.0, 32.0], [758.0, 11.0], [416.0, 151.0], [534.0, 9.0], [209.0, 94.0], [465.0, 184.0], [266.0, 81.0], [518.0, 199.0], [221.0, 99.0], [394.0, 127.0], [225.0, 40.0], [228.0, 78.0], [229.0, 100.0], [232.0, 44.0], [760.0, 263.0], [443.0, 168.0], [263.0, 18.0], [308.0, 12.0], [275.0, 101.0], [241.0, 44.0], [242.0, 82.0], [243.0, 25.0], [244.0, 30.0], [281.0, 26.0], [253.0, 92.0], [329.0, 72.0], [258.0, 18.0], [324.0, 95.0], [260.0, 106.0], [370.0, 48.0], [262.0, 57.0], [264.0, 19.0], [271.0, 19.0], [272.0, 13.0], [615.0, 212.0], [676.0, 211.0], [273.0, 12.0], [242.0, 12.0], [276.0, 26.0], [276.0, 96.0], [279.0, 118.0], [427.0, 11.0], [517.0, 8.0], [282.0, 119.0], [283.0, 104.0], [264.0, 48.0], [285.0, 25.0], [288.0, 108.0], [359.0, 5.0], [157.0, 9.0], [321.0, 19.0], [331.0, 59.0], [416.0, 8.0], [304.0, 124.0], [307.0, 116.0], [307.0, 13.0], [309.0, 11.0], [309.0, 126.0], [314.0, 128.0], [348.0, 56.0], [316.0, 13.0], [319.0, 137.0], [788.0, 10.0], [177.0, 132.0], [323.0, 35.0], [328.0, 25.0], [329.0, 130.0], [186.0, 125.0], [333.0, 113.0], [334.0, 117.0], [340.0, 60.0], [341.0, 12.0], [456.0, 180.0], [749.0, 111.0], [414.0, 153.0], [473.0, 184.0], [349.0, 33.0], [351.0, 141.0], [355.0, 19.0], [358.0, 135.0], [360.0, 43.0], [732.0, 19.0], [364.0, 91.0], [325.0, 25.0], [562.0, 34.0], [368.0, 147.0], [393.0, 130.0], [372.0, 136.0], [375.0, 13.0], [376.0, 56.0], [377.0, 6.0], [377.0, 46.0], [404.0, 2.0], [353.0, 142.0], [386.0, 40.0], [516.0, 201.0], [389.0, 156.0], [390.0, 31.0], [391.0, 64.0], [510.0, 19.0], [399.0, 20.0], [641.0, 157.0], [401.0, 138.0], [435.0, 172.0], [441.0, 149.0], [476.0, 130.0], [410.0, 9.0], [252.0, 150.0], [648.0, 219.0], [727.0, 297.0], [607.0, 219.0], [496.0, 177.0], [417.0, 2.0], [419.0, 84.0], [544.0, 209.0], [420.0, 145.0], [427.0, 40.0], [736.0, 155.0], [431.0, 18.0], [406.0, 144.0], [432.0, 4.0], [433.0, 78.0], [426.0, 137.0], [436.0, 128.0], [420.0, 18.0], [450.0, 171.0], [452.0, 93.0], [297.0, 178.0], [690.0, 10.0], [718.0, 290.0], [461.0, 139.0], [461.0, 56.0], [500.0, 197.0], [464.0, 155.0], [466.0, 44.0], [469.0, 170.0], [469.0, 33.0], [470.0, 185.0], [475.0, 33.0], [477.0, 95.0], [600.0, 181.0], [480.0, 187.0], [324.0, 140.0], [478.0, 167.0], [604.0, 230.0], [683.0, 34.0], [520.0, 19.0], [484.0, 133.0], [485.0, 157.0], [784.0, 240.0], [489.0, 9.0], [537.0, 62.0], [720.0, 18.0], [517.0, 130.0], [345.0, 32.0], [696.0, 204.0], [623.0, 219.0], [503.0, 37.0], [554.0, 18.0], [504.0, 198.0], [634.0, 50.0], [626.0, 179.0], [506.0, 152.0], [507.0, 50.0], [507.0, 152.0], [509.0, 41.0], [585.0, 213.0], [506.0, 84.0], [737.0, 304.0], [514.0, 111.0], [363.0, 26.0], [516.0, 56.0], [518.0, 11.0], [470.0, 49.0], [691.0, 83.0], [618.0, 10.0], [560.0, 34.0], [524.0, 34.0], [561.0, 129.0], [797.0, 57.0], [418.0, 71.0], [569.0, 215.0], [775.0, 32.0], [537.0, 121.0], [693.0, 278.0], [487.0, 33.0], [603.0, 4.0], [561.0, 130.0], [563.0, 2.0], [544.0, 21.0], [587.0, 226.0], [397.0, 26.0], [549.0, 159.0], [550.0, 202.0], [786.0, 329.0], [550.0, 212.0], [614.0, 13.0], [554.0, 195.0], [782.0, 344.0], [671.0, 264.0], [628.0, 243.0], [591.0, 220.0], [593.0, 40.0], [594.0, 40.0], [560.0, 191.0], [593.0, 171.0], [594.0, 181.0], [557.0, 11.0], [599.0, 225.0], [563.0, 162.0], [771.0, 146.0], [651.0, 127.0], [608.0, 4.0], [600.0, 26.0], [423.0, 218.0], [569.0, 3.0], [643.0, 8.0], [572.0, 222.0], [744.0, 270.0], [573.0, 158.0], [648.0, 254.0], [746.0, 306.0], [439.0, 6.0], [683.0, 244.0], [584.0, 225.0], [716.0, 11.0], [618.0, 131.0], [590.0, 190.0], [777.0, 235.0], [701.0, 282.0], [625.0, 18.0], [596.0, 150.0], [746.0, 186.0], [682.0, 269.0], [744.0, 310.0], [670.0, 254.0], [674.0, 267.0], [603.0, 40.0], [637.0, 62.0], [621.0, 138.0], [516.0, 21.0], [472.0, 40.0], [796.0, 219.0], [608.0, 176.0], [640.0, 12.0], [609.0, 212.0], [780.0, 341.0], [651.0, 182.0], [617.0, 44.0], [775.0, 337.0], [652.0, 214.0], [652.0, 213.0], [621.0, 19.0], [654.0, 34.0], [725.0, 153.0], [745.0, 40.0], [626.0, 243.0], [498.0, 239.0], [630.0, 244.0], [664.0, 260.0], [635.0, 19.0], [657.0, 249.0], [637.0, 88.0], [516.0, 44.0], [583.0, 11.0], [673.0, 241.0], [642.0, 25.0], [698.0, 256.0], [791.0, 351.0], [646.0, 4.0], [527.0, 252.0], [657.0, 259.0], [687.0, 275.0], [783.0, 326.0], [721.0, 56.0], [659.0, 25.0], [720.0, 268.0], [660.0, 258.0], [664.0, 9.0], [694.0, 46.0], [665.0, 18.0], [704.0, 102.0], [708.0, 64.0], [668.0, 21.0], [669.0, 263.0], [720.0, 167.0], [726.0, 226.0], [646.0, 299.0], [670.0, 6.0], [558.0, 21.0], [763.0, 21.0], [672.0, 266.0], [672.0, 3.0], [675.0, 57.0], [675.0, 224.0], [705.0, 21.0], [677.0, 44.0], [570.0, 34.0], [573.0, 31.0], [597.0, 30.0], [714.0, 288.0], [685.0, 44.0], [719.0, 199.0], [746.0, 28.0], [686.0, 21.0], [766.0, 57.0], [689.0, 216.0], [800.0, 360.0], [797.0, 357.0], [775.0, 314.0], [697.0, 59.0], [600.0, 279.0], [781.0, 341.0], [726.0, 86.0], [732.0, 21.0], [701.0, 193.0], [703.0, 164.0], [702.0, 283.0], [796.0, 133.0], [754.0, 268.0], [708.0, 298.0], [738.0, 163.0], [679.0, 269.0], [713.0, 133.0], [743.0, 309.0], [716.0, 288.0], [777.0, 30.0], [765.0, 324.0], [753.0, 21.0], [717.0, 223.0], [743.0, 191.0], [720.0, 283.0], [741.0, 18.0], [774.0, 335.0], [722.0, 18.0], [694.0, 221.0], [727.0, 101.0], [728.0, 131.0], [753.0, 26.0], [755.0, 314.0], [776.0, 338.0], [776.0, 320.0], [566.0, 207.0], [731.0, 176.0], [773.0, 60.0], [767.0, 326.0], [737.0, 279.0], [738.0, 276.0], [738.0, 176.0], [739.0, 6.0], [696.0, 327.0], [742.0, 25.0], [775.0, 337.0], [772.0, 182.0], [744.0, 18.0], [744.0, 293.0], [747.0, 313.0], [749.0, 193.0], [773.0, 212.0], [750.0, 122.0], [750.0, 291.0], [751.0, 315.0], [774.0, 336.0], [777.0, 212.0], [783.0, 341.0], [757.0, 296.0], [755.0, 319.0], [782.0, 47.0], [756.0, 6.0], [791.0, 163.0], [756.0, 320.0], [784.0, 80.0], [689.0, 322.0], [760.0, 324.0], [660.0, 56.0], [695.0, 26.0], [794.0, 356.0], [762.0, 304.0], [763.0, 86.0], [788.0, 13.0], [766.0, 144.0], [735.0, 146.0], [767.0, 46.0], [793.0, 190.0], [770.0, 224.0], [793.0, 296.0], [792.0, 351.0], [774.0, 191.0], [781.0, 3.0], [798.0, 358.0], [777.0, 339.0], [799.0, 33.0], [773.0, 188.0], [780.0, 34.0], [756.0, 320.0], [779.0, 341.0], [798.0, 237.0], [779.0, 335.0], [781.0, 121.0], [780.0, 342.0], [785.0, 3.0], [782.0, 336.0], [783.0, 222.0], [797.0, 269.0], [791.0, 382.0], [785.0, 108.0], [787.0, 349.0], [788.0, 10.0], [736.0, 19.0], [799.0, 8.0], [777.0, 289.0], [793.0, 18.0], [794.0, 335.0], [795.0, 335.0], [797.0, 23.0], [796.0, 18.0], [798.0, 9.0], [799.0, 311.0], [800.0, 342.0], [800.0, 115.0], [757.0, 362.0], [795.0, 269.0], [785.0, 317.0], [785.0, 379.0], [793.0, 311.0], [800.0, 359.0], [781.0, 224.0], [770.0, 368.0], [790.0, 382.0], [795.0, 361.0], [780.0, 376.0]],
    };
  }
};
</script>
<style>
  .article{
    font-family: Arial, sans-serif;
    font-size: 1.75em;
    line-height: 1.5;
    color: white;
  }
  .articleTitle{
    font-family: Arial, sans-serif;
    font-size: 5em;
    font-weight: bold;
    line-height: 1.5;
    color: white;
    text-decoration: underline
  }
  .articleSubTitle{
    font-family: Arial, sans-serif;
    font-size: 1.75em;
    line-height: 1.0;
    color: rgb(156, 147, 147);
  }
  .second-level-title{
    font-family: Arial, sans-serif;
    font-size: 4em;
    font-style: italic;
    line-height: 1.5;
    color: rgb(200, 186, 186);
  }
</style>