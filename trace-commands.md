## Trace commands

Run module with tracing every executed line

`python -m trace --trace trace_example\example-two.py`

`python -m trace --ignore-dir 'C:users\piotr\miniconda3\Lib' --trace trace_example\example-two.py`

Count total executions of each line (code coverage)
```
python -m trace --count trace_example\example-two.py
notepad trace_example\example-two.cover
```

Report several combined coverages

`python -m trace --coverdir trace_cover --count --file trace_cover\report.dat example-two.py`

`python -m trace --coverdir trace_cover --report --summary --missing --file trace_cover\report.dat`