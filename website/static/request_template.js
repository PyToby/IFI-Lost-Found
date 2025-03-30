function callFlaskFunction(functionName) {
    fetch('/' + functionName)
    .then(response=>{
        if (!response.ok){
            alert("Error:",response.status)
        }
        else{
        }
    })
    .catch(error => console.error('Error:', error))
}