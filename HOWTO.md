# Python Packaging


#### Python Package Project Structure

```
project-name
|- README.md
|- LICENSE.txt
|- .gitignore
|- requirements.txt
|- library-name
	|- __init__.py
|- setup.py
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


#### How to install a package

##### Locally

```python
pip install ./my-package
```

#### From GitHub

```python
pip install git+https://github.com/<github-username>/<project-name>
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
