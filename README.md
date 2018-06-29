# solo
Python module to ensure only a single instance of a program is running. 

## Synopsis

To check for other instances of a script running and stop all other instances: 

```python
import solo
solo.chk_and_stopall(__file__)
```

To check for other instances of a script are running and stop self (sys.exit(-1))

```python
import solo
solo.chk_and_stopself(__file__)
```

## Dependencies

Uses psutil which gives cross platform magic 

