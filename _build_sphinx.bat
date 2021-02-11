@pushd %~dp0
py -3.6 setup.py build_sphinx

@IF "%1" NEQ "SILENT" (
    build\sphinx\html\index.html
)

@popd

@IF "%1" NEQ "SILENT" (
    PAUSE
)
