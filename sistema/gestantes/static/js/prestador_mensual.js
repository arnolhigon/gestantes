function configurarPagina(titulo, buscarTexto, mensajeAlerta) {
  $("#table_title").text(titulo);
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
      var searchInput = $(".dataTables_filter input").removeClass("form-control-sm").attr("placeholder", buscarTexto);
      $(".dataTables_filter").html($('<div class="search_container"></div>').append(searchInput));
    },
  });

  $(".circle-container").click(function (e) {
    e.preventDefault();
    $("#table_title").text(mensajeAlerta);
/*     $(".car2, .car3").toggle(); */
    $(".circle-container").toggle()
    showAlert(mensajeAlerta, "info");
  });

  $(".btn-close").click(function (e) {
    e.preventDefault();
    $(".car3, .car2").toggle();
    location.reload(); // Esto recargará la página
  });
}

function showAlert(message, type) {
  var alertDiv = document.createElement("div");
  alertDiv.className = `my-custom-alert alert-${type === "success" ? "success" : type === "info" ? "info" : type === "warning" ? "warning" : type === "error" ? "error" : "secondary"}`;
  alertDiv.innerHTML = `<i class="fa ${type === "success" ? "fa-check" : type === "info" ? "fa-info" : type === "warning" ? "fa-exclamation-triangle" : type === "error" ? "fa-exclamation-circle" : "fa-comments"}" aria-hidden="true"></i> ${message}`;
  document.getElementById("alert-container").appendChild(alertDiv);
  setTimeout(function () {
    alertDiv.remove();
  }, 5000);
}