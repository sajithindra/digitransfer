<template>
<v-app id="inspire">
    <userview/>
</v-app>
</template>
<script>
export default {
    name : "user",
    data:()=>({}),
    methods:{
        async home(){
            window.location.reload();
        },
        async logout() {
            this.$router.push('/');
        },
    }
}
</script>