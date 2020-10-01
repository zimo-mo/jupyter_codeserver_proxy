import setuptools

setuptools.setup(
    name="jupyter-codeserver-proxy",
    version='1.0.2',
    description="orign from  @dirkcgrunwald/jupyter_codeserver_proxy-",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'codeserver = jupyter_codeserver_proxy:setup_codeserver',
        ]
    },
    package_data={
        'jupyter_codeserver_proxy': ['icons/*'],
    },
)
