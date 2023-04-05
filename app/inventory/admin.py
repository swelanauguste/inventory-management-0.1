from django.contrib import admin

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

# admin.site.register(Supplier)
admin.site.register(Category)
# admin.site.register(Item)
admin.site.register(Employee)
admin.site.register(Assignment)
# admin.site.register(Computer)
# admin.site.register(ComputerAssignment)
admin.site.register(ComputerModel)
admin.site.register(Printer)
admin.site.register(PrinterAssignment)
admin.site.register(PrinterModel)
admin.site.register(Scanner)
admin.site.register(ScannerAssignment)
admin.site.register(ScannerModel)
admin.site.register(Manufacturer)
admin.site.register(ReceiveItem)
admin.site.register(GiveItem)


@admin.register(ComputerAssignment)
class ComputerAssignmentAdmin(admin.ModelAdmin):
    list_display = ["computer", "employee", "date_assigned", "date_returned"]


@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ["serial_number", "model", "supplier"]


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "phone", "email"]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "supplier", "price", "get_item_total_count", 'get_total_cost']
