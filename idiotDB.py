# idiotDB 2018 Muzaffer Yildirim
import os
import shutil
import ast
import json

defdb = ""
deftb = ""


################################################################
#Create a new idiotDB
def createdb(name):
    global defdb
    if not os.path.exists(name):
        os.makedirs(name)
        defaultdb(name)
        return True
    else:
        defaultdb(name)
        return False
################################################################
#Create a new idiotDB table
def createtb(tbname,dbname = None):
    global deftb
    if dbname is None:
        dbname = defdb
    if not os.path.exists(dbname+"/"+tbname):
        with open(dbname+"/"+tbname,"w") as table:
            table.write("{}")
        defaulttb(tbname)
        return True
    else:
        defaulttb(tbname)
        return False
################################################################
#Create idiotDB and table
def create(db,tb):
    return createdb(db), createtb(tb)
################################################################
#Delete idiotDB
def deletedb(name):
    if os.path.exists(name):
        shutil.rmtree(name)
        return True
    else:
        return False
################################################################
#Delete idiotDB table
def deletetb(tbname, dbname=None):
    global defdb
    if dbname == None:
        dbname = defdb
    if os.path.exists(dbname+"/"+tbname):
        os.remove(dbname+"/"+tbname)
        return True
    else:
        return False
################################################################
#select default idiotDB
def defaultdb(dbname):
    global defdb
    defdb= dbname
    return defdb
################################################################
#select default idiotDB table
def defaulttb(tbname):
    global deftb
    deftb= tbname
    return deftb
################################################################
#select default idiotDB and table
def default(db,tb):
    return defaultdb(db), defaulttb(tb)
################################################################
#add data
def add(db=None,tb=None, **kwargs):
    if db == None:
        db = defdb
    if tb == None:
        tb = deftb
    with open(db+"/"+tb, "r") as table:
        main = ast.literal_eval(table.read())
        try:
            key = max(data, key=int)+1
        except:
            key = 0
        main.update({key:kwargs})
    with open(db+"/"+tb, "w") as table2:
        table2.write(str(main))
    return True
################################################################
def delete(deldata):
    pass
################################################################
# def search(db=None,tb=None, **kwargs):
#     if db == None:
#         db = defdb
#     if tb == None:
#         tb = deftb
#     with open(db+"/"+tb, "r") as table:
#         main = ast.literal_eval(table.read())
#
################################################################
def all(tb=None,db=None):
    if db == None:
        db = defdb
    if tb == None:
        tb = deftb
    with open(db+"/"+tb, "r") as table:
        data = ast.literal_eval(table.read())
        message = {'status':'success','database':'idiotDB.v001','data':data}
        return json.dumps(message, ensure_ascii=False)
