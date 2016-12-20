from django.contrib.auth import authenticate
from django.contrib.auth.models import User , Group

from core.models import TechUser, GrupoUsuarios


class TechCDBackend(object):


    def authenticate(self, username=None, password=None):

        # senha padrao para usuario
        default_password = 'logan277'

        # verifica se o usuario existe.
        tech_user = TechUser.objects.using('techcd').filter(username=username)


        # se o usuario não existir no banco legado  ele estará como None
        if tech_user is not None:
            try:
                # se existe no auth_db , entao crie ele para mim...
                user = User.objects.get(username=username)
                if user.check_password(password):
                    return user
                return None
            except User.DoesNotExist:

                # refatorar para funcção
                # quando não existir eu crio um usuario
                user = User(username=username)
                user.set_password(default_password)
                user.is_active = True
                user.save()

                # refatorar para funcção
                # set o grupo relacionado com o usuario ....
                tech_group_user = GrupoUsuarios.objects.using('techcd').filter(groups=tech_user)[0]
                group, created = Group.objects.get_or_create(name=tech_group_user.desc_grupo.strip())
                _user = User.objects.get(username=username)
                _user.groups.add(group)
                _user.save()

                return user
        return None



    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None