<template>
  <div>
    <div class="row">
      <div class="col-12">
        <card type="chart">
          <template slot="header">
            <div class="row">
              <div class="col-sm-6" :class="isRTL ? 'text-right' : 'text-left'">
                <h5 class="card-category">
                  SON 10 SİPARİŞ
                </h5>
                <h2 class="card-title">Sipariş Adeti</h2>
              </div>

              <div class="col-sm-6">
                <div
                  class="btn-group btn-group-toggle"
                  :class="isRTL ? 'float-left' : 'float-right'"
                  data-toggle="buttons"
                >
                  <label
                    v-for="(option, index) in bigLineChartCategories"
                    :key="option"
                    class="btn btn-sm btn-primary btn-simple"
                    :class="{ active: bigLineChart.activeIndex === index }"
                    :id="index"
                  >
                    <input
                      type="radio"
                      @click="initBigChart(index)"
                      name="options"
                      autocomplete="off"
                      :checked="bigLineChart.activeIndex === index"
                    />
                    {{ option }}
                  </label>
                </div>
              </div>
            </div>
          </template>
          <div class="chart-area">
            <line-chart
              style="height: 100%"
              ref="bigChart"
              chart-id="big-line-chart"
              :chart-data="bigLineChart.chartData"
              :gradient-colors="bigLineChart.gradientColors"
              :gradient-stops="bigLineChart.gradientStops"
              :extra-options="bigLineChart.extraOptions"
            >
            </line-chart>
          </div>
        </card>
      </div>
    </div>
    <div class="row">
      <div class="col-lg-4" :class="{ 'text-right': isRTL }">
        <card type="chart">
          <template slot="header">
            <h5 class="card-category">SON 6 AY VERİLEN SİPARİŞLER</h5>
            <h3 class="card-title">
              <i class="tim-icons icon-bell-55 text-primary"></i>
              {{ toplamaltı }}
            </h3>
          </template>
          <div class="chart-area" v-if="loadpurple">
            <line-chart
              style="height: 100%"
              chart-id="purple-line-chart"
              :chart-data="purpleLineChart.chartData"
              :gradient-colors="purpleLineChart.gradientColors"
              :gradient-stops="purpleLineChart.gradientStops"
              :extra-options="purpleLineChart.extraOptions"
            >
            </line-chart>
          </div>
        </card>
      </div>
      <div class="col-lg-4" :class="{ 'text-right': isRTL }">
        <card type="chart">
          <template slot="header">
            <h5 class="card-category">EN ÇOK SİPARİŞ VERENLER</h5>
            <h3 class="card-title">
              <i class="tim-icons icon-delivery-fast text-info"></i>
              Müşterilerin Toplam Sipariş Miktarları
            </h3>
          </template>
          <div class="chart-area" v-if="loadbar">
            <bar-chart
              style="height: 100%"
              chart-id="blue-bar-chart"
              :chart-data="blueBarChart.chartData"
              :extra-options="blueBarChart.extraOptions"
            >
            </bar-chart>
          </div>
        </card>
      </div>
      <div class="col-lg-4" :class="{ 'text-right': isRTL }">
        <card type="chart">
          <template slot="header">
            <h5 class="card-category">Süresi Geçen Sipariş Sayısı</h5>
            <h3 class="card-title">
              <i class="tim-icons icon-send text-success"></i> {{ toplamdate }}
            </h3>
          </template>
          <div class="chart-area" v-if="loadgreen">
            <line-chart
              style="height: 100%"
              chart-id="green-line-chart"
              :chart-data="greenLineChart.chartData"
              :gradient-stops="greenLineChart.gradientStops"
              :extra-options="greenLineChart.extraOptions"
            >
            </line-chart>
          </div>
        </card>
      </div>
    </div>
  </div>
</template>
<script>
import LineChart from "@/components/Charts/LineChart";
import BarChart from "@/components/Charts/BarChart";
import * as chartConfigs from "@/components/Charts/config";
import TaskList from "./Dashboard/TaskList";
import UserTable from "./Dashboard/UserTable";
import config from "@/config";

export default {
  components: {
    LineChart,
    BarChart,
    TaskList,
    UserTable
  },
  data() {
    return {
      totalgreen: [0, 0, 0, 0, 0, 0],
      totalpurple: [0, 0, 0, 0, 0, 0],
      totalorders: [],
      tempslit: [],
      toplamdate: 0,
      toplamaltı: 0,
      loadgreen: false,
      loadpurple: false,
      loadbar: false,
      customers: [],
      orders: [],
      cikolataOn: [],
      cilekOn: [],
      muzOn: [],
      bigLineChart: {
        allData: [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
        activeIndex: 0,
        chartData: {
          datasets: [{}],
          labels: ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        },
        extraOptions: chartConfigs.purpleChartOptions,
        gradientColors: config.colors.primaryGradient,
        gradientStops: [1, 0.4, 0],
        categories: []
      },
      purpleLineChart: {
        extraOptions: chartConfigs.purpleChartOptions,
        chartData: {
          labels: ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"],
          datasets: [
            {
              label: "Toplam",
              fill: true,
              borderColor: config.colors.danger,
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              pointBackgroundColor: config.colors.danger,
              pointBorderColor: "rgba(255,255,255,0)",
              pointHoverBackgroundColor: config.colors.danger,
              pointBorderWidth: 20,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 15,
              pointRadius: 4,
              data: [80, 100, 70, 80, 120, 80]
            }
          ]
        },
        gradientColors: config.colors.primaryGradient,
        gradientStops: [1, 0.2, 0]
      },
      greenLineChart: {
        extraOptions: chartConfigs.greenChartOptions,
        chartData: {
          labels: ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran"],
          datasets: [
            {
              label: "Süresi Geçen",
              fill: true,
              borderColor: config.colors.primary,
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              pointBackgroundColor: config.colors.primary,
              pointBorderColor: "rgba(255,255,255,0)",
              pointHoverBackgroundColor: config.colors.primary,
              pointBorderWidth: 20,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 15,
              pointRadius: 4,
              data: [0, 0, 0, 0, 0, 0]
            }
          ]
        },
        gradientColors: [
          "rgba(66,134,121,0.15)",
          "rgba(66,134,121,0.0)",
          "rgba(66,134,121,0)"
        ],
        gradientStops: [1, 0.4, 0]
      },
      blueBarChart: {
        extraOptions: chartConfigs.barChartOptions,
        chartData: {
          labels: ["a", "b", "c", "d", "e", "f"],
          datasets: [
            {
              label: "Toplam Adet",
              borderColor: config.colors.info,
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              data: [5, 8, 9, 1, 5, 3]
            }
          ]
        },
        gradientColors: config.colors.primaryGradient
      }
    };
  },
  computed: {
    enableRTL() {
      return this.$route.query.enableRTL;
    },
    isRTL() {
      return this.$rtl.isRTL;
    },
    bigLineChartCategories() {
      return this.$t("dashboard.chartCategories");
    }
  },
  methods: {
    getGreen() {
      var tempGreen = [];
      var ay = [0, 0, 0, 0, 0, 0];
      var toplam = 0;
      this.$axios.get("http://127.0.0.1:8000/orders/").then(res => {
        for (let i = 0; i < res.data.length; i++) {
          tempGreen = res.data[i].order_date.split("-");
          if (
            this.currentDateTime()
              .split("-")
              .join("") >= res.data[i].deadline.split("-").join("")
          ) {
            if (tempGreen[1] == "01") {
              ay[0]++;
            } else if (tempGreen[1] == "02") {
              ay[1]++;
            } else if (tempGreen[1] == "03") {
              ay[2]++;
            } else if (tempGreen[1] == "04") {
              ay[3]++;
            } else if (tempGreen[1] == "05") {
              ay[4]++;
            } else if (tempGreen[1] == "06") {
              ay[5]++;
            }
          }
        }
        for (let i = 0; i < 6; i++) {
          toplam += ay[i];
        }

        this.toplamdate = toplam;
        this.greenLineChart.chartData.datasets[0].data = ay;
        console.log(this.greenLineChart.chartData.datasets[0].data);
        this.loadgreen = true;
      });
    },
    getPurple() {
      this.$axios.get("http://127.0.0.1:8000/orders/").then(res => {
        this.totalorders = res.data;
        for (let i = 0; i < this.customers.length; i++) {
          this.customers[i].amount = 0;
        }
        this.$axios.get("http://127.0.0.1:8000/orderitems/").then(res => {
          for (let i = 0; i < this.totalorders.length; i++) {
            for (let j = 0; j < res.data.length; j++) {
              if (this.totalorders[i].order_id == res.data[j].order_id) {
                this.totalorders[i].amount = res.data[j].amount;
              }
            }
          }
          for (let i = 0; i < this.totalorders.length; i++) {
            this.temp = this.totalorders[i].order_date.split("-");
            this.toplamaltı += this.totalorders[i].amount;
            if (this.temp[1] == "01") {
              this.totalpurple[0] += this.totalorders[i].amount;
            } else if (this.temp[1] == "02") {
              this.totalpurple[1] += this.totalorders[i].amount;
            } else if (this.temp[1] == "03") {
              this.totalpurple[2] += this.totalorders[i].amount;
            } else if (this.temp[1] == "04") {
              this.totalpurple[3] += this.totalorders[i].amount;
            } else if (this.temp[1] == "05") {
              this.totalpurple[4] += this.totalorders[i].amount;
            } else if (this.temp[1] == "06") {
              this.totalpurple[5] += this.totalorders[i].amount;
            }
            this.purpleLineChart.chartData.datasets[0].data = this.totalpurple;
            this.loadpurple = true;
          }
        });
      });
    },
    loadData() {
      this.$axios.get("http://127.0.0.1:8000/orderitems/").then(res => {
        for (let i = res.data.length - 1; i >= 0; i--) {
          if (res.data[i].product_id == 20) {
            if (this.cikolataOn.length < 10) {
              this.cikolataOn.push(res.data[i].amount);
            }
          } else if (res.data[i].product_id == 21) {
            if (this.cilekOn.length < 10) {
              this.cilekOn.push(res.data[i].amount);
            }
          } else if (res.data[i].product_id == 22) {
            if (this.muzOn.length < 10) {
              this.muzOn.push(res.data[i].amount);
            }
          }
        }
        this.bigLineChart.allData = [this.cikolataOn, this.cilekOn, this.muzOn];
      });
    },
    initBigChart(index) {
      let chartData = {
        datasets: [
          {
            fill: true,
            borderColor: config.colors.primary,
            borderWidth: 2,
            borderDash: [],
            borderDashOffset: 0.0,
            pointBackgroundColor: config.colors.primary,
            pointBorderColor: "rgba(255,255,255,0)",
            pointHoverBackgroundColor: config.colors.primary,
            pointBorderWidth: 20,
            pointHoverRadius: 4,
            pointHoverBorderWidth: 15,
            pointRadius: 4,
            data: this.bigLineChart.allData[index]
          }
        ],
        labels: ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
      };
      this.$refs.bigChart.updateGradients(chartData);
      this.bigLineChart.chartData = chartData;
      this.bigLineChart.activeIndex = index;
    },
    getBar() {
      this.$axios.get("http://127.0.0.1:8000/customers/").then(res => {
        this.customers = res.data;
        for (let i = 0; i < this.customers.length; i++) {
          this.customers[i].adet = 0;
        }
        this.$axios.get("http://127.0.0.1:8000/orders/").then(res => {
          this.orders = res.data;
          this.$axios.get("http://127.0.0.1:8000/orderitems/").then(res => {
            for (let i = 0; i < this.orders.length; i++) {
              for (let j = 0; j < res.data.length; j++) {
                if (this.orders[i].order_id == res.data[j].order_id) {
                  this.orders[i].amount = res.data[j].amount;
                }
              }
            }
            //--------------
            for (let i = 0; i < this.orders.length; i++) {
              for (let j = 0; j < this.customers.length; j++) {
                if (
                  this.customers[j].customer_id == this.orders[i].customer_id
                ) {
                  this.customers[j].adet += this.orders[i].amount;
                }
              }
            }

            this.customers.sort((a, b) => (a.adet < b.adet ? 1 : -1));
            this.blueBarChart.chartData.labels = [
              this.customers[0].name,
              this.customers[1].name,
              this.customers[2].name,
              this.customers[3].name,
              this.customers[4].name,
              this.customers[5].name
            ];
            this.blueBarChart.chartData.datasets[0].data = [
              this.customers[0].adet,
              this.customers[1].adet,
              this.customers[2].adet,
              this.customers[3].adet,
              this.customers[4].adet,
              this.customers[5].adet
            ];
            this.loadbar = true;
          });
        });
      });
    },
    currentDateTime() {
      const current = new Date();
      const day0 =
        current.getDate() < 10 ? "0" + current.getDate() : current.getDate();

      const month0 =
        current.getMonth() + 1 < 10
          ? "0" + (current.getMonth() + 1)
          : current.getMonth() + 1;

      const date = current.getFullYear() + "-" + month0 + "-" + day0;

      const dateTime = date;

      return dateTime;
    }
  },
  mounted() {
    this.i18n = this.$i18n;
    if (this.enableRTL) {
      this.i18n.locale = "ar";
      this.$rtl.enableRTL();
    }
    this.initBigChart(0);
  },
  created() {
    this.getPurple();
    this.getBar();
    this.loadData();
    this.getGreen();
  },

  update() {},
  beforeDestroy() {
    if (this.$rtl.isRTL) {
      this.i18n.locale = "en";
      this.$rtl.disableRTL();
    }
  }
};
</script>
<style></style>
