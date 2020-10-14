const BASE_URL = 'http://localhost:8000';

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

async function makeRequest(url, method='GET', data=undefined) {
    let opts = {method, headers: {}};

    if (!csrfSafeMethod(method))
        opts.headers['X-CSRFToken'] = getCookie('csrftoken');

    if (data) {
        opts.headers['Content-Type'] = 'application/json';
        opts.body = JSON.stringify(data);
    }

    let response = await fetch(url, opts);

    if (response.ok) {
        return response;
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

async function calc() {
    async function onClick(event) {
        event.preventDefault()
        let url = event.target.href;
        let answer = await makeRequest(url, 'POST', {
            'A': document.getElementById('A').value,
            'B': document.getElementById('B').value
        }).then(response => response.json())

        let div = document.getElementsByClassName('result')[0];
        div.innerText = answer.result
    }

    let buttons = document.getElementsByClassName('btn');
    for(btn of buttons) {
        btn.addEventListener('click', onClick);
    }
}
calc();