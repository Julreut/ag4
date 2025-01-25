from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Question(models.Model):
    QUESTION_TYPES = [
        ('dropdown', 'Dropdown'),
        ('multiple_choice', 'Multiple Choice'),
        ('single_choice', 'Single Choice'),
        ('numeric', 'Numeric Scale'),
        ('open_text', 'Open Text'),
        ('slider', 'Slider'),
        ('multiple_likert', 'Multiple Likert'),
        ('ampel_rating', 'Ampel Rating')
    ]
    name = models.TextField(
        blank=True,
        help_text="Für alle Fragetypen: Hier bitte den Item-Name festlegen (Spalte 'name' in der questions Datenbanktabelle)."
    )
    question_type = models.CharField(
            max_length=20,
            choices=QUESTION_TYPES,
            help_text="Für alle Fragetypen: Hier bitte den Fragen-Typ auswählen."
        )
    label = models.CharField(
        max_length=10,
        choices=[('before', 'Before'), ('after', 'After')],
        help_text="Für alle Fragetypen: Gibt an, ob die Frage vor oder nach dem Experiment gestellt wird."
    )
    question_text = models.TextField(help_text="Für alle Fragetypen: Welche Frage soll in diesem Item gestellt werden?")

    choices = models.TextField(
        blank=True,
        help_text="Für alle Fragetypen mit <strong>vordefinierten Choices</strong>. <br> Dropdown, Multiple/Single Choice, Likert, Multiple Likert, Slider.<br> Für Slider: Bitte genau drei Möglichkeiten passend zu den Min und Max Werten angeben. <br>Angabe: Semikolon-separierte Auswahlmöglichkeiten."
    )
    sub_questions = models.TextField(
        blank=True,
        help_text=" <strong>NUR für Multiple Likert.</strong> <br>Angabe: Semikolon-separierte Sub-Fragen."
    )
    sub_choices = models.TextField(
        blank=True,
        help_text=" <strong>NUR für Ampel-Frage. </strong><br>Angabe von Tupeln für Fragenpole als semikolon-separierte Sub-Choices. <br>Beispieltext: negativ;positiv;ineffektiv;effektiv"
    )
    min_value = models.IntegerField(
        blank=True, null=True,
        help_text=" <strong>Für Numeric Scale und Slider: </strong> Minimaler Wert."
    )
    max_value = models.IntegerField(
        blank=True, null=True,
        help_text=" <strong>Für Numeric Scale und Slider: </strong> Maximaler Wert."
    )
    step_value = models.IntegerField(
        blank=True, null=True,
        help_text=" <strong>Für Slider: </strong> Stepgröße."
    )
    start_value = models.IntegerField(
        blank=True, null=True,
        help_text=" <strong>Für Slider: </strong> Startwert. Bitte Wert im Bereich von Min und Max Value wählen."
    )
    
    required = models.BooleanField(
        default=True,
        help_text="Pflichtfrage?"
    )

    def get_choices(self):
        """Gibt eine Liste der Auswahlmöglichkeiten zurück."""
        if self.choices:
            return [choice.strip() for choice in self.choices.split(';')]
        return []
    
    def get_sub_questions(self):
        """Gibt eine Liste der Sub-Fragen zurück."""
        if self.sub_questions:
            return [sub.strip() for sub in self.sub_questions.split(';')]
        return []
    
    def get_subchoices(self):
        if self.sub_choices:
            return [sub.strip() for sub in self.sub_choices.split(';')]
        return []
    
    # Subchoices ausgeben

    def get_subchoice_pairs(self):
        """Teilt die Subchoices in Paare (linke und rechte Labels)."""
        subchoices = self.get_subchoices()
        return list(zip(subchoices[::2], subchoices[1::2]))

    
    def clean(self):
        """Validierung des Modells."""
        if self.question_type in ['dropdown', 'likert', 'multiple_choice', 'single_choice']:
            if not self.choices:
                raise ValidationError(f"Für den Fragetyp '{self.get_question_type_display()}' müssen Auswahlmöglichkeiten angegeben werden.")
        if self.question_type == 'numeric':
            if self.min_value is None or self.max_value is None:
                raise ValidationError("Für numerische Fragen müssen 'min_value' und 'max_value' festgelegt werden.")

    def __str__(self):
        return f"{self.get_label_display()} - {self.question_text[:50]}"

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sub_question = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        help_text="Optional: Sub-question identifier for formats like Multiple Likert."
    )

    class Meta:
        unique_together = ('question', 'user',  'sub_question')

    def __str__(self):
        return f"{self.user.username} - {self.question.question_text} - {self.sub_question or 'Main'}"

class Text(models.Model):
    IDENTIFIER_CHOICES = [
        ##END
        ('end_experiment_header_de', 'End Experiment Header (German)' ),
        ('end_experiment_header_en', 'End Experiment Header (English)' ),
        ('end_experiment_message_de', 'End Experiment Message (German)'),
        ('end_experiment_message_en', 'End Experiment Message (English)'),
        
        ##INFO
        ('participant_info_header_de', 'Participant Information Header (German)'),
        ('participant_info_header_en', 'Participant Information Header (English)'),
        ('participant_info_message_de', 'Participant Information Message (German)'),
        ('participant_info_message_en', 'Participant Information Message (English)'),

        ## CONSENT
        ('consent_form_header_de', 'Consent Form Header (German)'),
        ('consent_form_header_en', 'Consent Form Header (English)'),
        ('consent_form_message_de', 'Consent Form Message (German)'),
        ('consent_form_message_en', 'Consent Form Message (English)'),
        ('no_consent_message_de', 'No Consent (German)'),
        ('no_consent_message_en', 'No Consent (English)'),
    ]

    identifier = models.CharField(max_length=200, choices=IDENTIFIER_CHOICES, unique=True, help_text="Textart auswählen.")
    content = models.TextField(help_text="HTML text sorgt dafür, dass der Content deutlich besser lesbar ist. Hierfür einfach den Plain Text in ChatGPT o.Ä. einfügen mit dem Prompt <br>'Erstelle eine anschauliche HTML-Seite mit folgendem Plaintext: [<i>Text hier einfügen</i>] <br>Der Titel der Seite sollte [<i>Titel</i>] lauten. Der Haupttext soll in der Mitte der Seite stehen, mit einer roten Überschrift und einer Beschreibung darunter. <br>Füge auch eine Kontaktmöglichkeit per E-Mail hinzu. Die Seite soll ansprechend und responsiv gestaltet sein.'")
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.identifier
    
class Consent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consent_given = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consent by {self.user.username} at {self.timestamp}"
    
    
# class SessionConfig(models.Model):
#     max_duration = models.PositiveIntegerField(
#         default=3600,  # Standard: 1 Stunde
#         help_text="Maximale Zeit in Sekunden, bevor der Benutzer automatisch ausgeloggt wird."
#     )
#     is_timer_enabled = models.BooleanField(default=False, help_text="Timer aktivieren oder deaktivieren")

#     def __str__(self):
#         return f"SessionConfig: {self.max_duration} Sekunden (Timer {'Enabled' if self.is_timer_enabled else 'Disabled'})"