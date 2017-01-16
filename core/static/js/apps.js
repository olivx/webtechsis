
$(document).ready(function() {

    /* data table */
    $('#lisence_table').DataTable({
        "pageLength": 5,
        "lengthMenu": [3, 5, 10, 25, 50, 75, 100 ],
        "language": {
            "search" : "Pesquisar ",
            "lengthMenu": " _MENU_ registros por pagina",
            "zeroRecords": "Nenhum registro encontrado, desculpe",
            "info": "_PAGE_ de _PAGES_",
            "infoEmpty": "sem registros ",
            "infoFiltered": "(filtro de  _MAX_ total )"
        },
        "paginate": {
        "first":      "Primeiro",
        "last":       "Ultimo",
        "next":       "Proximo",
        "previous":   "Voltar"
        }
    });


    /* fuction autocomplete */
    $(function() {
        $('#id_cliente').autocomplete( {
                appendTo: 'modal-add',
                minLength: 3,
                source: '/licenses/autocomplete/'
        });
    });


    /* reset the modal input text area and selects */
    $('.modal').on('hidden.bs.modal', function (e) {
         $(this).find("input,textarea,select").val('').end();
         $(this).find("span").text('').end();
    });


    //our date input has the name "date"
    var instaled_input=$('#id_installed');
    //var container_installed =$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
    instaled_input.datepicker({
        format: 'dd/mm/yyyy',
      //  container: container_installed,
        todayHighlight: true,
        autoclose: true,
        orientation: "bottom auto",
        language: 'pt-BR',
    });

    //our date input has the name "date"
    var valid_input=$('#id_valid');
    //var container_valid =$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
    valid_input.datepicker({
        format: 'dd/mm/yyyy',
      //  container: container_installed,
        todayHighlight: true,
        autoclose: true,
        orientation: "bottom auto",
        language: 'pt-BR',
    });

    // token csfr for ajax
    var csrftoken = $.cookie('csrftoken');
    // token csfr for ajax
    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
    // token csfr for ajax
    $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }

            }
        });

    // modal create ajax
    $('.js-send-create-or-update').click(function (e){
        e.preventDefault();
        var form = $('.js-modal-form-add');

        $.ajax({
            type: 'post',
            url: 'create/',
            data: form.serialize(),
            dataType: 'json',
            success: function(data){
                $('#modal-add').modal('hide');

                if (data.is_form_valid){
                    $("#js-alert-title").text(data.title);
                    $("#js-alert-serial").html(data.serial);
                    $("#js-alert-cliente").html(data.cliente);

                    if (data.method == 'update'){
                        $('.table > tbody  > tr').each(function() {
                              var row = $(this).closest('tr');
                              var serial =  row.find('td:eq(3)').text();
                              if(data.licenses.license.serial == serial){
                                    var date_ = data.licenses.license.valid.split('-');
                                    row.find('td:eq(1)').text(data.licenses.license.cliente.toUpperCase());
                                    row.find('td:eq(2)').text(data.licenses.license.mac_address.toUpperCase());
                                    row.find('td:eq(4)').text(date_[1] +'/'+ date_[2] +'/'+ date_[0]);
                              }
                        });

                    }

                    if(data.method == 'create'){
                        alert('foi criando um cara aqui!')
                        var table =  $('#lisence_table').DataTable();
                        table.row.add([
                            data.licenses.license.id,
                            data.licenses.license.cliente,
                            data.licenses.license.mac_address,
                            data.licenses.license.serial,
                            data.licenses.license.valid,

                            // ADD Button details license
                            '<button class="btn btn-primary js-send_details" type="submit"> DATLHES</button>',

                            // add Button deactivate license
                            '<td ><button class="btn btn-danger js-send_deactivate" type="button" data-toggle="modal" ' +
                            'data-target="#modal-deactivate"> DESATIVAR </button></td>'
                            ]).draw();

                    }

                    $('#alert').modal("show");
                }
            }
        });
    });


    // modal details to updade license
    var value_id;
    $('.js-send_details').click(function(event){
        event.preventDefault();
        var currentRow = $(this).closest("tr"); // get the current  row
        var value = currentRow.find("td:eq(0)").text(); // get current row 1st TD value
        value_id = value;

        $.ajax({
            type: "GET",
            url: "detail/",
            data: {"license_id" : value_id },
            success: function(data) {
               $('#modal-add').modal('show');
               var installed =  data.installed.split('-')
               var valid =  data.valid.split('-')
               $('#client_id').text(data.id);
               $('#id_cliente').val(data.cliente);
               $('#id_serial').val(data.serial);
               $('#id_mac_address').val(data.mac_address);
               $('#id_key').val(data.key);
               $('#id_installed').val(data.installed);
               $('#id_valid').val(data.valid);
               $('#id_tecnico').text(data.tecnico_name);
            } // end  sucess :
         }); // end $.ajax
    }); //  end $('.senddetails')


    // REFATORAR
    $('.js-send_deactivate').click(function (){
        var currentRow =  $(this).closest('tr'); // get current row of the table

        var message_cliente = "<span class= p-temp' > <strong>CLIENTE: " +currentRow.find('td:eq(1)').text() + " </strong> </span> </br>";
        var message_mac_address = "<span class=' p-temp'> <strong>MAC_ADRESS: " +currentRow.find('td:eq(2)').text() + "</strong></span> </br>";
        var message_serial = "<span class=' p-temp'> <strong>SERIAL: " +currentRow.find('td:eq(3)').text() + "</strong></span>";
        $('.deactive_license').append(message_cliente);
        $('.deactive_license').append(message_mac_address);
        $('.deactive_license').append(message_serial);

    });

    // remove paragraph  from modal deactivate license
      $('#modal-deactivate').on('hidden.bs.modal', function(e){
        $(".p-temp").remove();

      });

});
