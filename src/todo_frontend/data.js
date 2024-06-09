const apiUrl = 'http://localhost:8000'

export async function fetchData() {
    const response = await fetch(`${apiUrl}/todolist`, {
        method: 'GET',  //implicitly recognise, don't need to write GET
        headers: { 'Content-Type': 'application/json' }
    });
    console.log('It is from GET data.js')
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json()  //connect to `api.py` GET
    // console.log(data)  //output `api.py` GET
    return data;
}

export async function postData(data) {
    const response = await fetch(`${apiUrl}/todolist`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const responseData = await response.json()
    console.log('Fetched todos:', data); //don't know why should use DATA except 'response.data'
    return responseData;
}

export async function updateData(id, data) {
    const response = await fetch(`${apiUrl}/todolist/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const responseData = await response.json()
    console.log(responseData)
    return responseData;
}


export async function deleteData(id) {
    const response = await fetch(`${apiUrl}/todolist/${id}`, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' }
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    console.log('Item deleted');
    return;
}
