onload = () => {
    let app = new Vue({
        el: "#app",
        data: {
            events: props.upcomming_events
        }
    });
};

Vue.filter('formatDate', function (value) {
    if (value) {
        return moment(String(value)).tz("Europe/Berlin").format('DD-MM YYYY HH:mm')
    }
})
