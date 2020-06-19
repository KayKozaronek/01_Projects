**If you're using Powershell and want to execute scripts** 
```
Set-ExecutionPolicy Unrestricted
```

**Activate the virtual environment**
```
source blockchain-env/Scripts/activate
```

**Install all packages**
```
pip3 install -r requirements.txt
```

**Run the tests**

Make sure to activate the virtual environment.

```
python -m pytest backend/tests
```

