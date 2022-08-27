<template>
<v-app>
<v-container class="loginform">
    <v-form>
        <v-container>
            <v-col>
                <v-row>
                    <v-text-field v-model="name" label="Name"></v-text-field>
                </v-row>
                <v-row>
                    <v-text-field v-model="mob" label="mob"></v-text-field>
                </v-row>
                <v-row>
                    <v-text-field v-model="username" label="username"></v-text-field>
                </v-row>
                <v-row>
                    <v-text-field v-model="password" label="password"></v-text-field> 
                </v-row>
                <v-row>
                    <v-btn text block @click="createuser"> Sign Up </v-btn>
                </v-row>
            </v-col>
        </v-container>
    </v-form>
</v-container>
</v-app>
</template>
<script>
export default {
    name : "signup",
    data:()=>({
        name: '',
        mob:'',
        username:'',
        password:'',
    }),
    methods:{
        async createuser(){
            let url = "http://127.0.0.1:8000/adduser";
            let userdata = {
                name : this.name,
                username : this.username,
                password : this.password,
                mob : this.mob
            };
            let res = await this.$axios.post(url,userdata);
            if (res.data == true){
                this.$router.push('/');
            }
        },  
    }
}
</script>