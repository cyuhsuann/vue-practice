<script setup>
import { reactive } from 'vue'

import Nav from './Nav.vue';


const posts = reactive({
    POSTS: [
        { id: 1, Title: 'My journey with Vue' },
        { id: 2, Title: 'Blogging with Vue' },
        { id: 3, Title: 'Why Vue is so fun' }
    ]
})


</script>


<template>
    <div class="mainBody">
        <h1>To Do List</h1>
        <Nav v-for="post in posts.POSTS" :id="post.id" v-bind:Title="post.Title"></Nav>
    </div>
</template>



<style scoped>
.mainBody {
    border-style: dotted;
    float: none;
    margin-left: 277px;
    height: 100%;
}
</style>