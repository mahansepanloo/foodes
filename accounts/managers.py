from django.contrib.auth.models import BaseUserManager




class Usermanager(BaseUserManager):
    def create_user(self,username,phone_number,password):
        if not username:
            return ValueError('نام کاربری را وارد کنید')
        if not phone_number:
            return ValueError('شماره تماس را وارد کنید')
        if not password:
            return ValueError('رمز عبور را وارد کنید')

        user = self.model(username=username,phone_number=phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username,phone_number,password):
        user = self.create_user(username,phone_number,password)
        user.is_admin = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

