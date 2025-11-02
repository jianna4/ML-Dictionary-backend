from django.db import models

# Create your models here.
from django.db import models

class Term(models.Model):
    """Main entry for a machine learning dictionary term."""
    name = models.CharField(max_length=255, unique=True)
    meaning = models.TextField()
    meaning_source = models.CharField(
    max_length=500,
    blank=True,
    null=True,
    help_text="Source of the meaning (optional: book, article, or website URL)"
)

    # Meta info for better admin sorting
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Example(models.Model):
    """Example code snippets for a term."""
    term = models.ForeignKey(
        Term,
        on_delete=models.CASCADE,
        related_name='examples'
    )
    code = models.TextField()
    description = models.TextField(blank=True, null=True)  # optional short explanation

    def __str__(self):
        return f"Example for {self.term.name}"


class ReferenceLink(models.Model):
    """External links related to a term (e.g., documentation, tutorials)."""
    term = models.ForeignKey(
        Term,
        on_delete=models.CASCADE,
        related_name='links'
    )
    title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return f"{self.title} - {self.term.name}"
