from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404

from apps.contact.models import Contact

from .forms import LoginForm, ContactForm
from .registry import RESOURCES, NAV_ITEMS, NAV_CODES


def _get_resource(key):
    resource = RESOURCES.get(key)
    if resource is None:
        raise Http404("Unknown resource")
    return resource


def login_view(request):
    if request.user.is_authenticated:
        return redirect("panel:dashboard")

    form = LoginForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(
            request,
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],
        )
        if user is not None:
            login(request, user)
            return redirect("panel:dashboard")

    return render(request, "panel/login.html", {"form": form})


@login_required(login_url="panel:login")
def logout_view(request):
    logout(request)
    return redirect("panel:login")


@login_required(login_url="panel:login")
def dashboard(request):
    counts = [
        {"label": resource["label"], "key": key, "count": resource["model"].objects.count()}
        for key, resource in RESOURCES.items()
    ]
    context = {
        "counts": counts,
        "nav_items": NAV_ITEMS,
        "active_key": "dashboard",
        "sheet_code": NAV_CODES["dashboard"],
    }
    return render(request, "panel/dashboard.html", context)


@login_required(login_url="panel:login")
def resource_list(request, key):
    resource = _get_resource(key)
    objects = resource["model"].objects.all().order_by(resource["order_by"])

    query = request.GET.get("q", "").strip()
    if query and resource["search_fields"]:
        from django.db.models import Q

        condition = Q()
        for field in resource["search_fields"]:
            condition |= Q(**{f"{field}__icontains": query})
        objects = objects.filter(condition)

    rows = [
        {"pk": obj.pk, "values": [getattr(obj, field) for field in resource["list_fields"]]}
        for obj in objects
    ]

    context = {
        "resource": resource,
        "key": key,
        "rows": rows,
        "query": query,
        "nav_items": NAV_ITEMS,
        "active_key": key,
        "sheet_code": NAV_CODES.get(key, ""),
    }
    return render(request, "panel/resource_list.html", context)


@login_required(login_url="panel:login")
def resource_create(request, key):
    resource = _get_resource(key)
    form = resource["form"](request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"{resource['singular']} created.")
        return redirect("panel:resource_list", key=key)

    context = {
        "resource": resource,
        "key": key,
        "form": form,
        "nav_items": NAV_ITEMS,
        "is_create": True,
        "active_key": key,
        "sheet_code": NAV_CODES.get(key, ""),
    }
    return render(request, "panel/resource_form.html", context)


@login_required(login_url="panel:login")
def resource_edit(request, key, pk):
    resource = _get_resource(key)
    instance = get_object_or_404(resource["model"], pk=pk)
    form = resource["form"](request.POST or None, request.FILES or None, instance=instance)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"{resource['singular']} updated.")
        return redirect("panel:resource_list", key=key)

    context = {
        "resource": resource,
        "key": key,
        "form": form,
        "instance": instance,
        "nav_items": NAV_ITEMS,
        "is_create": False,
        "active_key": key,
        "sheet_code": NAV_CODES.get(key, ""),
    }
    return render(request, "panel/resource_form.html", context)


@login_required(login_url="panel:login")
def resource_delete(request, key, pk):
    resource = _get_resource(key)
    instance = get_object_or_404(resource["model"], pk=pk)
    if request.method == "POST":
        instance.delete()
        messages.success(request, f"{resource['singular']} deleted.")
        return redirect("panel:resource_list", key=key)

    context = {
        "resource": resource,
        "key": key,
        "instance": instance,
        "nav_items": NAV_ITEMS,
        "active_key": key,
        "sheet_code": NAV_CODES.get(key, ""),
    }
    return render(request, "panel/resource_delete.html", context)


@login_required(login_url="panel:login")
def contact_edit(request):
    instance = Contact.objects.first()
    form = ContactForm(request.POST or None, instance=instance)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Contact details updated.")
        return redirect("panel:contact_edit")

    context = {
        "form": form,
        "nav_items": NAV_ITEMS,
        "active_key": "contact",
        "sheet_code": NAV_CODES["contact"],
    }
    return render(request, "panel/contact_form.html", context)
