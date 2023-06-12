from jenkinsapi.jenkins import Jenkins

jenkins = Jenkins('http://127.0.0.1:8080/', useCrumb=True, username='hogwarts', password='114a2ced7e0ce84a56e38d53a67f644e1a')
#todo: 按需添加认证信息

