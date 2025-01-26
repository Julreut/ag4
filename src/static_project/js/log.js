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

document.addEventListener("click", function (event) {
  // Sucht das nächste Button- oder Link-Element
  const target = event.target.closest("button, a");

  if (target) {
    // Allgemeine Log-Daten erfassen
    const logData = {
      url: target.href || window.location.href || "No Url", // URL des Links oder aktuelle URL
      text: target.innerText || target.value || "No text", // Text des Elements
      tag: target.tagName || "No Tag", // Typ des Elements (z. B. BUTTON oder A)
      id: target.id || "No ID", // ID des Elements
      class: target.className || "No class", // Klassen des Elements
    };

    // Zusätzliche Daten aus `data-*`-Attributen erfassen (falls vorhanden)
    if (target.dataset.action) {
      logData.action = target.dataset.action;
    }
    if (target.dataset.commentId) {
      logData.comment_id = target.dataset.commentId;
    }

    console.log("Element clicked:", logData); // Debug-Ausgabe

    // Log-Daten senden
    logUserAction("click", logData);
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
// Event-Listener für "Mehr lesen/Weniger lesen" und "Mehr lesen & interagieren"
document.addEventListener("click", function (event) {
  const target = event.target;

  // Logik für "Mehr lesen/Weniger lesen"
  if (target.classList.contains("read-more") && target.dataset.replyId) {
    const replyId = target.dataset.replyId; // ID der Antwort
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

  // Logik für "Mehr lesen & interagieren"
  if (
    target.classList.contains("read-more") &&
    target.dataset.action === "read_and_interact"
  ) {
    const articleId = target.dataset.articleId || null; // Kommentar-ID
    const commentId = target.dataset.commentId || null; // Kommentar-ID
    const url = target.href || window.location.href;

    console.log(
      "Gesendete Daten:",
      JSON.stringify({
        event_type: "read_and_interact",
        event_data: {
          article_id: articleId,
          comment_id: commentId,
          url: url,
        },
      })
    );

    logUserAction("read_and_interact", {
      comment_id: commentId,
      url: url,
    });

    // Optional: Navigation verhindern und Logging sicherstellen
    event.preventDefault();
    setTimeout(() => {
      window.location.href = target.href;
    }, 100); // Leichte Verzögerung für das Logging
  }
});

// Show the reply form on button click
document.addEventListener("click", function (event) {
  const target = event.target;

  if (target.id === "show-article-form") {
    const articleId = target.dataset.articleId; // Kommentar-ID aus dem data-Attribut
    const commentForm = document.getElementById("article-form");

    if (commentForm) {
      logUserAction("write_comment_opened", { article_id: articleId }); // Loggen

      if (commentForm.style.display === "none") {
        commentForm.style.display = "block";
        target.style.display = "none";
      }
    } else {
      console.error("Kommentarformular konnte nicht gefunden werden.");
    }
  }
});

// Log event when the reply is submitted
document.addEventListener("submit", function (event) {
  const form = event.target;

  if (form.classList.contains("article-form")) {
    const articleId = form.dataset.articleId; // Kommentar-ID aus dem data-Attribut
    const commentTitle =
      document.getElementById("comment-title")?.value || "No title";

    const commentText =
        form.querySelector("textarea[name='content']")?.value ||"No content";

    logUserAction("write_comment_submitted", {
      article_id: articleId,
      comment_title: commentTitle,
      comment_text: commentText,
    });
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
      form.querySelector("input[name='title']")?.value || "No title";

    const replyText =
        form.querySelector("textarea[name='content']")?.value ||"No content";

    logUserAction("write_reply_submitted", {
      comment_id: commentId,
      reply_title: replyTitle,
      reply_text: replyText,
    });
  }
});

document.addEventListener(
  "focus",
  function (event) {
    const target = event.target;

    // Tracke sowohl das "title"-Eingabefeld als auch das "content"-Textarea
    if (
      (target.name === "title" && target.type === "text") || // Eingabefeld
      (target.name === "content" && target.tagName === "TEXTAREA") // Textarea
    ) {
      const logData = {
        input_name: target.name, // Name des Eingabefelds (z. B. "title" oder "content")
        placeholder: target.placeholder || "No placeholder", // Platzhaltertext
        class: target.className || "No class", // CSS-Klasse des Eingabefelds
      };

      console.log("Input field focused:", logData); // Debug-Ausgabe
      // Loggen
      logUserAction("input_focus", logData);
    }
  },
  true // Capture-Phase, um das `focus`-Event korrekt abzufangen
);

document.addEventListener("input", function (event) {
  const target = event.target;

    if (
      (target.name === "title" && target.type === "text") || // Eingabefeld
      (target.name === "content" && target.tagName === "TEXTAREA") // Textarea
    ) {
      const logData = {
        input_name: target.name,
        current_value: target.value, // Der aktuelle Text im Textarea-Feld
      };

      console.log("Textarea updated:", logData); // Debug-Ausgabe
      // Loggen
      logUserAction("input_change", logData);
    }
});
