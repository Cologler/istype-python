@set HTTP_PROXY=http://127.0.0.1:1082
@set HTTPS_PROXY=https://127.0.0.1:1082
python setup.py register sdist bdist_egg upload
