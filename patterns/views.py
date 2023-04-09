from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

from patterns.models import CrochetPatternForm, SKILL_LEVEL_CHOICES, REGION_CHOICES, CrochetPattern


def _choices_to_dict(choices: list[tuple[str, str]]) -> list[dict[str, str]]:
    return [
        {"value": value, "text": text}
        for value, text
        in choices
    ]


def create_pattern(request) -> HttpResponse:
    if request.method == "POST":
        form = CrochetPatternForm(request.POST)
        if form.is_valid():
            new_pattern = form.save(commit=False)
            new_pattern.author = request.user
            new_pattern.save()
            messages.success(request, "Pattern created successfully.")
            return redirect("/patterns/my-patterns")
    else:
        form = CrochetPatternForm()
        context = {
            "form": form,
            "skill_level_options": _choices_to_dict(SKILL_LEVEL_CHOICES),
            "region_options": _choices_to_dict(REGION_CHOICES)
        }
        return render(request, "patterns/create-pattern.html", context)


def edit_pattern(request, pattern_id: int) -> HttpResponse:
    pattern = CrochetPattern.objects.get(pk=pattern_id)
    if request.method == "POST":
        if pattern.author != request.user:
            messages.error(request, "You can only edit your own patterns.")
            return redirect("/patterns/my-patterns")
        form = CrochetPatternForm(request.POST, instance=pattern)
        if form.is_valid():
            form.save()
            messages.success(request, "Pattern edited successfully.")
            return redirect("/patterns/my-patterns")
    else:
        form = CrochetPatternForm(instance=pattern)
        context = {
            "pattern": pattern,
            "skill_level_options": _choices_to_dict(SKILL_LEVEL_CHOICES),
            "region_options": _choices_to_dict(REGION_CHOICES)
        }
        return render(request, "patterns/edit-pattern.html", context)


def delete_pattern(request, pattern_id: int) -> HttpResponse:
    pattern = CrochetPattern.objects.get(pk=pattern_id)
    if request.method != "POST":
        messages.error(request, "You can only delete patterns from the 'My Patterns' page.")
        return redirect("/patterns/my-patterns")
    if pattern.author != request.user:
        messages.error(request, "You can only delete your own patterns.")
        return redirect("/patterns/my-patterns")
    pattern.delete()
    messages.success(request, "Pattern deleted successfully.")
    return redirect("/patterns/my-patterns")


def get_user_patterns(request) -> HttpResponse:
    patterns = request.user.crochetpattern_set.all()
    context = {
        "patterns": patterns
    }
    return render(request, "patterns/user-patterns.html", context)


def view_pattern(request, pattern_id: int) -> HttpResponse:
    pattern = CrochetPattern.objects.get(pk=pattern_id)
    context = {
        "pattern": pattern
    }
    return render(request, "patterns/view-pattern.html", context)


def browse_patterns(request) -> HttpResponse:
    patterns = CrochetPattern.objects.all()
    context = {
        "patterns": patterns
    }
    return render(request, "patterns/browse-patterns.html", context)
