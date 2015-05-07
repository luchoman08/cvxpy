from setuptools import setup

setup(
    name='cvxpy',
    version='0.2.20',
    author='Steven Diamond, Eric Chu, Stephen Boyd',
    author_email='stevend2@stanford.edu, echu508@stanford.edu, boyd@stanford.edu',
    packages=['cvxpy',
              'cvxpy.atoms',
              'cvxpy.atoms.affine',
              'cvxpy.atoms.elementwise',
              'cvxpy.constraints',
              'cvxpy.expressions',
              'cvxpy.expressions.constants',
              'cvxpy.expressions.variables',
              'cvxpy.interface',
              'cvxpy.interface.numpy_interface',
              'cvxpy.interface.cvxopt_interface',
              'cvxpy.lin_ops',
              'cvxpy.problems',
              'cvxpy.problems.problem_data',
              'cvxpy.problems.solvers',
              'cvxpy.tests',
              'cvxpy.utilities'],
    package_dir={'cvxpy': 'cvxpy'},
        url='http://github.com/cvxgrp/cvxpy/',
    license='GPLv3',
    zip_safe=False,
    description='A domain-specific language for modeling convex optimization problems in Python.',
    install_requires=["cvxopt >= 1.1.6",
                      "ecos >= 1.1.1",
                      "scs >= 1.0.6",
                      "toolz",
                      "numpy >= 1.9",
                      "scipy >= 0.15"],
    use_2to3=True,
)
