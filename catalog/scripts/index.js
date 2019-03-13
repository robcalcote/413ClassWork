$((function(context) {
    
    return function() {

        var containers = $('.product-container');
        containers.each(function(i, container) {
            var pid = $(container).attr('data-product-id');
            console.log(1111111)
            $.ajax({
                url: "/catalog/product.tile/" + pid,
            }).done(function(data){
                $(container).html(data)
            });
            
        });
    }
})(DMP_CONTEXT.get()));
