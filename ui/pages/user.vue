<template>
<v-app id="inspire">
    <v-app-bar app>
     <v-app-bar-nav-icon @click="home"></v-app-bar-nav-icon>


      <v-toolbar-title> SWIFTPay</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-icon><v-icon  @click="logout">mdi-logout-variant</v-icon></v-toolbar-icon>
    </v-app-bar>
    <v-main>
    <userview/>
    </v-main>
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