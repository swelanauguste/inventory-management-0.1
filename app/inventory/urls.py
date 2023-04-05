from django.urls import path

from .views import (
    CategoryCreateView,
    CategoryDetailView,
    CategoryListView,
    CategoryUpdateView,
    ComputerAssignmentCreateView,
    ComputerAssignmentDetailView,
    ComputerAssignmentListView,
    ComputerUnAssignmentCreateView,
    ComputerCreateView,
    ComputerDetailView,
    ComputerListView,
    ComputerModelCreateView,
    ComputerModelDetailView,
    ComputerModelListView,
    ComputerModelUpdateView,
    ComputerUpdateView,
    EmployeeCreateView,
    EmployeeDetailView,
    EmployeeListView,
    EmployeeUpdateView,
    GiveItemCreateView,
    HomeView,
    ItemCreateView,
    ItemDetailView,
    ItemListView,
    ItemUpdateView,
    ManufacturerCreateView,
    ManufacturerDetailView,
    ManufacturerListView,
    ManufacturerUpdateView,
    ReceiveItemCreateView,
    SupplierCreateView,
    SupplierDetailView,
    SupplierListView,
    SupplierUpdateView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("items/", ItemListView.as_view(), name="item-list"),
    path("item/create/", ItemCreateView.as_view(), name="item-create"),
    path("item/update/<int:pk>/", ItemUpdateView.as_view(), name="item-update"),
    path("item/detail/<int:pk>/", ItemDetailView.as_view(), name="item-detail"),
    path("suppliers/", SupplierListView.as_view(), name="supplier-list"),
    path("supplier/create/", SupplierCreateView.as_view(), name="supplier-create"),
    path(
        "supplier/update/<int:pk>/",
        SupplierUpdateView.as_view(),
        name="supplier-update",
    ),
    path(
        "supplier/detail/<int:pk>/",
        SupplierDetailView.as_view(),
        name="supplier-detail",
    ),
    path("computers/", ComputerListView.as_view(), name="computer-list"),
    path("computer/create/", ComputerCreateView.as_view(), name="computer-create"),
    path(
        "computer/update/<int:pk>/",
        ComputerUpdateView.as_view(),
        name="computer-update",
    ),
    path(
        "computer/detail/<int:pk>/",
        ComputerDetailView.as_view(),
        name="computer-detail",
    ),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("category/create/", CategoryCreateView.as_view(), name="category-create"),
    path(
        "category/update/<int:pk>/",
        CategoryUpdateView.as_view(),
        name="category-update",
    ),
    path(
        "category/detail/<int:pk>/",
        CategoryDetailView.as_view(),
        name="category-detail",
    ),
    path(
        "computer-models/", ComputerModelListView.as_view(), name="computer-model-list"
    ),
    path(
        "computer-model/create/",
        ComputerModelCreateView.as_view(),
        name="computer-model-create",
    ),
    path(
        "computer-model/update/<int:pk>/",
        ComputerModelUpdateView.as_view(),
        name="computer-model-update",
    ),
    path(
        "computer-model/detail/<int:pk>/",
        ComputerModelDetailView.as_view(),
        name="computer-model-detail",
    ),
    path("manufacturers/", ManufacturerListView.as_view(), name="manufacturer-list"),
    path(
        "manufacturer/create/",
        ManufacturerCreateView.as_view(),
        name="manufacturer-create",
    ),
    path(
        "manufacturer/update/<int:pk>/",
        ManufacturerUpdateView.as_view(),
        name="manufacturer-update",
    ),
    path(
        "manufacturer/detail/<int:pk>/",
        ManufacturerDetailView.as_view(),
        name="manufacturer-detail",
    ),
    path("employees/", EmployeeListView.as_view(), name="employee-list"),
    path(
        "employee/create/",
        EmployeeCreateView.as_view(),
        name="employee-create",
    ),
    path(
        "employee/update/<int:pk>/",
        EmployeeUpdateView.as_view(),
        name="employee-update",
    ),
    path(
        "employee/detail/<int:pk>/",
        EmployeeDetailView.as_view(),
        name="employee-detail",
    ),
    path(
        "computer-assignments/",
        ComputerAssignmentListView.as_view(),
        name="computer-assignment-list",
    ),
    path(
        "computer-assignment/create/<int:pk>/",
        ComputerAssignmentCreateView.as_view(),
        name="computer-assignment-create",
    ),
    path(
        "computer-assignment/update/<int:pk>/",
        ComputerUnAssignmentCreateView.as_view(),
        name="computer-unassignment-create",
    ),
    path(
        "computer-assignment/detail/<int:pk>/",
        ComputerAssignmentDetailView.as_view(),
        name="computer-assignment-detail",
    ),
    path(
        "item-give/create/<int:pk>/",
        GiveItemCreateView.as_view(),
        name="item-give-create",
    ),
    path(
        "item-receive/create/<int:pk>/",
        ReceiveItemCreateView.as_view(),
        name="item-receive-create",
    ),
]
