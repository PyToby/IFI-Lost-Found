function callFlaskFunction(functionName) {
    fetch('/' + functionName)
    //.then(response => response.json())
    //.then(result => {
    //})
    .then(response=> response.text())
    .then(message=>{
        alert(message)
    })
    .catch(error => console.error('Error:', error))
}