# Flik, a Python Package for Film Buffs

## Review Functionality

In order to get review rates for a specific movie use `review` function:

```python
import flik
flik.review('se7en')
```
The returned object is a python dictionary containing available review rating in the first page of the Google search:

```python
{'www.imdb.com': '8.6/10',
 'www.rottentomatoes.com': '82%',
 'www.amazon.com': '4.7'}
```
