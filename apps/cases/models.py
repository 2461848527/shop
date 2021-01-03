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


class CaseInfos(BaseModel):
    '''案例信息模型类'''
    '''
    DecimalField
    类DecimalField（max_digits =无，decimal_places =无[，**选项]）
    固定精度的十进制数，在Python中表示一个 十进制的实例。有两个必需的参数：

    DecimalField max_digits 
    数中允许的最大数目的数字。请注意此数字必须是大于decimal_places的，如果存在的话。

    DecimalField decimal_places 
    存储的小数位数的数字。
    '''
    case_id = models.CharField(max_length=128, primary_key=True, verbose_name='案例id')
    order = models.ForeignKey('order.OrderInfo',on_delete=models.DO_NOTHING,verbose_name='订单')
    store_platform = models.CharField(max_length=50, verbose_name='店铺平台')
    picture_url = models.URLField(verbose_name='案例图片')
    new_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='现价')
    delivery_place = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='发货地')
    payer_num = models.IntegerField(verbose_name='付款人数')
    design_cycle = models.CharField(max_length=100, verbose_name='商品名')

    class Meta:
        db_table = 'dz_case_info'


class CaseDetailInfos(BaseModel):
    '''案例详细模型类'''
    # id
    case_detail_id = models.CharField(max_length=128, primary_key=True, verbose_name='详情页id')
    # 案例id
    case = models.ForeignKey('CaseInfos', on_delete=models.DO_NOTHING, verbose_name='案例')
    # 商品原价
    old_place = models.DecimalField(max_digits=10,decimal_places=2,verbose_name='商品原价')
    # 月销量
    monthly_salary = models.IntegerField(verbose_name='月销量')
    # 评论数
    comment_num = models.IntegerField(verbose_name='评论数')
    # 品牌名
    brand_name = models.CharField(max_length=16,verbose_name='品牌名')
    # 商品种类
    good_type = models.CharField(max_length=30,verbose_name='商品种类')
    # 商品口味
    good_flavor = models.CharField(max_length=300,verbose_name='商品口味')
    # 产地
    origin_place = models.CharField(max_length=30,verbose_name='产地')
    # 厂名
    factory_name = models.CharField(max_length=30,verbose_name='厂名')
    class Meta:
        db_table = 'dz_case_detail_infos'

class StoreInfo(BaseModel):
    '''案例店铺信息模型类'''
    store_id = models.CharField(max_length=128, primary_key=True, verbose_name='详情页id')
    store_name = models.CharField(max_length=100,verbose_name='店铺名称')
    case = models.ForeignKey('CaseInfos', on_delete=models.DO_NOTHING, verbose_name='案例')
    class Meta:
        db_table = 'dz_store_info'

class CaseComments(BaseModel):
    '''案例评论模型类'''
    comment_id = models.CharField(max_length=128,primary_key=True,verbose_name='案例评论id')
    case = models.ForeignKey('CaseInfos', on_delete=models.DO_NOTHING, verbose_name='案例')
    comment_people = models.CharField(max_length=20,verbose_name='评论人')
    comment_content = HTMLField(verbose_name='评论')
    class Meta:
        db_table = 'dz_case_comment'

class CaseAttribute(BaseModel):
    '''案例属性模型类'''
    attribute_id = models.CharField(max_length=128,primary_key=True,verbose_name='案例属性id')
    case = models.ForeignKey('CaseInfos',on_delete=models.DO_NOTHING,verbose_name='案例')
    is_free_postage = models.BooleanField(default=False, verbose_name='是否包邮')
    is_fast_refund = models.BooleanField(default=False, verbose_name='是否急速退款')
    is_jd_self_manage = models.BooleanField(default=False, verbose_name='是否京东自营')
    is_jd_logistics = models.BooleanField(default=False, verbose_name='是否京东物流')
    is_jd_supermarket = models.BooleanField(default=False, verbose_name='是否京东超市')
    is_jd_good_store = models.BooleanField(default=False, verbose_name='是否京东好店')
    is_jd_tianmao_store = models.BooleanField(default=False, verbose_name='是否天猫商城商品')
    class Meta:
        db_table = 'dz_case_attribute'

class CaseRotionCard(BaseModel):
    '''案例轮播图模型类'''
    rotion_card_id = models.CharField(max_length=128,primary_key=True,verbose_name='案例轮播图id')
    case = models.ForeignKey('CaseInfos',on_delete=models.DO_NOTHING,verbose_name='案例')
    case_picture = models.ImageField(upload_to='cases/rotion/',verbose_name='案例轮播图图片')
    index = models.IntegerField(verbose_name='轮播图的优先级')
    url = models.URLField(verbose_name='轮播图锁指向的案例的url')
    class Meta:
        db_table = 'dz_case_rotion_card'

class StepFlow(BaseModel):
    '''步骤流程图模型类'''
    step_flow_id = models.CharField(max_length=128,primary_key=True,verbose_name='步骤流程id')
    step_picture = models.ImageField(upload_to='cases/stepflow/', verbose_name='流程轮播图图片')
    index = models.IntegerField(verbose_name='轮播图的优先级')
    class Meta:
        db_table = 'dz_step_flow'

