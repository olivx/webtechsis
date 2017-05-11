
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

// pagina perennity licence

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


    // parar de mandar avisos
   $('#modal-license').on('click', '.js-send-warning', function (){

        var form = $('.js-form-license-update');

        $.ajax({
            url:  '/licenses/stop_send_warning/',
            type: 'post',
            data: form.serialize(),
            dataType: 'json',

            success: function(data){
                $('#modal-license').modal('hide');

                 $('#js-message').text(data.js_title_message)
                 $('#js-serial').text(data.js_serial)
                 $('#js-cliente').text(data.js_cliente)

                 $('#modal-message').modal('show');
            },
             error: function (request, status, error) {
                alert(error);
            }
        });

        return false;

    });




    // Create license
    $('.js-modal-form').click(loadFormLicense);
    $('#modal-license').on('submit', '.js-form-license-save', saveFormLicense);

    // Update License
    $('#license_table').on('click' , '.js-license-update' , loadFormLicense);
    $('#modal-license').on('submit', '.js-form-license-update', saveFormLicense);

    // Delete License
    $('#license_table').on('click' , '.js-license-delete' , loadFormLicense);
    $('#modal-license').on('submit', '.js-form-license-delete', saveFormLicense);



// page boletos
    //remendo os disabled dos campos para o subimit
    $('.js-form-update-boleto').submit(function(){
        $(".js-form-update-boleto :disabled").removeAttr('disabled');
    });

    // submiting
    $('input[name=radio-empresa]').change(function(){
        $('form').submit();
    });

    // formatando campo com calendario
    $('.calender').datepicker({
        format: 'dd/mm/yyyy',
        todayHighlight: true,
        autoclose: true,
        orientation: "bottom auto",
        language: 'pt-BR',
     });




});
