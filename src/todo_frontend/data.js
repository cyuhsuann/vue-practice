const apiUrl = 'http://localhost:8000'

// const express = require('express');
// const app = express();
// app.use(express.static('public'));

const logRequest = (verb) => { console.log(`${verb} Request Received`) }

// app.use((req, res, next) => { console.log(`${req.method} Request Received`); });

// app.get('/todolist/', (req, res, next) => {
//     const data = response.json()
//     res.send(data);
//     console.log('Response Sent');
// });



export async function fetchData() {
    logRequest('GET')
    const response = await fetch(`${apiUrl}/todolist`, {
        headers: { 'Content-Type': 'application/json' }
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    // // connect to `api.py` GET
    const data = await response.json()
    // console.log(data)  // // output `api.py` GET
    return data;
}

export async function postData(data) {
    logRequest('POST')
    const response = await fetch(`${apiUrl}/todolist`, {
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const responseData = await response.json()
    // TODO: don't know why should use DATA except 'response.data'
    console.log('Fetched todos:', data);
    return responseData;
}

export async function updateData(id, data) {
    logRequest('PUT')
    const response = await fetch(`${apiUrl}/todolist/${id}`, {
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
    logRequest('DELETE')
    const response = await fetch(`${apiUrl}/todolist/${id}`, {
        headers: { 'Content-Type': 'application/json' }
    });
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    console.log('Item deleted');
    return;
}

