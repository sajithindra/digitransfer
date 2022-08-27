<template>
<v-app>
<v-container class="loginform">
	<v-form>
		<v-container class="sm-auto">
			<h1 class="text-center"> SWIFT Pay</h1>
			<v-col dense>
				<v-row>
					<v-text-field v-model="username" label="username"></v-text-field>
				</v-row>
				<v-row>
					<v-text-field v-model = "password" label ="password" type="password"></v-text-field>
				</v-row>
				<v-row>
					<v-btn text block oulined @click="signin" color="green" x-large> Sign in </v-btn>
				</v-row>
				<v-row>
					<v-btn text block oulined @click="signup" color="primary" x-large> Signup </v-btn>
				</v-row>
			</v-col>
		</v-container>
	</v-form>
</v-container>
</v-app>
</template>

<script>
export default {
  name: 'IndexPage',
  data : () => ({
	username: "",
	password:"",
  }),
  methods:{
	async signin(){
		this.$storage.setUniversal('username',this.username);
		let url = "http://127.0.0.1:8000/login"
		let logindata= {
			username : this.username,
			password : this.password
		}
		let res = await this.$axios.post(url,logindata);
		if (res.data == true){
			this.$router.push('/user')
		}
	},
	async signup(){
		this.$router.push('/signup');
	},
  },
}
</script>
<style>

.loginform{
	width: 500px;
	margin: 10% auto;
}
</style>
