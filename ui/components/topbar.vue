<template>
<v-app-bar>
    <v-btn fab dark @click="home"><v-icon dark>mdi-home</v-icon></v-btn>
    <v-btn fab dark @click="logout"><v-icon dark>mdi-logout</v-icon></v-btn>
</v-app-bar>
</template>
<script>
export default{
    name: "topbar",
    data:()=>({
    }),
    methods:{
        async logout(){
            this.$router.push('/');
        },
        async home(){
            this.$router.push('/user');
        },
    }
}
</script>