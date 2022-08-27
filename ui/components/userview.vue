<template>
<v-container >
    <v-container class="form" v-if="showinfo">
        <v-container>
            <v-sheet>
            <br/>
                <v-container>
                    <h1 class="text-center"> Bal. {{fundstate}} </h1>
                </v-container>
                <v-container>
                    <v-btn text block color="teal" @click="showfund"> Show Fund </v-btn>
                </v-container>
                </v-sheet>
        </v-container>
        <v-container>
            <v-row>
                <v-col>
                    <v-btn text block color="secondary" @click="addfund"> Add fund</v-btn>
                </v-col>
                <v-col>
                    <v-btn text block color="teal" @click="sendfund"> Send fund</v-btn>
                </v-col>
            </v-row>
        </v-container>
    </v-container>
<v-container v-if="addfundshow" class="form">
        <h1 class="text-center">Deposit Transaction Details</h1>
        <br/>
        <v-form>
            <v-col>
                <v-row>
                    <v-text-field v-model="transactionid" label="Transaction ID"></v-text-field>
                </v-row>
                <v-row>
                    <v-text-field v-model="credit" label="Amount"></v-text-field>
                </v-row>
                <v-row>
                    <v-btn text block color="teal" @click="addfundupdate">Submit </v-btn>
                </v-row>
            </v-col>
        </v-form>
</v-container>
<v-container v-if="sendfundshow" class="form">
    <h1 class="text-center">Send Money </h1>
    <br/>
    <v-form>
        <v-col>
            <v-row>
                <v-text-field v-model="receiver" label="Reciever ID"></v-text-field>
            </v-row>
            <v-row>
                <v-text-field v-model="fund" label="Amount"></v-text-field>
            </v-row>
            <v-row>
                <v-btn text block color="teal" @click="sendfundupdate"> Send</v-btn>
            </v-row>
        </v-col>
    </v-form>
</v-container>
</v-container>


</template>
<script>
export default{
    name : "userview",
    mounted(){
        this.username = this.$storage.getUniversal('username');
    },
    data: ()=>({
        username: '',
        fundstate: "**********",
        transactionid:'',
        credit:0,
        receiver:'',
        fund:0,
        addfundshow: false,
        sendfundshow: false,
        showinfo: true,
    }),
    methods: {
        async showfund() {
            let url = "http://127.0.0.1:8000/userdetails";
            let userdata= {
                username: this.username,
            }
            let res = await this.$axios.post(url,userdata);
            this.fundstate = res.data.wallet;
        },
        async addfund() {
            this.showinfo=false;
            this.addfundshow = true;
            this.sendfundshow =false;
            console.log('addfund is already in progress');
        },
        async sendfund() {
            this.showinfo=false;
            this.addfundshow = false;
            this.sendfundshow = true;
            console.log('sendfund is already in progress');
        },
        async addfundupdate(){
            let url = "http://127.0.0.1:8000/addmoney";
            let money = {
                username : this.username,
                credit : this.credit,
                transactionid : this.transactionid
            };
            let res = await this.$axios.post(url,money);
            if (res.data == true){
                this.showinfo=true;
                this.addfundshow =false;
            }
            window.location.reload();
        },
        async sendfundupdate() {
            let url = "http://127.0.0.1:8000/transfer";
            let tranfer = {
                sender : this.username,
                receiver : this.receiver,
                fund : this.fund,
            }
            let res = await this.$axios.post(url,tranfer);
            if (res.data == true) {
                this.showinfo=true;
                this.sendfundshow =false;
            }
            window.location.reload();
        },
        
    }
}
</script>
<style>
.form{
    width: 500px;
    margin: 10% auto;
}
</style>