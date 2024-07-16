var tblProducts;
                                              
var vents = {
    
    items: {
        cliente: '',
        fecha_venta: '',
        subtotal: 0.00,
        bs : 0.00,
        total: 0.00,
        Item: []
    },
    
    calculate_invoice: function() {
        var subtotal = 0.00;
        var valor_dolar_bs = parseFloat($('#valor_dolar_bs').val());
        $.each(this.items.Item, function (pos, dict) {
            dict.subtotal = dict.cantidad * parseFloat(dict.precio_venta);
            subtotal += dict.subtotal;
        });
        this.subtotal = subtotal;
        this.total = this.subtotal * valor_dolar_bs;
        $('input[name="subtotal"]').val(this.subtotal.toFixed(2)); // Redondea a 2 decimales
        $('input[name="valor_dolar_bs"]').val(this.items.bs.toFixed(2));
        $('input[name="total"]').val(this.total.toFixed(2)); // Redondea a 2 decimales
    },
        
    add: function(item) {
        this.items.Item.push(item);
        this.list();
    },
    list: function () {
        this.calculate_invoice();
        tblProducts = $('#tblProducts').DataTable({
            responsive: true,
            autoWidth: false,
            destroy: true,
            data: this.items.Item,
            columns: [
                {"data": "id_item"},
                {"data": "marca"},
                {"data": "descripcion"},
                {"data": "id_categoria.descripcion"},
                {"data": "precio_venta"},
                {"data": "cantidad"},
                {"data": "subtotal"},
            ],
            columnDefs: [
                {
                    targets: [0],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<a rel="remove" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    }
                },
                {
                    targets: [-3],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
                {
                    targets: [-2],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '<input type="text" name="cantidad" class="form-control form-control-sm" autocomplete="off" value="'+row.cantidad+'">';
                    }
                },
                {
                    targets: [-1],
                    class: 'text-center',
                    orderable: false,
                    render: function (data, type, row) {
                        return '$' + parseFloat(data).toFixed(2);
                    }
                },
            ],

            initComplete: function (settings, json) {

            }
        });
    },

};

$(function () {
   
    // search products
    $('input[name="search"]').autocomplete({
        source: function (request, response) {
            $.ajax({
                url: window.location.pathname,
                type: 'POST',
                data: {
                    'action': 'search_products',
                    'term': request.term
                },
                dataType: 'json',
            }).done(function (data) {
                response(data);
            }).fail(function (jqXHR, textStatus, errorThrown) {
                //alert(textStatus + ': ' + errorThrown);
            }).always(function (data) {

            });
        },
        delay: 500,
        minLength: 1,
        select: function (event, ui) {
            event.preventDefault();
            console.clear();
            ui.item.cantidad = 1;
            ui.item.subtotal = 0.00;
            console.log(vents.items);
            vents.add(ui.item);
            $(this).val('');
        }
    });

    $('.btnRemoveAll').on('click', function () {
      
        vents.items.Item = [];
        vents.list();

    });


    $('#tblProducts tbody')
        .on ('click', 'a[rel = "remove"]', function () {
        var tr = tblProducts.cell($(this).closest('td, li')).index();
        vents.items.Item.splice(tr.row, 1);
        vents.list();

        })
        .on ('change keyup', 'input[name = "cantidad"]', function () {
        console.clear();
        var cantidad = parseInt($(this).val());
        var tr = tblProducts.cell($(this).closest('td, li')).index();
        console.log(tr);
        //var data = tblProducts.row(tr.row).data();
        vents.items.Item[tr.row].cantidad = cantidad;
        console.log(vents.items.Item);
        vents.calculate_invoice();
        $('td:eq(6)',tblProducts.row(tr.row).node()).html('$'+ vents.items.Item[tr.row].subtotal.toFixed(2));
             
    });

    // event submit
    $('form').on('submit', function (e) {
        e.preventDefault();

        if(vents.items.Item.length === 0){
            message_error('Debe al menos tener un item en su detalle de venta');
            return false;
        }

        vents.items.fecha_venta = $('input[name="fecha_venta"]').val();
        vents.items.cliente = $('select[name="cliente"]').val();
        vents.items.subtotal = $('input[name="subtotal"]').val();
        vents.items.total = $('input[name="total"]').val();
        

        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('vents', JSON.stringify(vents.items));
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function (response) {
            alert_action('Notificación', '¿Desea imprimir la factura?', function () {
                window.open('/factura/' + response.id, '_blank');
                location.href = '/menu_ventas';
            }, function () {
                location.href = '/menu_ventas';
            });
            
        });
    });  
   

    $('.select2').select2();

    vents.list();
});