onload = () => {
    let app = new Vue({
        el: "#app",
        data: {
            events: props.upcomming_events
        }
    });
};
moment.locale('da');

Vue.filter('formatDate', function (value) {
    if (value) {
        return moment(String(value)).format('dddd [d.] D MMMM')
    }
});

Vue.filter('formatPrice', function (value) {
    if (value) {
        return value + ".-"
    }
});
