var date_range = null;
var date_now = new moment().format('YYYY-MM-DD');

function generate_report() {
    var parameters = {
        'action': 'search_report',
        'dia': $('#dia').val(),
        'mes': $('#mes').val(),
        'anio': $('#anio').val()
    };

    $.ajax({
        url: '/ventas_por_dia/',
        type: 'GET',
        data: parameters,
        success: function(data) {
            $('#data').DataTable({
                destroy: true,
                data: data,
                columns: [
                    { data: 'dia' },
                    { data: 'zapato' },
                    { data: 'total_pares_vendidos' }
                ]
            });
        },
        error: function(xhr, status, error) {
            console.error(xhr.responseText);
        }
    });
}

$(function () {
    $('#buscar').click(function() {
        generate_report();
    });

    generate_report();
});