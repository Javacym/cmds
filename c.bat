@echo off
e:
cd Works\c-program
set /p option=choose your work dir:
cd %option%
set /p cfile=choose file you want to make to run:
set info=****************RUN C PROGRAMME************************
set d=%date:~0,10%
set t=%time:~0,8%
echo %info%
echo *              *filename: %cfile%
echo *    Fuck C    *Power by cheng
echo *              *create time:%d% %t%
echo *******************************************************
set f=%cfile%.c
gcc -o %cfile% %f%
%cfile%
pause
call cmd
