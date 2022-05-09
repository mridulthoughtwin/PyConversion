from django.db import models

# Create Models here.

CONVERT_CHOICES = (
    ("usd", "USD"),
    ("euro", "EURO"),
    ("Astrln","ASTRLN"),
    ("Brtsh","BRTSH"),
    ("Cndn", "CNDN"),
    ("SingaporeDollar", "SNGPR"),
    ("SwissFranc", "SWSFRNC"),
    ("MalaysianRinggit","MLYSN"),
    ("JapaneseYen","JPNS"),
    ("ChineseYuanRenminbi","CHNS"),
    ("IndianRupee","INR"),
) 

CURRENT_CHOICES = (
  ("IndianRupee","INR"),
  ("usd","USD"),
  ("euro","EURO"),
  ("British Pound","BRIPOU"),
  ("Australian Dollar","AUSDOL"),
  ("Canadian Dollar","CANDOL"),
  ("Swiss Franc","SWIFc"),
  ("Singapore Dollar","SINGDOL")
)


class Currency_convert_model(models.Model):
  current_choice = models.CharField(max_length = 20 , choices= CURRENT_CHOICES)
  amount = models.IntegerField()
  convert_choice = models.CharField(max_length = 20 , choices= CONVERT_CHOICES)
  