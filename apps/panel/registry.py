from apps.categories.models import Category
from apps.projects.models import Project
from apps.services.models import Service
from apps.home.models import Home
from apps.reviews.models import Review
from apps.practice.models import Practice
from apps.stats.models import Stat
from apps.process.models import Process
from apps.contact.models import Lead
from apps.equipment.models import Equipment

from .forms import (
    CategoryForm,
    ProjectForm,
    ServiceForm,
    HomeForm,
    ReviewForm,
    PracticeForm,
    StatForm,
    ProcessForm,
    LeadForm,
    EquipmentForm,
)


RESOURCES = {
    "categories": {
        "model": Category,
        "form": CategoryForm,
        "label": "Categories",
        "singular": "Category",
        "list_fields": ["id", "name", "order"],
        "order_by": "order",
        "search_fields": ["name"],
    },
    "projects": {
        "model": Project,
        "form": ProjectForm,
        "label": "Projects",
        "singular": "Project",
        "list_fields": ["id", "name", "category", "year", "location", "order"],
        "image_field": "image",
        "order_by": "order",
        "search_fields": ["name", "location", "description"],
    },
    "services": {
        "model": Service,
        "form": ServiceForm,
        "label": "Services",
        "singular": "Service",
        "list_fields": ["id", "name", "order"],
        "order_by": "order",
        "search_fields": ["name", "description"],
    },
    "home": {
        "model": Home,
        "form": HomeForm,
        "label": "Home Images",
        "singular": "Home Image",
        "list_fields": ["id", "created_at", "order"],
        "image_field": "image",
        "order_by": "order",
        "search_fields": [],
    },
    "reviews": {
        "model": Review,
        "form": ReviewForm,
        "label": "Reviews",
        "singular": "Review",
        "list_fields": ["id", "name", "type", "created_at", "order"],
        "image_field": "photo",
        "order_by": "order",
        "search_fields": ["name", "description"],
    },
    "practice": {
        "model": Practice,
        "form": PracticeForm,
        "label": "Practice",
        "singular": "Practice",
        "list_fields": ["id", "title", "order"],
        "image_field": "image",
        "order_by": "order",
        "search_fields": ["title", "description"],
    },
    "stats": {
        "model": Stat,
        "form": StatForm,
        "label": "Stats",
        "singular": "Stat",
        "list_fields": ["id", "value", "label", "order"],
        "order_by": "order",
        "search_fields": ["value", "label"],
    },
    "process": {
        "model": Process,
        "form": ProcessForm,
        "label": "Process",
        "singular": "Process Step",
        "list_fields": ["id", "step", "title"],
        "order_by": "step",
        "search_fields": ["title", "description"],
    },
    "leads": {
        "model": Lead,
        "form": LeadForm,
        "label": "Leads",
        "singular": "Lead",
        "list_fields": ["id", "name", "email", "phone", "created_at"],
        "order_by": "-created_at",
        "search_fields": ["name", "email", "phone"],
    },
    "equipment": {
        "model": Equipment,
        "form": EquipmentForm,
        "label": "Equipment",
        "singular": "Equipment",
        "list_fields": ["id", "name", "unit", "quantity", "order"],
        "image_field": "image",
        "order_by": "order",
        "search_fields": ["name", "unit"],
    },
}


# Lucide icon inner-markup (https://lucide.dev, ISC license) — wrapped in an
# <svg> shell by the nav template. Kept inline so the console has no runtime
# icon-font/JS dependency.
ICONS = {
    "dashboard": '<rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/>',
    "projects": '<path d="M6 22V4a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v18Z"/><path d="M6 12H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h2"/><path d="M18 9h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2h-2"/><path d="M10 6h4"/><path d="M10 10h4"/><path d="M10 14h4"/><path d="M10 18h4"/>',
    "categories": '<path d="M12.586 2.586A2 2 0 0 0 11.172 2H4a2 2 0 0 0-2 2v7.172a2 2 0 0 0 .586 1.414l8.704 8.704a2.426 2.426 0 0 0 3.42 0l6.58-6.58a2.426 2.426 0 0 0 0-3.42z"/><circle cx="7.5" cy="7.5" r=".5" fill="currentColor"/>',
    "home": '<rect width="18" height="18" x="3" y="3" rx="2" ry="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.086-3.086a2 2 0 0 0-2.828 0L6 21"/>',
    "reviews": '<path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"/>',
    "practice": '<path d="m15 12-8.5 8.5a2.12 2.12 0 1 1-3-3L12 9"/><path d="M17.64 15 22 10.64"/><path d="m20.91 11.7-1.25-1.25c-.6-.6-.93-1.4-.93-2.25v-.86L16.01 4.6a5.56 5.56 0 0 0-3.94-1.64H9l.92.82A6.18 6.18 0 0 1 12 8.4v1.56l2 2h2.47l2.26 1.91"/>',
    "services": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94z"/>',
    "process": '<path d="M10 6h11"/><path d="M10 12h11"/><path d="M10 18h11"/><path d="M4 6h1v4"/><path d="M4 10h2"/><path d="M6 18H4c0-1 2-2 2-3s-1-1.5-2-1"/>',
    "equipment": '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94z"/>',
    "stats": '<line x1="18" x2="18" y1="20" y2="10"/><line x1="12" x2="12" y1="20" y2="4"/><line x1="6" x2="6" y1="20" y2="14"/>',
    "contact": '<path d="M13.832 16.568a1 1 0 0 0 1.213-.303l.355-.465A2 2 0 0 1 17 15h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2A18 18 0 0 1 2 4a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v3a2 2 0 0 1-.883 1.605l-.465.336a1 1 0 0 0-.31 1.22 12.035 12.035 0 0 0 6.99 6.98"/>',
    "leads": '<path d="M22 12h-6l-2 3h-4l-2-3H2"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/>',
}

NAV_ITEMS = [
    {"key": "dashboard", "label": "Overview", "url_name": "panel:dashboard", "code": "A-01", "icon": ICONS["dashboard"]},
    {"key": "projects", "label": "Projects", "url_name": "panel:resource_list", "code": "A-02", "icon": ICONS["projects"]},
    {"key": "categories", "label": "Categories", "url_name": "panel:resource_list", "code": "A-03", "icon": ICONS["categories"]},
    {"key": "home", "label": "Home Images", "url_name": "panel:resource_list", "code": "A-04", "icon": ICONS["home"]},
    {"key": "reviews", "label": "Reviews", "url_name": "panel:resource_list", "code": "A-05", "icon": ICONS["reviews"]},
    {"key": "practice", "label": "Practice", "url_name": "panel:resource_list", "code": "A-06", "icon": ICONS["practice"]},
    {"key": "services", "label": "Services", "url_name": "panel:resource_list", "code": "A-07", "icon": ICONS["services"]},
    {"key": "equipment", "label": "Equipment", "url_name": "panel:resource_list", "code": "A-08", "icon": ICONS["equipment"]},
    {"key": "process", "label": "Process", "url_name": "panel:resource_list", "code": "A-09", "icon": ICONS["process"]},
    {"key": "stats", "label": "Stats", "url_name": "panel:resource_list", "code": "A-10", "icon": ICONS["stats"]},
    {"key": "leads", "label": "Leads", "url_name": "panel:resource_list", "code": "A-11", "icon": ICONS["leads"]},
    {"key": "contact", "label": "Contact", "url_name": "panel:contact_edit", "code": "A-12", "icon": ICONS["contact"]},
]

NAV_CODES = {item["key"]: item["code"] for item in NAV_ITEMS}
