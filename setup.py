from setuptools import find_packages,setup

hyphen_e_dot = '-e .'

def get_requirements(file_path:str)->list[str]:
    with open(file_path,'r') as f:
        requirements = f.readlines()
        requirements = [req.replace('\n',"") for req in requirements]
        requirements = [req.rstrip() for req in requirements]
        
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
        
        return requirements



setup(
    name='test_project',
    version='0.0.1',
    author='Himanshu',
    author_email='himanshu1703@gmail.com',
    packages=find_packages(),
    requires=get_requirements('requirements.txt')
)
