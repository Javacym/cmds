@echo off
e:
cd Works/python/
set /p option=choose your work dir:
cd %option%
dir
set /p pfile=choose file you want to run:
set info=****************RUN Python PROGRAMME************************
set d=%date:~0,10%
set t=%time:~0,8%
echo %info%
echo *              *filename:%pfile%
echo * Fuck Python  *Power by cheng
echo *              *DAY:%d%
echo *              *TIME:%t%
echo ************************************************************
set pf=%pfile%.py
py %pf%
call cmd