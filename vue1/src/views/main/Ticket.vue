<template>
    <div>
        <br><br>
        <img :src="selectedMovie.poster" alt="selectedMovie.poster" class="movie-poster">
        <p>{{name}}</p>
        <Booking @listReturned="handleListReturned"/>
    </div>
</template>

<script>
import Booking from '../../components/Booking.vue';
export default {
    computed: {
        selectedMovie() {
        return this.$store.state.selectedMovie; // 或者其他数据源
        },
    },
    created() {
        // 当组件创建时，从Vuex中同步selectedMovie的mid到form
        if (this.selectedMovie && this.selectedMovie.mid) {
            this.form.mid = this.selectedMovie.mid;
        }
    },
    data(){
        return{
            name:'',
            poster:''
        }
    },
    components:{
        Booking
    },
    created() {
        const name = this.$route.params.name;
        const poster = this.$route.params.poster;
        // 将获取到的name参数值赋给data中的name属性
        if (name) {
            this.name = name;
        }
        if (poster) {
            this.poster = poster;
        }
    },
    methods: {

    }
}
</script>

<style>

</style>