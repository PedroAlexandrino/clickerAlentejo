from django.db import models

# Create your models here.

class Contador(models.Model):
    contador = models.CharField(max_length=100,blank="true", null="true")
    data = models.CharField(max_length=100,blank="true", null="true")
    turno = models.CharField(max_length=10,blank="true", null="true")


    # TO STRING METHOD
    def __str__(self):
        return f"{self.contador} -> {self.data}"
    
    def to_dict(self):
        return {
            "contador": self.contador,
            "data": self.data,
            "turno": self.turno,
        }
    
class Contador_View(models.Model):
    contador = models.CharField(max_length=250,blank="true", null="true")
    data = models.CharField(max_length=100,blank="true", null="true")
    turno = models.CharField(max_length=10,blank="true", null="true")

   

    def __str__(self):
        return self.contador
    
    def to_dict(self):
            return {
                "id": self.id,
                "contador": self.contador,
                "data": self.data,
                "turno": self.turno,
            }
    class Meta:
        managed = False
        db_table ="clicker_contador_view"

class P1(models.Model):
    p1_inicio = models.CharField(max_length=10,blank="true", null="true")
    p1_fim = models.CharField(max_length=10,blank="true", null="true")

    def __str__(self):
        return self.p1
    
    def to_dict(self):
        return {
            "p1_inicio": self.p1_inicio,
            "p1_fim": self.p1_fim,
        }

class P2(models.Model):
    p2_inicio = models.CharField(max_length=10,blank="true", null="true")
    p2_fim = models.CharField(max_length=10,blank="true", null="true")

    def __str__(self):
            return self.p2
    
    def to_dict(self):
        return {
            "p2_inicio": self.p2_inicio,
            "p2_fim": self.p2_fim,
        }

class P3(models.Model):
    p3_inicio = models.CharField(max_length=10,blank="true", null="true")
    p3_fim = models.CharField(max_length=10,blank="true", null="true")

    def __str__(self):
        return self.p3
    def to_dict(self):
        return {
            "p3_inicio": self.p3_inicio,
            "p3_fim": self.p3_fim,
        }

class Pergunta(models.Model):
    pergunta = models.CharField(max_length=250,blank="true", null="true")
    data = models.CharField(max_length=100,blank="true", null="true")

    def __str__(self):
        return self.pergunta
    
    def to_dict(self):
            return {
                "pergunta": self.pergunta,
                "data": self.data,
            }
    

class Compras(models.Model):
    nPessoa = models.CharField(max_length=250,blank="true", null="true")
    descricao = models.CharField(max_length=100,blank="true", null="true")
    total = models.CharField(max_length=10,blank="true", null="true")
    data = models.CharField(max_length=100,blank="true", null="true")

    def __str__(self):
        return self.nPessoa
    
    def to_dict(self):
            return {
                "id": self.id,
                "nPessoa": self.nPessoa,
                "descricao": self.descricao,
                "total": self.total,
                "data": self.data,
            }
    

class Compras_View(models.Model):
    nPessoa = models.CharField(max_length=250,blank="true", null="true")
    descricao = models.CharField(max_length=100,blank="true", null="true")
    total = models.CharField(max_length=10,blank="true", null="true")
    data = models.CharField(max_length=100,blank="true", null="true")

    def __str__(self):
        return self.nPessoa
    
    def to_dict(self):
            return {
                "id": self.id,
                "nPessoa": self.nPessoa,
                "descricao": self.descricao,
                "total": self.total,
                "data": self.data,
            }
    class Meta:
        managed = False
        db_table ="clicker_compras_view"


""" class Tracking_ShippersPage_Sub_Items(models.Model):
    abs_id = models.CharField(max_length=200, null=True)
    abs_status  = models.CharField(max_length=200, null=True)
    abs_shipfrom = models.CharField(max_length=200, null=True)
    abs_item = models.CharField(max_length=200, null=True)
    abs_qty = models.CharField(max_length=200, null=True)
    abs_ship_qty = models.CharField(max_length=200, null=True)

    
    # TO STRING METHOD
    def __str__(self):
        return f"{self.dataHoraChegada}"
    
    def to_dict(self):
        return {
            "abs_id": self.abs_id,
            "abs_status": self.abs_status,
            "abs_shipfrom": self.abs_shipfrom,
            "abs_item": self.abs_item,
            "abs_qty": self.abs_qty,
            "abs_ship_qty": self.abs_ship_qty,
        } """