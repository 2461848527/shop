#encoding: utf-8

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from shortuuidfield import ShortUUIDField
from django.db import models
from db.base_model import BaseModel


class UserManager(BaseUserManager):
    # eg.2
    # 有下划线是受保护的方法，不能够再外面被使用，创建用户
    def _create_user(self,email,username,password,**kwargs):
        if not email:
            raise ValueError('请传入邮箱号！')
        if not username:
            raise ValueError('请传入用户名！')
        if not password:
            raise ValueError('请传入密码！')

        user = self.model(email=email,username=username,**kwargs)
        # 密码设置进去
        user.set_password(password)
        user.save()
        return user

    def create_user(self,email,username,password,**kwargs):
        """创建普通用户"""
        # eg.3
        kwargs['is_superuser'] = False
        return self._create_user(email,username,password,**kwargs)

    def create_superuser(self,email,username,password,**kwargs):
        """创建超级用户"""
        # eg.4
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(email,username,password,**kwargs)


class User(AbstractBaseUser,PermissionsMixin,BaseModel):
    # eg.1
    # 我们不使用默认的自增长的主键
    # 防止机密泄露
    # id：100，101，102，103
    # uuid/shortuuid
    # Shortuuidfield：pip install django-shortuuidfield
    # 既保证唯一性，也不会太长
    user_id = ShortUUIDField(primary_key=True)
    # # 用户账号
    # user_account = models.CharField(max_length=20)
    # 用户名
    username = models.CharField(max_length=100,null=True,default='客人')
    # 头像图片
    head_picture = models.ImageField(upload_to='cases/headpicture/')
    # 微信号
    wechat = models.CharField(max_length=20,null=True)
    # QQ号
    qq = models.CharField(max_length=11,null=True)
    # 手机号
    telephone = models.CharField(max_length=11,null=True)
    # 保留邮箱，以免以后有开发需要
    email = models.EmailField(unique=True,null=True)
    # 是否是可用的，默认是可用的
    is_active = models.BooleanField(default=False)
    # 是否是员工
    is_staff = models.BooleanField(default=False)
    # 作为唯一验证的，默认会用username字段
    USERNAME_FIELD = 'email'
    # 调createsuperuser，就会去让填这些字段， USERNAME_FIELD也会提示让你输入
    # email，username，password
    REQUIRED_FIELDS = ['username']
    # 给指定用户发送邮件
    EMAIL_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username
    class Meta:
        db_table = 'dz_user'