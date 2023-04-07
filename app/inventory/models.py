from decimal import Decimal

from django.conf import settings
from django.db import models
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=200, null=True)
    address1 = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)

    def get_absolute_url(self):
        return reverse("supplier-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse("category-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, null=True, blank=True
    )
    quantity = models.IntegerField(default=1, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)

    def get_total_cost(self):
        return self.price * self.get_item_total_count()

    def get_all_received_count(self):
        return sum(item.qty for item in self.receive_items.all())

    def get_all_given_count(self):
        return sum(item.qty for item in self.give_items.all())

    def get_item_total_count(self):
        return (
            self.get_all_received_count() + self.quantity
        ) - self.get_all_given_count()

    def get_absolute_url(self):
        return reverse("item-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class ReceiveItem(models.Model):
    item = models.ForeignKey(
        Item, on_delete=models.CASCADE, related_name="receive_items"
    )
    qty = models.PositiveIntegerField("quantity")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return f"{self.item} ({self.qty})"


class GiveItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="give_items")
    qty = models.PositiveIntegerField("quantity")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="+")

    def __str__(self):
        return f"{self.item} ({self.qty})"


class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255)
    dept = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="department",
    )
    ext = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        ordering = ("name",)

    def get_absolute_url(self):
        return reverse("employee-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Assignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, blank=True)
    date_assigned = models.DateField(auto_now_add=True)
    date_returned = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.item} assigned to {self.employee}"


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse("manufacturer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class ComputerModel(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, null=True, blank=True
    )
    processor = models.CharField(max_length=255, blank=True)
    memory = models.CharField(max_length=255, blank=True)
    storage = models.CharField(max_length=255, blank=True)

    def get_absolute_url(self):
        return reverse("computer-model-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f" {self.manufacturer} {self.name}"


# class PrintTechnology(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name


class PrinterModel(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, null=True, blank=True
    )
    # print_technology = models.ForeignKey(
    #     PrintTechnology, on_delete=models.CASCADE, null=True, blank=True
    # )
    colour_printer = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ScannerModel(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    scan_technology = models.CharField(max_length=255, blank=True)
    scan_resolution = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name


class Computer(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    model = models.ForeignKey(ComputerModel, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("computer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.serial_number} {self.model}"


class Printer(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    model = models.ForeignKey(PrinterModel, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("printer-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.serial_number} {self.model}"


class Scanner(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    model = models.ForeignKey(ScannerModel, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("scanner-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.serial_number} {self.model}"


class ComputerAssignment(models.Model):
    computer = models.ForeignKey(
        Computer, on_delete=models.CASCADE, related_name="computer_assignments"
    )
    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="computer_assignments",
    )
    date_assigned = models.DateField(auto_now_add=True, null=True)
    date_returned = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("computer-assignment-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.computer} assigned to {self.employee}"


class PrinterAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)
    date_assigned = models.DateField(auto_now_add=True)
    date_returned = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.printer} assigned to {self.employee}"


class ScannerAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    scanner = models.ForeignKey(Scanner, on_delete=models.CASCADE)
    date_assigned = models.DateField(auto_now_add=True)
    date_returned = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.scanner} assigned to {self.employee}"
