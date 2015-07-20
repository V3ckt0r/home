#!/bin/sh

ORACLE_HOME=/u01/app/oracle/prodict/11.2.0/client1/
LD_LIBRARY_PATH=u01/app/oracle/product/11.2.0/client_1/lib

export ORACLE_HOME
export LD_LIBRARY_PATH


python test.py
#./test.py

