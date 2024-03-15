<script setup>
import { ref, reactive } from 'vue'
import Image01 from '../assets/IMG_01.jpg'
import Image03 from '../assets/IMG_03.jpg'
import Image04 from '../assets/IMG_04.jpg'
import Image06 from '../assets/IMG_06.jpg'
import Image07 from '../assets/IMG_07.jpg'
import Image08 from '../assets/IMG_08.jpg'
import Image09 from '../assets/IMG_09.jpg'
import Image010 from '../assets/IMG_010.jpg'
import Image011 from '../assets/IMG_011.jpg'

const gallerys = reactive({
    lists: [
        { name: "清晨繁星", img: Image01, price: 2500 },
        { name: "澡澤", img: Image03, price: 3500 },
        { name: "清晨繁星", img: Image04, price: 2500 },
        { name: "澡澤", img: Image06, price: 3500 },
        { name: "清晨繁星", img: Image07, price: 2500 },
        { name: "澡澤", img: Image08, price: 3500 },
        { name: "清晨繁星", img: Image09, price: 2500 },
        { name: "澡澤", img: Image010, price: 3500 },
        { name: "清晨繁星", img: Image011, price: 2500 },
        { name: "清晨繁星", img: Image01, price: 2500 },
        { name: "澡澤", img: Image03, price: 3500 },
        { name: "清晨繁星", img: Image04, price: 2500 },
        { name: "澡澤", img: Image06, price: 3500 },
        { name: "清晨繁星", img: Image07, price: 2500 },
        { name: "澡澤", img: Image08, price: 3500 },
        { name: "清晨繁星", img: Image09, price: 2500 },
        { name: "澡澤", img: Image010, price: 3500 },
        { name: "清晨繁星", img: Image011, price: 2500 },
        { name: "清晨繁星", img: Image01, price: 2500 },
        { name: "澡澤", img: Image03, price: 3500 },
        { name: "清晨繁星", img: Image04, price: 2500 },
        { name: "澡澤", img: Image06, price: 3500 },
        { name: "清晨繁星", img: Image07, price: 2500 },
        { name: "澡澤", img: Image08, price: 3500 },
        { name: "清晨繁星", img: Image09, price: 2500 },
        { name: "澡澤", img: Image010, price: 3500 },
        { name: "清晨繁星", img: Image011, price: 2500 },
    ],
    template: '<p></p>'
})
</script>


<template>
    <div class="mainBody">
        <div class="row row-cols-3 galleryITEMS">
            <div class="galleryITEM" v-for="list in gallerys.lists">
                <img class="galleryIMG" :src="list.img" :alt="list.name" style="width:100%;">
                <p>{{ list.name }}</p>
            </div>
        </div>
    </div>
</template>



<style scoped>
.mainBody {
    border-style: dotted;
    float: none;
    margin-left: 277px;
    height: 100%;
}

.galleryITEMS {
    margin: 30px;
}

/* .galleryIMG {
    border-style: groove;
    border-color: #ffffff;
    border-width: 3px;
} */

@media screen and (max-width: 700px) {
    .mainBody {
        margin-left: 0;
        float: none;
        height: 100%;
        padding: 30px;
    }
}
</style>