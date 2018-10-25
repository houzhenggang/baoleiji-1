#get ready
import getpass,os,sys
from django.contrib.auth import authenticate
from django.conf import settings
import subprocess
# from source.models import UserProfile


class userprepare(object):
    def __init__(self):
        self.user=None

    def user_input(self):
        """yonghu xinxi shuru"""
        try_number = 0
        while try_number<3:
            username = input("username:")
            if type(username) is str:
                username = username.strip()
            else:
                username = str(username).strip()
            if len(username) == 0:
                continue
            password = getpass.getpass("password:")
            if len(password)==0:
                print("password cant be null")
            user = authenticate(username=username,password=password)
            if user:
                self.user=user
                print("welcome login in")
                return
            else:
                print("username or password is wrong")
            try_number +=1
        else:
            exit("please enter again")

    def opreation(self,zhuji):

        username = zhuji.host_user.username
        password = zhuji.host_user.password
        ip = zhuji.host.ip_addr
        port = zhuji.host.port
        print("login %s@%s" % (username, ip))
        pas = 'sshpass -p %s ssh %s@%s -o "StricHostKeyChecking no"' %(password,username,ip)
        ssh_instance = subprocess.run(pas,shell=True)
        print("logout")




    def select(self):
        self.user_input()
        if self.user:
            while True:
                host_groups = self.user.hostgroup_set.all()
                hg_number=host_groups.count()
                print("$$$$$$$$$$$$$$$$zhujizu %s$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$" %(hg_number))
                for index,host_group in enumerate(host_groups):

                    print("%s %s") %(index,host_group.name)
                bind_hosts = self.user.bindhost_set.all()
                bh_number = bind_hosts.count()
                global bh_number
                print("$$$$$$$$$$$$$$$$dangezhuji %s$$$$$$$$$$$$$$" %(bh_number))
                for bind_host in bind_hosts:
                    for host in host_groups:
                        if bind_host in host.bindhost_set.all():
                            print(bind_host)
                            bind_hosts = list[bind_hosts]
                            bind_hosts.remove(bind_host)



                for index,bind_host in enumerate(bind_hosts):
                    print("%s.%s-%s@%s" %(hg_number,bind_host.host_group,bind_host.host,bind_host.host.ip_addr))
                #xuanze
                # while True:
                number = input("please select:")
                if number == "b":
                    break
                # print((str(number)))
                if len(str(number).strip()) ==0:
                    print((str(number)))
                    continue
                if isinstance(number,int):

                    if number<hg_number and number>=0:

                        selected_hostgroup= host_groups[number]
                        count = selected_hostgroup.bindhost_set.all()#zhu ji zu bao han de zhu ji
                        for index,bind_host in enumerate(selected_hostgroup.bindhost_set.all()):
                            print("%s.%s-%s@%s" % (index,
                                                   bind_host.host_group,
                                                   bind_host.host,
                                                   bind_host.host.ip_addr))
                            while True:
                                number = input("please select:")
                                if number == "b":
                                    break
                                # print((str(number)))
                                if len(str(number).strip()) == 0:

                                    continue
                                if isinstance(number, int):


                                    if number < count and number >= 0:
                                        obj=selected_hostgroup.bindhost_set.all()[number]
                                        self.opreation(obj)
                    elif number>=hg_number and number<hg_number+bh_number:
                        bh=bind_hosts[number-hg_number]
                        self.opreation(bh)







if __name__=="__main__":
    sys.path.insert(0, os.path.split(os.path.split(os.getcwd())[0])[0])
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "baoshijie.settings")
    os.environ['DJANGO_SETTINGS_MODULE']="baoshijie.settings"
    import django
    django.setup()
    from source.models import UserProfile
    up = userprepare()
    up.select()