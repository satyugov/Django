window.onload = function () {
    $('.basket_list').on(types: 'click', selector: 'input[type="number"]', data: fuction() {
        var t_href = event.target;

        $.ajax(url: {
            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",

            success: fuction(data) {
                $('.basket_list').html(data.result);
            },
        });
        event.preventDefault();
    });
}