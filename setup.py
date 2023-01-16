from setuptools import setup, find_packages

setup(
    name='skip-django-project-info',
    version='1.0.2.1',
    description='A small plugin which takes a configuration (like Bower or npm) and it provides data via context'
    'processors.',
    keywords='django, project-info',
    author='Lukas Rychtecky',
    author_email='lukas.rychtecky@gmail.com',
    url='https://github.com/skip-pay/django-project-info',
    license='MIT',
    package_dir={'project_info': 'project_info'},
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'django>=1.11',
    ],
    zip_safe=False
)
