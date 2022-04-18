document.addEventListener('DOMContentLoaded', function() {

    if (document.querySelector('#add_task_form')) {
        document.querySelector('#add_task_form').onsubmit = () => { addtask() };
    };
});

function addtask() {

    let description = document.querySelector('#description').value;

    fetch('/add_task', {
        method: 'POST',
        body: JSON.stringify({
            description: description
        }),
    })
    .then(response =>  response.text().then(data => ({status: response.status})))
    .then(result => {
        if (result.status == "200") {
            document.location.href="/";
        } else {
            alert('Error: ' + result.status);
        }
    });
}