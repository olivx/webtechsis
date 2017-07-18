from django.db import models


class ClienteQuerySet(models.QuerySet):
    db = 'techcd'


class ClienteManager(models.Manager):
    def get_queryset(self):
        return ClienteQuerySet(self.model, using=self._db)


class TechUserQuerySet(models.QuerySet):
    db = 'techcd'


class TechUserManager(models.Manager):
    def get_queryset(self):
        return TechUserQuerySet(self.model, using=self._db)


class GrupoUsuarioQuerySet(models.QuerySet):
    db = 'techcd'


class GrupoUsuarioManager(models.Manager):
    def get_queryset(self):
        return GrupoUsuarioQuerySet(self.model, using=self._db)


class ProdutoTechQuerySet(models.QuerySet):
    db = 'techcd'


class ProdutoTechManager(models.Manager):
    def get_queryset(self):
        return ProdutoTechQuerySet(self.model, using=self._db)


class CategoriaProdutosTechQuerySet(models.QuerySet):
    db = 'techcd'


class CategoriaProdutoTechManager(models.Manager):
    def get_queryset(self):
        return ProdutoTechQuerySet(self.model, using=self._db)
