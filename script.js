url = 'http://127.0.0.1:5000/'

// alert top end sweetalert2
function topEndSuscess(){
    Swal.fire({
        toast: true,
        position: 'top-end',
        icon: 'success',
        title: 'Success',
        showConfirmButton: false,
        timer: 1500
    })
}

function topEndError(){
    Swal.fire({
        toast: true,
        position: 'top-end',
        icon: 'error',
        title: 'Error',
        showConfirmButton: false,
        timer: 1500
    })
}


async function getTable(){
    clearTalbe()
    const response = await fetch(url + 'getAll',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            abi_address: document.getElementById('abiInput').value
        })
    }).catch((error) => {
        console.log(error)
    });
    const data = await response.json();
    console.log(data)
    var count=0
    // const account = data.account;
    let table = document.getElementById('tableBody')
    data.forEach((element, index) => {
        if(element[4]){
            console.log(element, index)
            let row = table.insertRow(count)
            let cell0 = row.insertCell(0)
            let cell1 = row.insertCell(1)
            let cell2 = row.insertCell(2)
            let cell3 = row.insertCell(3)
            let cell4 = row.insertCell(4)
            cell0.innerHTML = element[0]
            cell1.innerHTML = element[1]
            cell2.innerHTML = element[2]
            cell3.innerHTML = element[3]
            cell4.innerHTML = "<div class='d-flex text-center>"
            cell4.innerHTML += `<button type="button" class="btn btn-info" onclick="popupedit('${(element[0])}')">Edit</button>`
            cell4.innerHTML += `<button type="button" class="btn btn-danger" onclick="del('${(element[0])}')">Delete</button>`
            cell4.innerHTML += '</div>'
            count+=1
        }
    });
}

async function post(){
    let abi = document.getElementById('abiInput').value;
    let id = document.getElementById('idInput').value;
    let fName = document.getElementById('fNameInput').value;
    let lName = document.getElementById('lNameInput').value;
    let gpax = document.getElementById('gpaxInput').value;

    const response = await fetch(url + 'post', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            abi_address: abi,
            id: parseInt(id),
            fname: fName,
            lname: lName,
            gpax: gpax
        })
    }).catch((error) => {
        topEndError()
    });
    topEndSuscess()
    getTable()
}

async function getByID(id){
    const response = await fetch(url + 'getByID', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            abi_address: document.getElementById('abiInput').value,
            id: parseInt(id)
        })
    }).catch((error) => {
        console.log(error)
    });
    const data = await response.json();
    return data
    }

// pop up edit with sweetalert2
async function popupedit(id){
    const data = await getByID(id)
    console.log(data)
    Swal.fire({
        title: 'Edit',
        html:
        '<div class="form-group">' +
        '<label for="editidInput">ID</label>' +
        '<input type="text" class="form-control" id="editidInput" value="'+data[0]+'" disabled>' +
        '</div>' +
        '<div class="form-group">' +
        '<label for="editfNameInput">First Name</label>' +
        '<input type="text" class="form-control" id="editfNameInput" value="'+data[1]+'">' +
        '</div>' +
        '<div class="form-group">' +
        '<label for="editlNameInput">Last Name</label>' +
        '<input type="text" class="form-control" id="editlNameInput" value="'+data[2]+'">' +
        '</div>' +
        '<div class="form-group">' +
        '<label for="editgpaxInput">GPAX</label>' +
        '<input type="text" class="form-control" id="editgpaxInput" value="'+data[3]+'">' +
        '</div>',
        showCancelButton: true,
        confirmButtonText: 'Confirm',
        cancelButtonText: 'Cancel',
        preConfirm: () => {
            confirmEdit(id)
        }
    })
}

async function confirmEdit(id){
    const response = await fetch(url + 'edit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            abi_address: document.getElementById('abiInput').value,
            id: parseInt(id),
            fname: document.getElementById('editfNameInput').value,
            lname: document.getElementById('editlNameInput').value,
            gpax: document.getElementById('editgpaxInput').value
        })
    }).catch((error) => {
        console.log(error)
        topEndError()
    });
    topEndSuscess()
    const data = await response.json();
    console.log(data)
    getTable()
}

function clearTalbe() {
    var table = document.getElementById("tableBody");
    while(table.hasChildNodes())
    {
       table.removeChild(table.firstChild);
    }
}

async function del(id){
    const response = await fetch(url + 'setFlag', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            abi_address: document.getElementById('abiInput').value,
            id: parseInt(id),
            flag: false
        })
    }).catch((error) => {
        console.log(error)
        topEndError()
    });
    topEndSuscess()
    const data = await response.json();
    console.log(data)
    getTable()
}