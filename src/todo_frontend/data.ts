type TodoItem = {
    id?: number;
    item: string;
    price: number;
    isdone: boolean;
}

//to make sure it would send a list, not an object
type ApiResponse<T> = {
    message: T
}

// this is call: in middleware wraps `api calls`(CRUD) with DTOs
// to check the backend `api.py` variable and use a function to make them equal 
type ApiTodoItem = {
    id?: number
    item: string
    price: number
    is_done: boolean
}

function fromTodoApi(data: ApiTodoItem): TodoItem {
    return {
        id: data.id,
        item: data.item,
        price: data.price,
        isdone: data.is_done
    }
}

function toTodoApi(data: TodoItem): ApiTodoItem{
    return {
        id: data.id,
        item: data.item,
        price: data.price,
        is_done: data.isdone
    }
}


const apiUrl = 'http://localhost:8000'

const logRequest = (verb: string) => { console.log(`${verb} Request Received`) }


export async function fetchData(): Promise<TodoItem[]> {
    logRequest('GET')
    
    // // The response object, returned by the await fetch(), is a generic 
    // // placeholder for multiple data formats.
    const response = await fetch(`${apiUrl}/todolist`, {
        headers: { 'Content-Type': 'application/json' }
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }

    // // connect to `api.py` GET
    // // response.json() returns a promise resolved to a JSON object
    const data: ApiResponse<ApiTodoItem[]> = await response.json()
    console.log('Fetched Items:', data)
    // // from [a ApiTodoItem list of obect] to {an TodoItem Object}
    return data.message.map((item) => fromTodoApi(item));
}

export async function postData(data: TodoItem): Promise<TodoItem> {
    logRequest('POST')
    const response = await fetch(`${apiUrl}/todolist`, {
        headers: { 'Content-Type': 'application/json' },
        method: 'POST',
        body: JSON.stringify(toTodoApi(data))

    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const responseData: ApiResponse<TodoItem> = await response.json()
    console.log('Posted Item:', responseData);
    return responseData.message;
}

export async function deleteData(id: number): Promise<void> {
    logRequest('DELETE')
    const response = await fetch(`${apiUrl}/todolist/${id}`, {
        headers: { 'Content-Type': 'application/json' },
        method: 'DELETE',
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const responseData: ApiResponse<ApiTodoItem> = await response.json()
    console.log('Deleted Item:', responseData);
    return;
}

export async function updateData(id: number, data: TodoItem): Promise<TodoItem> {
    logRequest('PUT')
    const response = await fetch(`${apiUrl}/todolist/${id}`, {
        headers: { 'Content-Type': 'application/json' },
        method: 'PUT',
        body: JSON.stringify(toTodoApi(data))
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    // // improtant lesson: check the `api.py` and here
    const responseData: ApiResponse<ApiTodoItem> = await response.json()
    console.log('Updated item:', responseData)
    return fromTodoApi(responseData.message);
}

