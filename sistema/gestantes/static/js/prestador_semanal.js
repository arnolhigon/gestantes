$(document).ready(function () {
    $("#miTabla").DataTable({
        paging: true,
        pageLength: 7,
        language: {
            url: "https://cdn.datatables.net/plug-ins/1.10.25/i18n/Spanish.json",
        },
        info: false,
        ordering: false,
        searching: true,
        dom: '<"top"f>rt<"bottom"lp><"clear">',
        initComplete: function () {
            var searchInput = $(".dataTables_filter input");
            searchInput.removeClass("form-control-sm");
            searchInput.attr("placeholder", "Buscar");
            var searchContainer = $('<div class="search_container"></div>');
            searchContainer.append(searchInput);
            $(".dataTables_filter").html(searchContainer);
        }
    });

    $(".circle-text a").click(function (e) {
        e.preventDefault();
        $(".car2").hide();
        $(".car3").show();
        showAlert("Nuevo Cargue Abierto", "info"); 
    });

    $(".btn-close").click(function (e) {
        e.preventDefault();
        $(".car3").hide();
        $(".car2").show();
    });
});

function showAlert(message, type) {
    // Crea un elemento div para la alerta
    var alertDiv = document.createElement("div");
    alertDiv.className = "my-custom-alert";
  
    // Agrega el mensaje y el icono al contenido del elemento
    if (type === "success") {
      alertDiv.innerHTML = `<i class="fa fa-check" aria-hidden="true"></i> ${message}`;
      alertDiv.classList.add("alert-success");
    } else {
      alertDiv.textContent = message;
      if (type === "info") {
        alertDiv.innerHTML = `<i class="fa fa-info" aria-hidden="true"></i> ${message}`;
        alertDiv.classList.add("alert-info");
      } else if (type === "warning") {
        alertDiv.innerHTML = `<i class="fa fa-exclamation-triangle" aria-hidden="true"></i> ${message}`;
        alertDiv.classList.add("alert-warning");
      } else if (type === "error") {
        alertDiv.innerHTML = `<i class="fa fa-exclamation-circle" aria-hidden="true"></i> ${message}`;
        alertDiv.classList.add("alert-error");
      } else {
        alertDiv.innerHTML = `<i class="fa fa-comments" aria-hidden="true"></i> ${message}`;
        alertDiv.classList.add("alert-secondary");
      }
    }
  
    // Agrega la alerta al contenedor
    document.getElementById("alert-container").appendChild(alertDiv);
  
    // Oculta la alerta después de un tiempo
    setTimeout(function () {
      alertDiv.remove();
    }, 5000);
  }
  