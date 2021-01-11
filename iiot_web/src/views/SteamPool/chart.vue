<script>
import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  props: ['data'],
  data() {
      return {
          gradient: null,
          gradient2: null
      }
  },
  mounted () {
    this.gradient = this.$refs.canvas.getContext("2d").createLinearGradient(0, 0, 0, 450),
    this.gradient2 = this.$refs.canvas.getContext("2d").createLinearGradient(0, 0, 0, 450),
    this.gradient2.addColorStop(0, "rgba(0, 231, 255, 0.9)"),
    this.gradient2.addColorStop(.5, "rgba(0, 231, 255, 0.25)"),
    this.gradient2.addColorStop(1, "rgba(0, 231, 255, 0)"),
    this.gradient.addColorStop(0, "rgba(255, 0,0, 0.5)"),
    this.gradient.addColorStop(.5, "rgba(255, 0, 0, 0.25)"),
    this.gradient.addColorStop(1, "rgba(255, 0, 0, 0)"),
    this.data.datasets.forEach((element,index) => {
        if(index%2)
            element.backgroundColor = this.gradient;
        else
            element.backgroundColor = this.gradient2;
    });
    this.renderChart(this.data,{
                responsive: !0,
                maintainAspectRatio: !1
            })
  }
}
</script>

<style scoped>
</style>