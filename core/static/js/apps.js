
$(document).ready(function() {


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


    /* data table */
//   var table = $('#license_table').DataTable({
//
//        "order": [[ 0, "desc" ]],
//        "pageLength": 5,
//        "lengthMenu": [3, 5, 10, 25, 50, 75, 100 ],
//        "language": {
//            "lengthMenu": " _MENU_ registros por pagina",
//            "zeroRecords": "Nenhum registro encontrado, desculpe",
//            "info": "_PAGE_ de _PAGES_",
//            "infoEmpty": "sem registros ",
//            "infoFiltered": "(filtro de  _MAX_ total )"
//        },
//           "language": {
//             "Search": "Pesquisar ",
//             "lengthMenu": "Mostrar _MENU_ registro por paginas",
//             "zeroRecords": "não há registros",
//             "info": "Mosnrando registro _PAGE_ de _PAGES_",
//             "infoEmpty": "Nenhum resuldado foi encontrado",
//             "infoFiltered": "(filtradno de _MAX_ total de registros)",
//
//             "paginate": {
//                "next": "Próxima",
//                "previous": "Anterior"
//                 }
//            }
//    });



    $('.paginator').click(function(){
        var page = $(this);
        $.ajax({
            url:    '/' + page.attr('href'),
            type:  'GET',
            success: function(data){

                alert('');

            },
        });
    });



    var loadFormLicense =  function (){
        var btn = $(this)
        $.ajax({
            url:    btn.attr('data-url'),
            type:  'GET',
            beforeSend: function(){
               $('#modal-license').modal('show');
            },
            success: function(data){
                $('#modal-license .modal-content').html(data.form_html);

                 $('.calender').datepicker({
                    format: 'dd/mm/yyyy',
                    todayHighlight: true,
                    autoclose: true,
                    orientation: "bottom auto",
                    language: 'pt-BR',
                });

                $('.autocomplete').autocomplete( {
                    appendTo: 'modal-license',
                    minLength: 3,
                    source: '/licenses/autocomplete/'
                });



            },
        });
    };


    var saveFormLicense = function(){
        var form = $(this);

        $.ajax({
            url:    form.attr('action'),
            type:   form.attr('method'),
            data:   form.serialize(),
            dataType: 'json',

            success: function(data){
                if(data.is_form_valid){

                    $('#license_table tbody').html(data.table_license);
                    $('#modal-license').modal('hide')

                    table.columns.adjust().draw();

                    $('#js-message').text(data.js_title_message)
                    $('#js-serial').text(data.js_serial)
                    $('#js-cliente').text(data.js_cliente)
                    $('#modal-message').modal('show');

                }else{
                    $('#modal-license .modal-content').html(data.form_html);
                }
            }
    });
        // return false because this method is trigger on submit.
        return false;
    };


    // Create license

    $('.js-modal-form').click(loadFormLicense);
    $('#modal-license').on('submit', '.js-form-license-save', saveFormLicense);

    // Update License
    $('#license_table').on('click' , '.js-license-update' , loadFormLicense);
    $('#modal-license').on('submit', '.js-form-license-update', saveFormLicense);

    // Delete License
    $('#license_table').on('click' , '.js-license-delete' , loadFormLicense);
    $('#modal-license').on('submit', '.js-form-license-delete', saveFormLicense);


});
