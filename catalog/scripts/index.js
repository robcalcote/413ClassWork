$((function(context) {
    return function() {

        var containers = $('.product-container');
        console.log(111, containers);

        containers.each(function(i, container) {
            var pid = $(container).attr('data-product-id');
            $.ajax({
                url: "/catalog/product.tile/" + pid,
            });
            console.log(containers);
        });
    }
})(DMP_CONTEXT.get()));
