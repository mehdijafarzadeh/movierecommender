# Python Packaging


#### Python Package Project Structure

```
./project-name
|- README.md
|- LICENSE.txt
|- .gitignore
|- requirements.txt
|- package-name
	|- __init__.py
	|- other_module.py
|- setup.py
```

#### How to install a package

##### Locally

```python
pip install ./project-name
```

or if you are allready inside the project folder

```python
pip install ./
```



#### From GitHub

```python
pip install git+https://github.com/<github-username>/<project-name>
```


#### How to add package dependencies?

add the following argument to your `setup.py`:

```python
install_requires=[
        'pandas',
        'scikit-learn'
]
```


#### How to add external data files?

add the following argument to your `setup.py`:

```python
package_data= {
    '<package-name>': ['data/*.csv', 'trained_models/*.pickle']
}
```


#### How to read in packaged data files?

```Python
import pandas as pd
import os

package_dir = os.path.dirname(__file__)

df = pd.read_csv(package_dir + '/data/my_data.csv')
```


#### How to specify a Python package on GitHub in the `requirements.txt`?

open your  `requirements.txt` and add the line:

```shell
git+git://github.com/<user>/<repo>
```

You can then install it with:

```
pip install -r requirements.txt
```


#### How to upload your package to PyPy

1. Register an acount on https://test.pypi.org/  
2. Setup your credentials in a `.pypirc` file, it should look like that:
```
[testpypi]
  username = __token__
  password = <your-token-from-the-website>
```

3. Build and upload your package:

```shell
python setup.py sdist bdist_wheel
twine upload --repository testpypi dist/*
```






