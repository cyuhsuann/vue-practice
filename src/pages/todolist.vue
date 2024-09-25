<script setup lang="ts">
import { ref, onMounted } from 'vue';

// // present to browser
import { fetchData, postData, deleteData, updateData } from '../todo_frontend/data';

// // define the TodoItem type
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

const sortTodos = () => {
    todos.value.sort((a, b) => {
        return a.id - b.id
    });

    doneTodos.value.sort((a, b) => {
        return b.id - a.id
    });
};

const fetchTodos = async () => {
    const data = await fetchData();
    if (Array.isArray(data)) {
        const sortTodos = TrueOrFalse(data)
        todos.value = sortTodos.notDoneItem as TodoItem[];
        doneTodos.value = sortTodos.doneItem as TodoItem[];
        // console.log('FROM VUE GET', todos.value, doneTodos.value)
        console.log('Fetched todos:', data);  // chack the data that we have gotten
    } else {
        console.error('Failed to fetch todos:', error);
    }
    sortTodos();
};

const addTodo = async () => {
    try {
        const newItem: TodoItem = {
            //only can accept one object
            item: newTodo.value,
            price: newPrice.value,
            isdone: false
        }
        const newTodoItem = await postData(newItem);
        todos.value.push(newItem)
        console.log('*******', newTodoItem)
        // // this one goes to api list and with id
        // EX: {id: 10, is_done: false, item: 'zzz', price: 2222}
        
        sortTodos();
        await fetchTodos()
        console.log('Added new todo:', newItem)
        // // this one goes to js list
        // EX: {item: 'zzz', price: '2222', isdone: false}
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
        console.log('Deleted todo:', id)
    } catch (error) {
        console.error('Failed to delete item:', error)
    }
}

const updateTodo = async (
    id: number, updatedItem: string, updatedPrice: number, isDone: boolean
): Promise<void> => {

    const item = { id, item: updatedItem, price: updatedPrice, isdone: isDone }
    console.log('Fetch the update item:', item)

    try {
        const updatedTodo = await updateData(id, item)
        const index = todos.value.findIndex((todo) => todo.id === id);
        if (index !== -1) {
            // todos.value[index] = updatedTodo;
            todos.value.splice(index, 1); // Remove from Not Done
            doneTodos.value.unshift(updatedTodo); // Add to Done at the beginning
        }

        editingTodo.value = null;  // Reset editing state
        // await fetchTodos()
        console.log('Updated todo:', updatedTodo, todos.value);

    } catch (error) {
        console.error('Failed to update new todo:', error)
    }
    sortTodos();
};

const editTodo = (todo: TodoItem) => {
    editingTodo.value = { ...todo };
    // Create a copy of the todo item to edit
    // spread syntax !
};

const cancelEdit = () => {
    editingTodo.value = null; // Reset editing state
};

const isDoneItem = async (todo: TodoItem) => {
    try {
        // // switch/ toggle the isdone status
        const updatedItem = { ...todo, isdone: !todo.isdone };
        const updatedTodo = await updateData(todo.id, updatedItem);
        const index = todos.value.findIndex((tdex) => tdex.id === todo.id);
        if (index !== -1) {
            // todos.value[index] = updatedTodo;
            todos.value.splice(index, 1); // Remove from Not Done
            doneTodos.value.unshift(updatedTodo); // Add to Done at the beginning
        }
        await fetchTodos()
        console.log('Marked as done:', updatedItem);
    } catch (error) {
        console.error('Failed to mark item as done:', error);
    }
}

const TrueOrFalse = (todos: TodoItem[]) => {
    const doneItem = todos.filter((todo) => todo.isdone === true)
    const notDoneItem = todos.filter((todo) => todo.isdone === false)
    return { notDoneItem, doneItem }
}


onMounted(fetchTodos);  //= onMounted(() => { fetchTodos() });


</script>

<template>
    <div class="mainBody">
        <div class="listForm">
            <h1>To Do List</h1>
            <div class="input">
                <input v-model="newTodo" type="text" placeholder="Enter a new todo" />
                <input v-model="newPrice" type="int" placeholder="Enter a new price" />
                <button @click="addTodo">ADD</button>
            </div>
            <div v-if="editingTodo">Edit Todo
                <input v-model="editingTodo.item" type="text" />
                <input v-model="editingTodo.price" type="number" />
                <button @click="updateTodo(editingTodo.id, editingTodo.item,
                    editingTodo.price, editingTodo.isdone)">Update</button>
                <button @click="cancelEdit">Cancel</button>
            </div>

            <ul>
                <!-- strike through the item if it's done -->
                <li class="todoitems" v-for="todo in todos" :key="todo.id">
                    <span class="todolist">。 {{ todo.item }} - ${{ todo.price }}</span>
                    <span class="buttons">
                        <button class="updateBN" @click="editTodo(todo)">Edit</button>
                        <button class="isdoneBN" @click="isDoneItem(todo)">Done</button>
                        <button class="deleteBN" @click="deleteTodo(todo.id)">Del</button>
                    </span>
                </li>
                <li class="todoitems" v-for="todo in doneTodos" :key="todo.id"
                    :style="{ textDecoration: todo.isdone ? 'line-through' : 'none' }">
                    <span class="todolist">。 {{ todo.item }} - ${{ todo.price }}</span>
                    <span class="buttons">
                        <button class="updateBN" @click="editTodo(todo)">Edit</button>
                        <button class="isdoneBN" @click="isDoneItem(todo)">Done</button>
                        <button class="deleteBN" @click="deleteTodo(todo.id)">Del</button>
                    </span>
                </li>
            </ul>




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
    border: 0;
    width: 60px;
    height: 30px;
    border-radius: 50%;
    height: 30px;
    margin-left: 10px;
    /* border-bottom-style: dashed; */
    background-color: #9162A6;
}

.deleteBN {
    background-color: #699B9F;
}

.isdoneBN {
    background-color: #69900F;
}

.updateBN {
    background-color: #F3AE3F;
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

.input {
    text-align: center;

}

ul {
    list-style: none;
}

.todoitems {
    margin: 20px;
}

.todolist {
    /* border-bottom-style: dotted; */
    /* display: inline-block; */
    margin-left: 15%;
}

.buttons {
    /* border-style: dotted; */
    float: right;
    margin-right: 15%;
}
</style>