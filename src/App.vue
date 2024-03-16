<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>


<template>

    <body>
        <nav class="logo">
            <RouterLink to="/gate"><img src="./assets/空屋 logo-2.png" alt="雲端空屋RENT"></RouterLink>
        </nav>
        <ul>
            <li>
                <RouterLink style="text-decoration: none; color: inherit;" to="/gate">gate | 大門</RouterLink>
            </li>
            <li>
                <RouterLink style="text-decoration: none; color: inherit;" to="/livingroom">livingroom | 客廳
                </RouterLink>
            </li>
            <li>
                <RouterLink style="text-decoration: none; color: inherit;" to="/kitchen">Kitchen | 廚房</RouterLink>
            </li>
        </ul>
    </body>

    <RouterView />

    <footer>Hey It's our lovely rent house for something fun here.</footer>
</template>

<style scoped>
nav {
    display: ruby-text;
    background-color: #699B9F;
}

img {
    height: 60px;
    margin: 20px auto 15px auto;
}

ul {
    margin: 0;
    list-style: none;
    padding: 30px 20px 100% 25px;
    float: left;
    display: flow-root;
    background-color: #F3AE3F;
    font-family: monospace;
}

li {
    margin: 10px
}

footer {
    display: grid;
    background-color: #333333;
    width: 100%;
    padding: 10px;
    text-align: center;
    color: aliceblue;
    font-family: monospace;
    font-size: medium;
}

@media screen and (max-width: 700px) {
    ul {
        float: none;
        display: flex;
        width: 100%;
        padding: 15px 0 15px 25px;
    }

    li {
        display: flex;
        margin: auto 5px;
        border-right: dotted;
    }
}
</style>
