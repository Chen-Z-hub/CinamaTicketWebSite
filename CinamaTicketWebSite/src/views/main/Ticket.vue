<template>
    <div>
        <br><br>
        <div class="if-movie">
            <img class="if-poster" :src="selectedMovie.poster" alt="电影海报" />
            <p>{{ selectedMovie.name }}</p>
        </div>
        <!-- <img :src="selectedMovie.poster" alt="poster" class="movie-poster">
        <p>{{selectedMovie.name}}</p> -->
        <Booking />
        <br><br><br><br>
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

    data(){
        return{

        }
    },
    components:{
        Booking
    },
    created() {
        
    },
    methods: {

    }
}
</script>

<style>
.if-movie{
  width: 100%;
}
.if-poster{
  width: 15%;
  justify-content: center; /* 水平居中 */
  align-items: center; /* 垂直居中 */
}
</style>