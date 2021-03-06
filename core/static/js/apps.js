
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

// product form

    var loadFormProduto =  function(){

        var btn = $(this)

        $.ajax({
            url: btn.attr('data-url'),
            type: 'GET',

            beforeSend: function(){
                $('#modal-produtos').modal('show');
            },
            success: function(data){
                $('#modal-produtos .modal-content').html(data.html_form)

                $('.autocomplete').autocomplete({
                    appendTo: 'modal-produtos',
                    minLength: 3,
                    source: '/core/produto/autocomplete/'
                });


            }
        });

    }

    var saveProdutoForm =  function(){
        var form = $(this);

        $.ajax({
            url:    form.attr('action'),
            type:   form.attr('method'),
            data:   form.serialize(),
            dataType: 'json',

            success: function(data){
                if( data.is_form_valid){
                    $('#produto-table tbody').html(data.html_table);
                    $('#modal-produtos').modal('hide');

                    alert(data.message)

                }else{
                    alert(data.message)
                    $('#modal-produtos .modal-content').html(data.html_form)

                }

            }

        });
        return false;
    };


//  Create produtos
    $('.js-modal-prodtudos').click(loadFormProduto);
    $('#modal-produtos').on('submit', '.js-form-produto-save', saveProdutoForm);

// Update produtos
    $('#produto-table').on('click', '.js-produto-update', loadFormProduto);
    $('#modal-produtos').on('submit', '.js-form-produto-update', saveProdutoForm);

// deactivate produto
    $('#produto-table').on('click', '.js-produto-deactivate', loadFormProduto);
    $('#modal-produtos').on('submit' , '.js-form-produto-deactivate', saveProdutoForm);


// License form
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
                    source: '/core/cliente/autocomplete/'
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



// suporte add

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



// faturamento app
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
