// Funktion, um den Pfad aus einer URL zu extrahieren
function getPathFromUrl(url) {
  try {
    const parsedUrl = new URL(url, window.location.origin); // Sicherstellen, dass die URL vollständig ist
    return parsedUrl.pathname; // Gibt nur den Pfad zurück (z. B. "/profiles/myprofile/")
  } catch (error) {
    console.error("Fehler beim Parsen der URL:", error);
    return url; // Fallback zur ursprünglichen URL
  }
}

// Funktion, um ein Logging-Event zu senden
function logUserAction(eventType, eventData = {}) {
  if (!logActionUrl || !csrfToken) {
    console.error("logActionUrl oder csrfToken fehlt!");
    return;
  }

  fetch(logActionUrl, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrfToken,
    },
    body: JSON.stringify({
      event_type: eventType,
      event_data: eventData,
    }),
  })
    .then((response) => {
      if (!response.ok) {
        console.error("Fehler beim Loggen der Aktion:", response.statusText);
      }
    })
    .catch((error) =>
      console.error("Fehler beim Senden der Log-Daten:", error)
    );
}

// Seitenaufrufe loggen
document.addEventListener("DOMContentLoaded", function () {
  logUserAction("page_view", {
    url: getPathFromUrl(window.location.href),
    title: document.title,
  });
});

// Klicks auf Links und Buttons loggen
document.addEventListener("click", function (event) {
  const target = event.target;

  // Prüfen, ob der Klick auf einen Button oder Link erfolgt
  if (target.tagName === "A" || target.tagName === "BUTTON") {
    logUserAction("click", {
      url: getPathFromUrl(target.href || window.location.href),
      text: target.innerText || target.value || "No text",
      tag: target.tagName,
      id: target.id || "No ID",
      class: target.className || "No class",
    });
  }
});

// Kommentar-Post-Aktionen loggen
document.addEventListener("submit", function (event) {
  const form = event.target;

  // Prüfen, ob das Formular für das Posten eines Kommentars ist
  if (form.classList.contains("comment-form")) {
    const commentText =
      form.querySelector("textarea[name='content']")?.value || "No content";
    const commentTitle =
      form.querySelector("input[name='title']")?.value || "No title";
    const articleId =
      form.querySelector("input[name='article_id']")?.value ||
      "Unknown article";
    const parentCommentId =
      form.querySelector("input[name='parent_comment_id']")?.value || null; // Falls es ein Reply ist

    logUserAction("comment_post", {
      url: getPathFromUrl(window.location.href), // Aktuelle URL
      comment_title: commentTitle,
      comment_text: commentText,
      article_id: articleId,
      parent_comment_id: parentCommentId,
    });
  }
});

// Toggle "Mehr lesen/Weniger lesen"
document.addEventListener("click", function (event) {
  const target = event.target;

  if (target.classList.contains("read-more")) {
    const replyId = target.dataset.replyId; // ID des Kommentars/Antworts
    const replyTitle = target.dataset.replyTitle; // Titel der Antwort
    const fullContent = document.getElementById(`content-${replyId}`);
    const shortContent = document.getElementById(`content-${replyId}-short`);

    if (fullContent && shortContent) {
      if (fullContent.style.display === "none") {
        fullContent.style.display = "block";
        shortContent.style.display = "none";
        target.textContent = "Weniger lesen";
        logUserAction("read_more", {
          reply_id: replyId,
          reply_title: replyTitle,
        });
      } else {
        fullContent.style.display = "none";
        shortContent.style.display = "block";
        target.textContent = "Mehr lesen";
        logUserAction("read_less", {
          reply_id: replyId,
          reply_title: replyTitle,
        });
      }
    } else {
      console.error("Inhalt für die Antwort konnte nicht gefunden werden.");
    }
  }
});

// Show the reply form on button click
document.addEventListener("click", function (event) {
  const target = event.target;

  if (target.id === "show-reply-form") {
    const commentId = target.dataset.commentId; // Kommentar-ID aus dem data-Attribut
    const replyForm = document.getElementById("reply-form");

    if (replyForm) {
      logUserAction("write_reply_opened", { comment_id: commentId }); // Loggen

      if (replyForm.style.display === "none") {
        replyForm.style.display = "block";
        target.style.display = "none";
      }
    } else {
      console.error("Antwortformular konnte nicht gefunden werden.");
    }
  }
});

// Log event when the reply is submitted
document.addEventListener("submit", function (event) {
  const form = event.target;

  if (form.classList.contains("reply-form")) {
    const commentId = form.dataset.commentId; // Kommentar-ID aus dem data-Attribut
    const replyTitle =
      document.getElementById("reply-title")?.value || "No title";

    logUserAction("write_reply_submitted", {
      comment_id: commentId,
      reply_title: replyTitle,
    });
  }
});

