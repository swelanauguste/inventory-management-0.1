from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from .forms import ComputerAssignmentCreateForm, ComputerUnAssignmentCreateForm
from .models import (
    Assignment,
    Category,
    Computer,
    ComputerAssignment,
    ComputerModel,
    Employee,
    GiveItem,
    Item,
    Manufacturer,
    Printer,
    PrinterAssignment,
    PrinterModel,
    ReceiveItem,
    Scanner,
    ScannerAssignment,
    ScannerModel,
    Supplier,
)


class PrinterListView(LoginRequiredMixin, ListView):
    model = Printer


class PrinterCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Printer
    fields = "__all__"
    success_url = reverse_lazy("printer-list")
    success_message = "%(name)s was created successfully"


class PrinterUpdateView(SuccessMessageMixin, UpdateView):
    model = Printer
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class PrinterDetailView(LoginRequiredMixin, DetailView):
    model = Printer


class ReceiveItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ReceiveItem
    fields = ["item", "qty"]
    success_url = reverse_lazy("item-list")
    success_message = "%(qty)s %(item)s(s) were added"

    def get_initial(self):
        return {"item": self.kwargs["pk"]}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class GiveItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = GiveItem
    fields = ["item", "qty"]
    success_url = reverse_lazy("item-list")
    success_message = "%(qty)s %(item)s(s) were removed"

    def get_initial(self):
        return {"item": self.kwargs["pk"]}

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class ComputerAssignmentListView(LoginRequiredMixin, ListView):
    model = ComputerAssignment


class ComputerAssignmentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ComputerAssignment
    form_class = ComputerAssignmentCreateForm
    success_url = reverse_lazy("computer-list")
    success_message = "%(computer)s was assigned to %(employee)s successfully"

    def get_initial(self):
        return {"computer": self.kwargs["pk"]}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["computer_name"] = Computer.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        self.object = form.save()
        computer_pk = self.object.computer.id
        form.instance.computer = Computer.objects.get(pk=computer_pk)
        return super().form_valid(form)


class ComputerUnAssignmentCreateView(
    LoginRequiredMixin, SuccessMessageMixin, CreateView
):
    model = ComputerAssignment
    form_class = ComputerUnAssignmentCreateForm
    success_url = reverse_lazy("computer-list")
    success_message = "%(computer)s was unassigned"

    def get_initial(self):
        return {
            "computer": self.kwargs["pk"],
            "employee": "",
            "date_returned": now,
        }

    def form_valid(self, form):
        self.object = form.save()
        computer_pk = self.object.computer.id
        form.instance.computer = Computer.objects.get(pk=computer_pk)
        return super().form_valid(form)


class ComputerAssignmentDetailView(LoginRequiredMixin, DetailView):
    model = ComputerAssignment


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee


class EmployeeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Employee
    fields = "__all__"
    success_url = reverse_lazy("employee-list")
    success_message = "%(name)s was created successfully"


class EmployeeUpdateView(SuccessMessageMixin, UpdateView):
    model = Employee
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee


class ManufacturerListView(LoginRequiredMixin, ListView):
    model = Manufacturer


class ManufacturerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Manufacturer
    fields = "__all__"
    success_url = reverse_lazy("manufacturer-list")
    success_message = "%(name)s was created successfully"


class ManufacturerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Manufacturer
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class ManufacturerDetailView(LoginRequiredMixin, DetailView):
    model = Manufacturer


class ComputerModelListView(LoginRequiredMixin, ListView):
    model = ComputerModel


class ComputerModelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = ComputerModel
    fields = "__all__"
    success_url = reverse_lazy("computer-model-list")
    success_message = "%(name)s was created successfully"


class ComputerModelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ComputerModel
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class ComputerModelDetailView(LoginRequiredMixin, DetailView):
    model = ComputerModel


class PrinterModelListView(LoginRequiredMixin, ListView):
    model = PrinterModel


class PrinterModelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = PrinterModel
    fields = "__all__"
    success_url = reverse_lazy("printer-model-list")
    success_message = "%(name)s was created successfully"


class PrinterModelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = PrinterModel
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class PrinterModelDetailView(LoginRequiredMixin, DetailView):
    model = PrinterModel


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category


class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("category-list")
    success_message = "%(name)s was created successfully"


class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class CategoryDetailView(LoginRequiredMixin, DetailView):
    model = Category


class ComputerListView(LoginRequiredMixin, ListView):
    model = Computer

    def get_queryset(self):
        query = self.request.GET.get("computers")
        if query:
            return Computer.objects.filter(
                Q(serial_number__icontains=query)
                | Q(model__name__icontains=query)
                | Q(model__manufacturer__name__icontains=query)
                | Q(supplier__name__icontains=query)
            ).distinct()
        else:
            return Computer.objects.all()


class ComputerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Computer
    fields = "__all__"
    success_url = reverse_lazy("computer-list")
    success_message = "%(serial_number)s was created successfully"


class ComputerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Computer
    fields = "__all__"
    success_message = "%(serial_number)s was updated successfully"


class ComputerDetailView(LoginRequiredMixin, DetailView):
    model = Computer


class ItemListView(LoginRequiredMixin, ListView):
    model = Item

    def get_queryset(self):
        query = self.request.GET.get("items")
        if query:
            return Item.objects.filter(
                Q(name__icontains=query)
                | Q(category__name__icontains=query)
                | Q(supplier__name__icontains=query)
            ).distinct()
        else:
            return Item.objects.all()


class ItemCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Item
    fields = "__all__"
    success_url = reverse_lazy("item-list")
    success_message = "%(name)s was created successfully"


class ItemUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Item
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item


class SupplierListView(LoginRequiredMixin, ListView):
    model = Supplier

    def get_queryset(self):
        query = self.request.GET.get("suppliers")
        if query:
            return Supplier.objects.filter(
                Q(name__icontains=query)
                | Q(address__icontains=query)
                | Q(phone__icontains=query)
                | Q(email__icontains=query)
            ).distinct()
        else:
            return Supplier.objects.all()


class SupplierCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Supplier
    fields = "__all__"
    success_url = reverse_lazy("supplier-list")
    success_message = "%(name)s was created successfully"


class SupplierUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Supplier
    fields = "__all__"
    success_message = "%(name)s was updated successfully"


class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Supplier


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home.html"
