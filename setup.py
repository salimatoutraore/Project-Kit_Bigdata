from setuptools import setup, find_packages

# Les données de projet
setup(
    name='my_task_manager',
    version='1.0',
    description='Métadonnées et informations sur la construction de projet To-do List',
    author='Alban Pereira, Yuchen Xia, Aurélien Raulo, Salimatou Traore',
    author_email='alban.pereira98@gmail.com, xiayuchen35@gmail.com, aurelien0raulo@gmail.com, tra.salimatou@gmail.com',
    packages=find_packages(),
    install_requires=[
        'datetime',
        'logging',
    ],
    zip_safe=False,
)
