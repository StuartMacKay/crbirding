from django.db import models
from django.utils.translation import gettext_lazy as _

from .position import Position


class Rule(models.Model):
    """Rules are regular expressions for matching against encoded colour
    marks so the project that marked a bird can be identified.

    Projects use specific colours and codes which do not overlap (in theory
    at least). That makes it possible to create regular expressions which
    can be used to map an entire sequence of codes to a project. For example
    one of the project marking Lesser Black-backed Gulls in Norway use black
    rings with a white inscription. The inscription starts with the letter 'J',
    followed by three digits and a letter. This can be represented be the
    regular expression, '^NW\(J\d{3}[A-Z]\)$'. You can also create regular
    expressions with a wider scope, e.g. '^[A-Z][A-Z]\(J' to find all projects
    in Norway.

    Building the expressions is time-consuming but being able to identify a
    project as soon as the encoding is entered saves an immense amount of time.

    """

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created"),
        help_text=_("When was the record created."),
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_("updated"),
        help_text=_("When was the record last updated."),
    )
    species = models.ForeignKey(
        "core.Species",
        on_delete=models.PROTECT,
        related_name="patterns",
        verbose_name=_("species"),
        help_text=_("The species of bird being marked by the project."),
    )
    position = models.TextField(
        choices=Position.choices,
        verbose_name=_("position"),
        help_text=_("The position of the colour mark on the bird."),
    )
    regex = models.TextField(
        verbose_name=_("regex"), help_text=_("A regular expression for matching colour marks.")
    )
    project = models.ForeignKey(
        "core.Project",
        on_delete=models.CASCADE,
        related_name="patterns",
        verbose_name=_("project"),
        help_text=_("The project that marked the bird."),
    )

    class Meta:
        verbose_name = _("rule")
        verbose_name_plural = _("rules")

    def __str__(self) -> str:
        return f"{self.regex} ({self.get_position_display()}) → {self.project}"
