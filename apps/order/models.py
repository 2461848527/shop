from django.db import models
from db.base_model import BaseModel
from tinymce.models import HTMLField
# Create your models here.
'''
pid = models.ForeignKey('self',on_delete=models.SET_NULL,related_name='addinfo',null=True,blank=True,verbose_name='上一级别的行政区域id')
CASCADE：级联操作。如果外键对应的那条数据被删除了，那么这条数据也会被删除。
PROTECT：受保护。即只要这条数据引用了外键的那条数据，那么就不能删除外键的那条数据。
SET_NULL：设置为空。如果外键的那条数据被删除了，那么在本条数据上就将这个字段设置为空。如果设置这个选项，前提是要指定这个字段可以为空。
例如：把on_delete的值设置成models.SET_NULL
SET_DEFAULT：设置默认值。如果外键的那条数据被删除了，那么本条数据上就将这个字段设置为默认值。如果设置这个选项，前提是要指定这个字段一个默认值。
SET()：如果外键的那条数据被删除了。那么将会获取SET函数中的值来作为这个外键的值。SET函数可以接收一个可以调用的对象（比如函数或者方法），如果是可以调用的对象，那么会将这个对象调用后的结果作为值返回回去。
DO_NOTHING：不采取任何行为。一切全看数据库级别的约束。
'''

class OrderInfo(BaseModel):
    '''订单模型类'''
    PAY_METHOD_CHOICES = (
        (1, '货到付款'),
        (2, '微信支付'),
        (3, '支付宝'),
    )

    ORDER_STATUS_CHOICES = (
        (1, '待支付'),
        (2, '待联系'),
        (3, '待设计'),
        (4, '待验货'),
        (5, '待余款'),
        (6, '待评价'),
        (7, '已完成')
    )

    # DESIGN_CYCLE_CHOICES = (
    #     (1,'半个月'),
    #     (2,'一个月'),
    #     (3,'两个月'),
    #     (4,'其他'),
    # )
    '''
    DecimalField
    类DecimalField（max_digits =无，decimal_places =无[，**选项]）
    固定精度的十进制数，在Python中表示一个 十进制的实例。有两个必需的参数：
    
    DecimalField max_digits 
    数中允许的最大数目的数字。请注意此数字必须是大于decimal_places的，如果存在的话。
    
    DecimalField decimal_places 
    存储的小数位数的数字。
    '''
    order_id = models.CharField(max_length=128, primary_key=True, verbose_name='订单id')
    user = models.ForeignKey('user.User', on_delete=models.DO_NOTHING, verbose_name='用户')
    store_platform = models.CharField(max_length=50,verbose_name='店铺平台')
    store_style = models.CharField(max_length=50,verbose_name='店铺风格')
    pay_method = models.SmallIntegerField(choices=PAY_METHOD_CHOICES, default=3, verbose_name='支付方式')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='订单总价')
    Deposit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='订金金额')
    Balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='尾款金额')
    order_status = models.SmallIntegerField(choices=ORDER_STATUS_CHOICES, default=1, verbose_name='订单状态')
    design_cycle = models.CharField(max_length=20,verbose_name='订单周期')
    design_requirement = HTMLField(verbose_name='设计要求')
    trade_no = models.CharField(max_length=128, verbose_name='支付编号')
    Store_account = models.CharField(max_length=20, verbose_name='用户店铺账号')
    Store_password = models.CharField(max_length=20, verbose_name='用户店铺密码')
    comment = models.CharField(max_length=256, verbose_name='订单评论')

    class Meta:
        db_table = 'dz_order_info'



class ContactInformations(BaseModel):
    '''我方联系方式模型类'''
    # id
    contact_id = models.CharField(max_length=128, primary_key=True, verbose_name='联系方式id')
    # 联系人
    contact_name = models.CharField(max_length=100, null=True, verbose_name='联系人姓名')
    # 微信号
    wechat = models.CharField(max_length=20, null=True, verbose_name='联系人微信号')
    # QQ号
    qq = models.CharField(max_length=11, null=True, verbose_name='联系人qq')
    # 手机号
    telephone = models.CharField(max_length=11, unique=True, verbose_name='联系人手机号')
    # 备用手机号
    spare_telephone = models.CharField(max_length=11, null=True, verbose_name='联系人备用手机号')
    # 保留邮箱，以免以后有开发需要
    email = models.EmailField(unique=True, null=True, verbose_name='联系人邮箱')

    class Meta:
        db_table = 'dz_contact_informations'

