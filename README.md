# Some Useful Software Developement Tools
This repo was created for a talk on software development tools for scientists.
## Debbugging
### Example 1
We introduce `ipdb` with `debugging_example_1.py`. The idea is to show that one can use `ipdb` instead of adding prints everywhere, allowing us to decide dynamically what to “print”.

```Bash
> python debugging_example_1.py
None
```
We add the breakpoint `import ipdb; ipdb.set_trace()` inside `filter_and_sort`. We explore a little to introduce the commands `l`, `n`, and the posibility of calculating things interactively. Then we show that `sorted_temps` is `None` cause `.sort()` sorts in place.
```bash
ipdb> l
      1 def filter_and_sort(temps, threshold):
      2     import ipdb; ipdb.set_trace()
      3     filtered = [t for t in temps if t > threshold]
----> 4     sorted_temps = filtered.sort()
      5     return sorted_temps
      6
      7 if __name__ == "__main__":
      8     temps = [23.1, 19.5, 21.7, 25.0]
      9     print(filter_and_sort(temps, 20))

ipdb> filtered
[23.1, 21.7, 25.0]
ipdb> temps
[23.1, 19.5, 21.7, 25.0]
ipdb> print(set(temps)-set(filtered))
{19.5}
ipdb> n
> /home/nate/Devel/sft_dev_seminar/debugging_example_1.py(5)filter_and_sort()
      4     sorted_temps = filtered.sort()
----> 5     return sorted_temps
      6

ipdb> sorted_temps
ipdb> type(sorted_temps)
<class 'NoneType'>
ipdb> filtered
[21.7, 23.1, 25.0]
```
After having established that we modified `filtered` in place and that we didn't actually assigned anything to `sorted_temps`, we can show the solution in `sol_debugging_example_1.py`. It's probably a good idea to run the correct code using `ipython`.
```Bash
~/Devel/sft_dev_seminar > ipython
```
```Python
In [1]: def filter_and_sort(temps, threshold):
   ...:     filtered = [t for t in temps if t > threshold]
   ...:     filtered.sort()
   ...:     return filtered
   ...:

In [2]: temps = [23.1, 19.5, 21.7, 25.0]

In [3]: print(filter_and_sort(temps, 20))
[21.7, 23.1, 25.0]

In [4]:
```

### Example 2
In `debugging_example_2.py` we introduce the idea of having a function that checks part of our code, not yet set up as a proper unit test. The idea here is to illustrate that we can step into fuctions, and also to prepare the ground for testing.

### Example 3
