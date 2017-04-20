from django.contrib.auth import authenticate
from django.db.models import Q
from django.contrib.auth.models import User , Group
from core.models import TechUser, GrupoUsuarios


class TechCDBackend(object):


    def authenticate(self, username=None, password=None):

        # senha padrao para usuario
        default_password = 'tech2433'

        # verifica se o usuario existe.
        tech_user = TechUser.objects.using('techcd').\
            filter(Q(username=username),Q(password=password)).first()

        # se o usuario não existir no banco legado  ele estará como None
        if tech_user:
            # se existe no auth_db , entao crie ele para mim...
            user = User.objects.filter(username=username).first()
            if user :
                return user
            else:
                # quando não existir eu crio um usuario
                _user = User(username=username)
                _user.set_password(default_password)
                _user.is_active = True
                _user.save()
                group_user = GrupoUsuarios.objects.using('techcd').get(groups=tech_user)
                group, created = Group.objects.get_or_create(name=group_user.desc_grupo.strip())
                _user.groups.add(group)
                _user.save()

                return _user
        else:
            return None



    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None