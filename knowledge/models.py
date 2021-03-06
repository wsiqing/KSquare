from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_delete
import knowledge
# Create your models here.


class Concept(models.Model):
    id = models.AutoField(primary_key=True)
    _title = models.CharField(max_length=30)
    content = models.TextField()
    click_number = models.IntegerField(default=0, null=False)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value.strip(" ")


class Relation(models.Model):
    id = models.AutoField(primary_key=True)
    _title = models.CharField(max_length=30)
    content = models.TextField()
    color = models.CharField(max_length=10, null=True)
    is_sym = models.BooleanField
    # To is Forth's ...
    t_is_f = models.CharField(max_length=30, null=True)
    # Forth is To's ...
    f_is_t = models.CharField(max_length=30, null=True)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value.strip(" ")


class ToLink(models.Model):
    id = models.AutoField(primary_key=True)
    relation_main = models.ForeignKey(Relation, on_delete=models.CASCADE, null=True)
    related_concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='to_link', null=True)


class ForthLink(models.Model):
    id = models.AutoField(primary_key=True)
    relation_main = models.ForeignKey(Relation, on_delete=models.CASCADE, null=True)
    related_concept = models.ForeignKey(Concept, on_delete=models.CASCADE, related_name='forth_link', null=True)
    to_link_partner = models.OneToOneField(ToLink, on_delete=models.CASCADE, related_name='forth_link_partner'
                                           , null=True)


# To and Forth are linked. One deleted also another.
@receiver(post_delete, sender=ForthLink)
def post_delete_to_link(sender, instance, *args, **kwargs):
    try:
        instance.to_link_partner
    except knowledge.models.ToLink.DoesNotExist:
        return
    if instance.to_link_partner:  # just in case user is not specified
        instance.to_link_partner.delete()


# @receiver(post_delete, sender=ToRelationEntry)
# def post_delete_forth_relation_entry(sender, instance, *args, **kwargs):
#     if instance.forth_relation_partner:  # just in case user is not specified
#         instance.forth_relation_partner.delete()


def get_or_create_by_title(cls, title_in=""):
    title_in = title_in.strip(" ")
    try:
        ob = cls.objects.get(_title=title_in)
    except cls.DoesNotExist:
        ob = cls.objects.create(_title=title_in)
    return ob











