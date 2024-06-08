<script setup>
import { ref, reactive } from 'vue'


const email = ref('')
const phone = ref('')
const gender = ref('')


const info = reactive({
    firstName: '',
    lastName: '',
    fullName: function () {
        console.log('******')
        if (this.firstName && this.lastName) {
            return this.firstName + ' ' + this.lastName;
        } else {
            return this.firstName || this.lastName;
        }
    },

    birthDay: '',
    birthMonth: '',
    birthYear: '',
    fullBirth: function () {
        console.log('======')
        if (this.birthDay < 31) {
            return this.birthDay + '-' + this.birthMonth + '-' + this.birthYear
        } else {
            console.log('ERROR')
        }
    },
})




</script>


<template>
    <div class="mainBody">
        <div class="guestForm">
            <h2>Guest Form</h2>
            <div class="form">
                <h6>Name</h6>
                <input v-model="info.firstName" placeholder="first name" />
                <input v-model="info.lastName" placeholder="last name" />
            </div>
            <div class="form">
                <h6>E-mail Address</h6>
                <input v-model="email" placeholder="example@example.com" style="width: 80%;" />
            </div>
            <div class="form">
                <h6>Phone</h6>
                <input v-model="phone" />
            </div>
            <div class="form">
                <h6>Gender</h6>
                <span class="genders">
                    <input type="radio" id="Male" value="Male" v-model="gender" />
                    <label for="Male">Male</label>
                </span>
                <span class="genders">
                    <input type="radio" id="Female" value="Female" v-model="gender" />
                    <label for="Female">Female</label>
                </span>
                <span class="genders">
                    <input type="radio" id="They" value="They" v-model="gender" />
                    <label for="They">They</label>
                </span>
                <span class="genders">
                    <input type="radio" id="Alien" value="Alien" v-model="gender" />
                    <label for="Alien">Alien</label>
                </span>
            </div>
            <div class="birthday">
                <h6>Birth</h6>
                <input v-model="info.birthDay" placeholder="DD" style="width: 26.5%;" />
                <select v-model="info.birthMonth" style="width: 26.5%; height: 30px;">
                    <option disabled value="">MM</option>
                    <option>January</option>
                    <option>Februry</option>
                    <option>March</option>
                    <option>April</option>
                    <option>May</option>
                    <option>June</option>
                    <option>July</option>
                    <option>August</option>
                    <option>September</option>
                    <option>October</option>
                    <option>November</option>
                    <option>December</option>
                </select>
                <input v-model="info.birthYear" placeholder="YY" style="width: 26.5%;" />
            </div>
            <div class="sendArea">
                <button v-on:click="send">:: SEND ::</button>
            </div>
        </div>
    </div>


</template>

<style scoped>
.mainBody {
    float: none;
    margin-left: 277px;
    height: 100%;
}

.guestForm {
    border: 0;
    width: 60%;
    padding: 30px 30px 80px 30px;
    margin: 50px auto 0px auto;
    background-color: #9162A6;
    color: #333333;
    border-radius: 10px;
}


h2 {
    background-color: #F3AE3F;
    width: 100%;
    margin: 10px auto 30px auto;
    padding: 10px 10px 10px 10px;
    text-align: center;

}

.form {
    border-style: dotted;
    background-color: #9162A6;
    padding: 5px;
    color: #F3AE3F;
    margin: 10px auto;
    width: 100%;
}

.birthday {
    border-style: dotted;
    padding: 5px;
    color: #F3AE3F;
    margin: 10px auto;
}

h6 {
    padding: 5px;
}

.genders {
    margin: 0 10px;
}

label {
    margin-left: 5px;
}

.sendArea {
    padding-top: 40px;
    text-align: center;
}

button {
    background-color: #F3AE3F;
    border: 0;
    width: 60%;
    height: 60px;
    border-radius: 50%;
}

button:hover {
    background-color: #633379;
    color: #f1b210;
}

@media screen and (max-width: 700px) {
    .mainBody {
        margin-left: 0;
        float: none;
        height: 100%;
        padding: 30px;
    }

    .genders {
        display: flex;
        width: 20%;
    }

}

@media screen and (max-width: 500px) {
    input {
        width: 80%;
    }

    button {
        width: 100%;
        border: 0;
        padding: 0;
        text-align: center;
    }
}


.result {
    border-style: dotted;
    width: 60%;
    padding: 30px;
    margin: 50px auto;
}
</style>