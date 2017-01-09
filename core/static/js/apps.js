
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
    });



        var instaled_input=$('#id_installed'); //our date input has the name "date"
        //var container_installed =$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
        instaled_input.datepicker({
            format: 'dd/mm/yyyy',
          //  container: container_installed,
            todayHighlight: true,
            autoclose: true,
            orientation: "bottom auto",
    	    language: 'pt-BR',
        });


        var valid_input=$('#id_valid'); //our date input has the name "date"
        //var container_valid =$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
        valid_input.datepicker({
            format: 'dd/mm/yyyy',
          //  container: container_installed,
            todayHighlight: true,
            autoclose: true,
            orientation: "bottom auto",
    	    language: 'pt-BR',
        });


        var csrftoken = $.cookie('csrftoken');

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





        var value_id;
        $(function(){
            $('.senddetails').click(function(event){
            event.preventDefault();

                    var currentRow = $(this).closest("tr"); // get the current  row
                    var value = currentRow.find("td:eq(0)").text(); // get current row 1st TD value
                    value_id = value;

                $.ajax({
                    type: "GET",
                    url: "api/",
                    data: {"license_id" : value_id },
                    success: function(data) {

                        $('#modal-add').modal('show');

                       // id cliente
                       $('#client_id').text(data[0].id);
                       $('#id_cliente').val(data[0].cliente);
                       $('#id_serial').val(data[0].serial);
                       $('#id_mac_address').val(data[0].mac_address);
                       $('#id_key').val(data[0].key);
                       $('#id_installed').val(data[0].installed);
                       $('#id_valid').val(data[0].valid);



                    } // end  sucess :
                }); // end $.ajax
            }); //  end $('.senddetails')
        }); // end function

});
