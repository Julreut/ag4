$(document).ready(function () {
  // UI-Interaktionen (Modal und Dropdown)
  $("#modal-btn").click(function () {
    $(".ui.modal").modal("show");
  });

  $(".ui.dropdown").dropdown();

  // Zeit-Tracking
  let startTime = Date.now(); // Startzeit speichern

  // Event-Listener für das Verlassen der Seite
  $(window).on("beforeunload", function () {
    let duration = Date.now() - startTime; // Zeit in Millisekunden

    fetch(logTimeSpentURL, {
      // Definieren Sie `logTimeSpentURL` im Template
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken, // Definieren Sie `csrfToken` im Template
      },
      body: JSON.stringify({
        page_type: "newspaper", // Seite
        id: null, // ID der Seite, falls vorhanden
        duration_ms: duration, // Dauer
      }),
    }).catch((err) => console.error("Error logging time_spent:", err));
  });
});
