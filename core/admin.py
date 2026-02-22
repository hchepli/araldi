"""
Django admin customization.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name', 'passage_id')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            },
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
        (_('Groups'), {'fields': ('groups',)}),
        (_('User Permissions'), {'fields': ('user_permissions',)}),
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'name',
                    'is_active',
                    'is_staff',
                    'is_superuser',
                ),
            },
        ),
    )


admin.site.register(models.User, UserAdmin)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'display_order', 'active')
    list_filter = ('active',)
    search_fields = ('name', 'description')
    ordering = ('display_order', 'name')
    list_per_page = 10

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'category', 'active')
    list_filter = ('active', 'category')
    search_fields = ('name', 'description')
    ordering = ('name',)
    list_per_page = 10

@admin.register(models.ProductOptionGroup)
class ProductOptionGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', )
    list_filter = ('name',)
    search_fields = ('name', 'description')
    ordering = ('name',)
    list_per_page = 10

@admin.register(models.ProductOption)
class ProductOptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'option_group', 'active')
    list_filter = ('active', 'option_group')
    search_fields = ('name',)   
    ordering = ('name',)
    list_per_page = 10

@admin.register(models.ProductExtra)
class ProductExtraAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'active')
    list_filter = ('active',)
    search_fields = ('name',)
    ordering = ('name',)
    list_per_page = 10

@admin.register(models.OrderIntent)
class OrderIntentAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer_name', 'customer_phone',)
    ordering = ('-created_at',)
    list_per_page = 10

@admin.register(models.OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_intent', 'quantity',)
    list_filter = ('order_intent',)
    search_fields = ('order_intent__id', 'product__name')
    ordering = ('-id',)
    list_per_page = 10

@admin.register(models.OrderItemOption)
class OrderItemOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_item', 'additional_price')
    list_filter = ('order_item',)
    search_fields = ('order_item__id', 'product_option__name')
    ordering = ('-id',)
    list_per_page = 10

@admin.register(models.OrderItemExtra)
class OrderItemExtraAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_item',)
    list_filter = ('order_item',)
    search_fields = ('order_item__id', 'product_extra__name')
    ordering = ('-id',)
    list_per_page = 10

@admin.register(models.Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_start', 'date_end')
    list_filter = ('date_start', 'date_end',)
    search_fields = ('name', 'description')
    ordering = ('name',)
    list_per_page = 10

@admin.register(models.PromotionProduct)
class PromotionProductAdmin(admin.ModelAdmin):
    list_display = ('promotion',)
    list_filter = ('promotion',)
    search_fields = ('promotion__name', 'product__name')
    ordering = ('promotion__name', 'product__name')
    list_per_page = 10