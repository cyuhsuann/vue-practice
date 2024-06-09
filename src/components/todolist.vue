<script>
import { ref, onMounted } from 'vue';
import { fetchData, postData, updateData, deleteData } from '../todo_frontend/data';  //present to browser
// import axios from 'axios';

const apiUrl = 'http://localhost:8000';

export default {
    setup() {
        const todos = ref([]);
        const newTodo = ref('');
        const newPrice = ref('');
        const editingTodo = ref(null);

        const fetchTodos = async () => {
            const data = await fetchData();
            if (Array.isArray(data)) {
                todos.value = data; // 確保這裡設置的是數組
                console.log('Fetched todos:', data);  // chack the data thast we have gotten
            } else {
                console.error('Failed to fetch todos:', error);
            }
        };

        const addTodo = async () => {
            try {
                const newTodoItem = await postData({ item: newTodo.value, price: newPrice.value });  //only can accept one object
                todos.value.push({ item: newTodo.value, price: newPrice.value })  // todos.value.push(newTodoItem);
                console.log('New item added:', newTodoItem)
            } catch (error) {
                console.error('Failed to add new todo:', error)
            }
            newTodo.value = '';
            newPrice.value = '';
        };

        const updateTodo = async (id, updatedItem, updatedPrice) => {
            try {
                const updatedTodo = await updateData(id, { item: updatedItem, price: updatedPrice })
                const index = todos.value.findIndex(todo => todo.id === id);
                if (index !== -1) {
                    todos.value[index] = updatedTodo;
                }
                console.log('Updated item:', updatedTodo);
                editingTodo.value = null;  // Reset editing state

            } catch (error) {
                console.error('Failed to add new todo:', error)
            }
        };

        const editTodo = (todo) => {
            editingTodo.value = { ...todo };
            // Create a copy of the todo item to edit
            // spread syntax !
        };

        const cancelEdit = () => {
            editingTodo.value = null; // Reset editing state
        };


        const deleteTodo = async (id) => {
            try {
                await deleteData(id);
                await fetchTodos();  // Refresh the list
            } catch (error) {
                console.error('Failed to add new todo:', error)
            }
        }

        onMounted(fetchTodos);  //= onMounted(() => { fetchTodos() });

        return {
            todos,
            newTodo,
            newPrice,
            editingTodo,
            fetchTodos,
            addTodo,
            updateTodo,
            deleteTodo,
            editTodo,
            cancelEdit,
        }


    }
};
</script>

<template>
    <div class="mainBody">
        <div class="listForm">
            <h1>To Do List</h1>
            <div class="output">
                <!-- 文字輸入框 -->
                <input v-model="newTodo" type="text" placeholder="Enter a new todo" />
                <input v-model="newPrice" type="int" placeholder="Enter a new price" />
                <!-- 提交按鈕 -->
                <button @click="addTodo">+ U +</button>

                <!-- 顯示待辦事項列表 -->
                <ul>
                    <li v-for="todo in todos" :key="todo.id">
                        。 {{ todo.item }} - ${{ todo.price }}
                        <button class="updateBN" @click="editTodo(todo)">Edit</button>
                        <button class="deleteBN" @click="deleteTodo(todo.id)">Del</button>

                    </li>
                </ul>
                <div v-if="editingTodo">
                    <h3>Edit Todo</h3>
                    <input v-model="editingTodo.item" type="text" />
                    <input v-model="editingTodo.price" type="number" />
                    <button @click="updateTodo(editingTodo.id, editingTodo.item, editingTodo.price)">Update</button>
                    <button @click="cancelEdit">Cancel</button>
                </div>
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