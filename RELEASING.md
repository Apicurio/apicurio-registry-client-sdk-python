# Release Guide

Here are the steps you need to take in order to create a new release of the `apicurioregistryclient` on [PyPI](https://pypi.org/project/apicurioregistryclient).

## Bump version in `setup.py`

1. `git checkout -b release-1.0.0`.
2. Set the value of `VERSION` in [setup.py](./setup.py) to "1.0.0".
3. `git add setup.py && git commit -m "chore: release 1.0.0"`.
4. Create a pull request and merge it to `main`.

## Create release

1. `git tag 1.0.0`.
2. `git push <remote> 1.0.0`.
3. The [Upload Python Package](https://github.com/Apicurio/apicurio-registry-client-sdk-python/actions/workflows/pythonpublish.yml) will start to publish the package to PyPI.
4. Once completed, the package should be available on [PyPI](https://pypi.org/project/apicurioregistryclient).
