$(document).ready(function () {
  // UI-Interaktionen (Modal und Dropdown)
  $("#modal-btn").click(function () {
    $(".ui.modal").modal("show");
  });

  $(".ui.dropdown").dropdown();
});
