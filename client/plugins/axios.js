export default function ({ $axios, store }) {
    $axios.onRequest(config => {
        const token = localStorage.getItem('userToken');
        return config;
    });

    $axios.onResponse(response => {
        return response;
    });

    $axios.onError(error => {
        return Promise.reject(error);
    });

}


