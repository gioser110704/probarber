var tblProducts;
                                              
var comps = {
    
    items: {
        proveedor: '',
        fecha_compra: '',
        subtotal: 0.00,
        envio : 0.00,
        total: 0.00,
        Item: []
    },
    
    calculate_invoice: function() {
        var subtotal = 0.00;
        var envio = parseFloat($('#envio').val());
        $.each(this.items.Item, function (pos, dict) {
            dict.subtotal = dict.cantidad * parseFloat(dict.precio_compra);
            subtotal += dict.subtotal;
        });
        this.subtotal = subtotal;
        this.total = this.subtotal + envio;
        $('input[name="subtotal"]').val(this.subtotal.toFixed(2)); // Redondea a 2 decimales
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
                {"data": "precio_compra"},
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
            console.log(comps.items);
            comps.add(ui.item);
            $(this).val('');
        }
    });

    $('.btnRemoveAll').on('click', function () {
      
        comps.items.Item = [];
        comps.list();

    });


    $('#tblProducts tbody')
        .on ('click', 'a[rel = "remove"]', function () {
        var tr = tblProducts.cell($(this).closest('td, li')).index();
        comps.items.Item.splice(tr.row, 1);
        comps.list();

        })
        .on ('change keyup', 'input[name = "cantidad"]', function () {
        console.clear();
        var cantidad = parseInt($(this).val());
        var tr = tblProducts.cell($(this).closest('td, li')).index();
        console.log(tr);
        //var data = tblProducts.row(tr.row).data();
        comps.items.Item[tr.row].cantidad = cantidad;
        console.log(comps.items.Item);
        comps.calculate_invoice();
        $('td:eq(6)',tblProducts.row(tr.row).node()).html('$'+ comps.items.Item[tr.row].subtotal.toFixed(2));
             
    });

    // event submit
    $('form').on('submit', function (e) {
        e.preventDefault();

        if(comps.items.Item.length === 0){
            message_error('Debe al menos tener un item en su compra');
            return false;
        }

        comps.items.fecha_compra = $('input[name="fecha_compra"]').val();
        comps.items.proveedor = $('select[name="proveedor"]').val();
        comps.items.subtotal = $('input[name="subtotal"]').val();
        comps.items.envio = $('input[name="envio"]').val();
        comps.items.total = $('input[name="total"]').val();
        

        var parameters = new FormData();
        parameters.append('action', $('input[name="action"]').val());
        parameters.append('comps', JSON.stringify(comps.items));
        submit_with_ajax(window.location.pathname, 'Notificación', '¿Estas seguro de realizar la siguiente acción?', parameters, function (response) {
            alert_action('Notificación', '¿Desea imprimir la factura de compra?', function () {
                window.open('/recibo/' + response.id, '_blank');
                location.href = '/menu_compras';
            }, function () {
                location.href = '/menu_compras';
            });
            
        });
    });  
   

    $('.select2').select2();

    comps.list();
});