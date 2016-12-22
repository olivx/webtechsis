
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
                source: '/lisences/autocomplete/'
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





});
