from django.db import models

# Create your models here.


class Board(models.Model):
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    board_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'board'
