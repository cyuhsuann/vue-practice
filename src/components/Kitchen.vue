<script setup>
import { ref, reactive } from 'vue'

const todoList = reactive({
    title: '',
    addlist: '',
    lists: [
        {
            text: 'Add',
            striked: false,
        },
        {
            text: 'Things',
            striked: false,
        },
        {
            text: 'haha',
            striked: false,
        },
        {
            text: 'youhere',
            striked: false,
        }

    ],

    removeLIST: function (index) {
        this.lists.splice(index, 1)
    },

    addLIST: function () {
        if (this.addlist.length === 0) {
            return
        } else {
            this.lists.push({
                text: this.addlist,
                striked: false,
            });
            this.addlist = ''   /* let the block become empty again */
        }
    },

    // toggleStrike: function (index) {
    //     this.lists[index].striked = !this.lists[index].striked;

    //     let lastOne = ''
    //     if (this.lists[index].striked === true) {
    //         lastOne = this.lists.splice(index, 1)
    //         this.lists.push(lastOne[0])
    //     } else {
    //         lastOne = this.lists.splice(index, 1)
    //         this.lists.unshift(lastOne[0])
    //     }
    // },

    toggleStrike: function (index) {
        this.lists[index].striked = !this.lists[index].striked;

        let lastOne = ''
        if (this.lists[index].striked === true) {
            lastOne = this.lists.splice(index, 1)
            this.lists.push(lastOne[0])
        } else {
            lastOne = this.lists.splice(index, 1)
            this.lists.unshift(lastOne[0])
        }
    },
    // hideLIST: function () {
    //     let hideList = []

    // },

})
</script>


<template>
    <div class="mainBody">
        <div class="listForm">
            <h1>{{ todoList.title }} To Do List</h1>
            <!-- <h4><input v-model="todoList.title" placeholder="This is for?"></h4> -->
            <div><input v-model="todoList.addlist" placeholder="add todo..."></input>
                <button class="addBN" @click="todoList.addLIST"> + </button>
            </div>

            <div v-for="(list, index) in todoList.lists" :key="index"
                :style="{ textDecoration: list.striked ? 'line-through' : 'none' }">
                {{ list.text }}
                <button class="doneBN" @click="todoList.toggleStrike(index)">Done</button>
                <button class="deleteBN" @click="todoList.removeLIST(index)">Delete</button>

                <!-- {{ hideList.text }}
                    <button @click="todoList.toggleStrike(index)">Done</button>
                    <button @click="todoList.removeLIST(index)">Delete</button> -->
            </div>
        </div>
        <!-- <div class=" test">
                <h4>test</h4>
                <ul>
                    <li>{{ todoList.lists }}</li>
                </ul>
            </div> -->


    </div>


</template>



<style scoped>
.mainBody {
    float: none;
    margin-left: 277px;
    height: 100%;
}

.listForm {
    border: 10px;
    width: 60%;
    padding: 30px 30px 80px 30px;
    margin: 50px auto 0px auto;
    /* background-color: #9162A6; */
    color: #333333;
    border-radius: 10px;
    border-style: solid;
    border-color: #9162A6;
}

h1 {
    background-color: #F3AE3F;
    width: 100%;
    margin: 10px auto 30px auto;
    padding: 10px 10px 10px 10px;
    text-align: center;

}

.addBN {
    background-color: #9162A6;
    border: 0;
    width: 60px;
    height: 30px;
    border-radius: 50%;
}

.doneBN {
    background-color: #F3AE3F;
    border: 0;
    width: 60px;
    height: 30px;
    border-radius: 50%;
}

.deleteBN {
    background-color: #699B9F;
    border: 0;
    width: 60px;
    height: 30px;
    border-radius: 50%;
}

@media screen and (max-width: 700px) {
    .mainBody {
        margin-left: 0;
        float: none;
        height: 100%;
        padding: 30px;
    }

}

@media screen and (max-width: 500px) {
    input {
        width: 80%;
    }
}


#listForm {
    border-style: dotted;
    width: 50%;
}

.test {
    border-style: dotted;
    width: 50%;
    margin-top: 100px;
}

ul {
    list-style: none;
    border-bottom-style: dotted;
}
</style>