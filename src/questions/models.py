from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Question(models.Model):
    QUESTION_TYPES = [
        ('dropdown', 'Dropdown'),
        ('likert', 'Likert Scale'),
        ('multiple_choice', 'Multiple Choice'),
        ('single_choice', 'Single Choice'),
        ('numeric', 'Numeric Scale'),
        ('open_text', 'Open Text'),
    ]

    label = models.CharField(
        max_length=10,
        choices=[('before', 'Before'), ('after', 'After')],
        help_text="Gibt an, ob die Frage vor oder nach dem Experiment gestellt wird."
    )
    question_text = models.TextField(help_text="Der Text der Frage.")
    question_type = models.CharField(
        max_length=20,
        choices=QUESTION_TYPES,
        help_text="Der Typ der Frage."
    )
    choices = models.TextField(
        blank=True,
        help_text="Komma-separierte Auswahlmöglichkeiten für Fragen mit vordefinierten Antworten (z.B. Dropdown, Likert-Skala)."
    )
    min_value = models.IntegerField(
        blank=True, null=True,
        help_text="Minimaler Wert für numerische Fragen."
    )
    max_value = models.IntegerField(
        blank=True, null=True,
        help_text="Maximaler Wert für numerische Fragen."
    )
    required = models.BooleanField(
        default=True,
        help_text="Ob die Frage beantwortet werden muss."
    )

    def get_choices(self):
        """Gibt eine Liste der Auswahlmöglichkeiten zurück."""
        if self.choices:
            return [choice.strip() for choice in self.choices.split(',')]
        return []

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

    class Meta:
        unique_together = ('question', 'user')

    def __str__(self):
        return f"Antwort von {self.user.username} auf '{self.question.question_text[:50]}'"

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

    identifier = models.CharField(max_length=200, choices=IDENTIFIER_CHOICES, unique=True, help_text="Choose which text to display.")
    content = models.TextField(help_text="HTML or plain text content.")
    visibility = models.BooleanField(default=False)

    def __str__(self):
        return self.identifier
    
class Consent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    consent_given = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consent by {self.user.username} at {self.timestamp}"
    
    
class SessionConfig(models.Model):
    max_duration = models.PositiveIntegerField(
        default=3600,  # Standard: 1 Stunde
        help_text="Maximale Zeit in Sekunden, bevor der Benutzer automatisch ausgeloggt wird."
    )

    def __str__(self):
        return f"SessionConfig: {self.max_duration} Sekunden"
