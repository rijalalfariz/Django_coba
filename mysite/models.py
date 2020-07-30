from django.db import models

class PegawaiReg(models.Model):
    nip = models.CharField(max_length = 100)
    nama = models.CharField(max_length = 100)
    kantor = models.CharField(max_length = 100)
    pwd = models.CharField(max_length = 100)
    foto = models.CharField(max_length = 100)
    class Meta:
        db_table = "karyawan"
        
