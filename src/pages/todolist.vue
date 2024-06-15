<script setup lang="ts">
import { ref, onMounted } from 'vue';

//present to browser
import { fetchData, postData, deleteData, updateData } from '../todo_frontend/data';

// Define the TodoItem type
type TodoItem = {
    id: number;
    item: string;
    price: number;
    isdone: boolean;
}


const todos = ref<TodoItem[]>([]);
const newTodo = ref<string>('');
const newPrice = ref<string | number>('');
const editingTodo = ref<TodoItem | null>(null);
const doneTodos = ref<TodoItem[]>([]);

const fetchTodos = async () => {
    const data = await fetchData();
    if (Array.isArray(data)) {
        todos.value = data as TodoItem[];  // 確保這裡設置的是數組
        console.log('Fetched todos:', data);  // chack the data thast we have gotten
    } else {
        console.error('Failed to fetch todos:', error);
    }
};

const addTodo = async () => {
    try {
        newItem = {
            //only can accept one object
            item: newTodo.value, price: newPrice.value, isdone: false
        }
        const newTodoItem = await postData(newItem);
        // todos.value.push(newTodoItem);
        todos.value.push(newItem)
        console.log('New item added:', newTodoItem)
    } catch (error) {
        console.error('Failed to add new todo:', error)
    }
    newTodo.value = '';
    newPrice.value = '';
};

const deleteTodo = async (id: number) => {
    try {
        await deleteData(id);
        await fetchTodos();  // Refresh the list
    } catch (error) {
        console.error('Failed to delete item:', error)
    }
}

const updateTodo = async (
    id: number, updatedItem: string, updatedPrice: number, isdone: boolean
) => {
    const item = { id, item: updatedItem, price: updatedPrice, isdone }
    console.log(item)
    try {
        const updatedTodo = await updateData(
            id,
            item
        )
        const index = todos.value.findIndex((todo) => todo.id === id);
        if (index !== -1 && isdone === false) {
            todos.value[index] = updatedTodo;
        }
        console.log('Updated item:', updatedTodo);
        editingTodo.value = null;  // Reset editing state
        console.log("*******  ", todos.value)

    } catch (error) {
        console.error('Failed to update new todo:', error)
    }
};

const editTodo = (todo: TodoItem) => {
    console.log('*******', todo)
    editingTodo.value = { ...todo };
    // Create a copy of the todo item to edit
    // spread syntax !
};

const cancelEdit = () => {
    editingTodo.value = null; // Reset editing state
};

// const isDoneItem = async (todo: TodoItem) => {
//     try {
//         const updateTodo = await updateData(todo.id, { ...todo, isdone: !todo.isdone });
//         const index = todos.value.findIndex((tdex) => tdex.id === todo.id);
//         if (index !== -1) {
//             todos.value[index] = updatedTodo;
//         }
//         console.log('isDone item:', updatedTodo)
//     } catch (error) {
//         console.error('Failed to isDone item:', error)
//     }
// }

// const notDoneTodos = () => todos.value.filter(todo => !todo.isDone);
// DoneTodos = () => todos.value.filter(todo => todo.isDone);

onMounted(fetchTodos);  //= onMounted(() => { fetchTodos() });


</script>

<template>
    <div class="mainBody">
        <div class="listForm">
            <h1>To Do List</h1>
            <div class="output">
                <input v-model="newTodo" type="text" placeholder="Enter a new todo" />
                <input v-model="newPrice" type="int" placeholder="Enter a new price" />
                <button @click="addTodo">ADD</button>

                <ul>
                    <!-- strike through the item if it's done -->
                    <li v-for="todo in todos" :key="todo.id">
                        <!-- :style="{ textDecoration: list.isDone ? 'line-through' }" -->
                        。 {{ todo.item }} - ${{ todo.price }}
                        <button class="updateBN" @click="editTodo(todo)">Edit</button>
                        <button class="isdoneBN" @click="isDoneItem(todo)">Done</button>
                        <button class="deleteBN" @click="deleteTodo(todo.id)">Del</button>


                    </li>
                </ul>
                <div v-if="editingTodo">
                    <h3>Edit Todo</h3>
                    <input v-model="editingTodo.item" type="text" />
                    <input v-model="editingTodo.price" type="number" />
                    <button @click="updateTodo(editingTodo.id, editingTodo.item,
                    editingTodo.price, editingTodo.isdone)">Update</button>
                    <button @click="cancelEdit">Cancel</button>
                </div>

                <h3>Done</h3>
                <li v-for="todo in doneTodos" :key="todo.id">
                    。 {{ todo.item }} - ${{ todo.price }}
                    <button class="deleteBN" @click="deleteTodo(todo.id)">Del</button>
                    <!-- <button class="isdoneBN" @click="isDoneItem(todo)">Done</button> -->
                </li>
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

.listForm {
    border: 10px;
    width: 60%;
    padding: 30px 30px 80px 30px;
    margin: 50px auto 0px auto;
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

button {
    background-color: #9162A6;
    color: aliceblue;
    border: 0;
    width: 100px;
    height: 30px;
    border-radius: 50%;
}

.deleteBN {
    background-color: #699B9F;
    border: 0;
    width: 60px;
    height: 30px;
    margin-left: 10px;
    border-radius: 50%;
}

.updateBN {
    background-color: #F3AE3F;
    border: 0;
    width: 60px;
    height: 30px;
    margin-left: 10px;
    border-radius: 50%;
}

.isdoneBN {
    background-color: #69900F;
    border: 0;
    width: 60px;
    height: 30px;
    margin-left: 10px;
    border-radius: 50%;
}

/* .strikethrough {
    text-decoration: line-through;
} */

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


ul {
    list-style: none;
    /* border-bottom-style: dotted; */
}
</style>