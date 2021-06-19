from django.db import models

GRADE=(
        ("秀","秀"),
        ("優","優"),
        ("良","良"),
        ("可","可"),
        ("不","不"),
    )
BROOD_GROUP=(
        ("A","A"),
        ("B","B"),
        ("O","O"),
        ("AB","AB"),
    )

class School(models.Model):
    name = models.CharField(max_length=100,verbose_name="スクール名")
    email = models.EmailField(null=True, blank=True, verbose_name="メールアドレス")
    address = models.TextField(verbose_name="住所")

    class Meta:
        verbose_name ="スクールデータ"
        verbose_name_plural ="スクールデータ"

    def __str__(self):
        return self.name
        

class Student(models.Model):
    name = models.CharField(max_length=100,verbose_name="氏名")
    grade = models.CharField(verbose_name="成績", max_length=5, choices=GRADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE, verbose_name="スクール名")
    blood_group = models.CharField(max_length=10,verbose_name="血液型", choices=BROOD_GROUP)
    mobile = models.CharField(max_length=20)
    address = models.TextField(verbose_name="住所")

    class Meta:
        verbose_name ="学生データ"
        verbose_name_plural ="学生データ"

    def __str__(self):
        return self.name

