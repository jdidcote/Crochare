from django.contrib import messages
from django.shortcuts import render, redirect

from patterns.models import CrochetPatternForm, SKILL_LEVEL_CHOICES, REGION_CHOICES


def _choices_to_dict(choices: list[tuple[str, str]]) -> list[dict[str, str]]:
    return [
        {"value": value, "text": text}
        for value, text
        in choices
    ]


def create_pattern(request):
    if request.method == "POST":
        form = CrochetPatternForm(request.POST)
        print(form.errors)
        if form.is_valid():
            new_pattern = form.save(commit=False)
            new_pattern.author = request.user
            new_pattern.save()
            messages.success(request, "Pattern created successfully.")
            return redirect("/")
    else:
        form = CrochetPatternForm()
        context = {
            "form": form,
            "skill_level_options": _choices_to_dict(SKILL_LEVEL_CHOICES),
            "region_options": _choices_to_dict(REGION_CHOICES)
        }
        return render(request, "patterns/create-pattern.html", context)
