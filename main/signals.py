from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import OrderModel, HistoryOrderModel


@receiver(post_save, sender=OrderModel)
def order_signal(sender, instance, created, **kwargs):
    if created:  # Only create history entry for newly created orders
        history_order = HistoryOrderModel.objects.create(
            user=instance.user,
            created_at=instance.created_at,
            # Copy product information
        )
        history_order.product.add(*instance.product.all())  # Copy products from order to history
        history_order.save()
