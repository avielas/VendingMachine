@pushd %~dp0
py -3.6 setup.py develop --uninstall
@popd

@IF "%1" NEQ "SILENT" (
    PAUSE
)
