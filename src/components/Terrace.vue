<script setup>
import { ref } from 'vue'
const checkedNames = ref([])
const picked = ref('')
const selected = ref('')
</script>


<template>
    <div class="terrace">
        <div class="container">
            <div class="row">
                <div class="col-sm-2"></div>
                <div class="col-sm-10">
                    <h1>hey ?!</h1>

                    <div class="checkName">

                        <input type="checkbox" id="jack" value="Jack" v-model="checkedNames" />
                        <label for="jack">Jack</label>

                        <input type="checkbox" id="john" value="John" v-model="checkedNames" />
                        <label for="john">John</label>

                        <input type="checkbox" id="mike" value="Mike" v-model="checkedNames" />
                        <label for="mike">Mike</label>
                    </div>

                    <div class="pickOne">
                        <input type="radio" id="one" value="One" v-model="picked" />
                        <label for="one">One</label>

                        <input type="radio" id="two" value="Two" v-model="picked" />
                        <label for="two">Two</label>

                        <input type="radio" id="three" value="Three" v-model="picked" />
                        <label for="three">Three</label>
                    </div>

                    <div class="selection">

                        <div>
                            <select v-model="selected">
                                <option disabled value="">Please select one</option>
                                <option>A</option>
                                <option>B</option>
                                <option>C</option>
                            </select>
                        </div>

                        <h5>Checked names: {{ checkedNames }}</h5>
                        <h5>Picked: {{ picked }}</h5>
                        <h5> Selected: {{ selected }}</h5>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>



<style scoped></style>