# Some Useful Software Developement Tools
This repo was created for a talk on software development tools for scientists. Contents:

0. Coding Environments
1. Debbuging
2. Virtual Environment
3. Version Control (& GitHub)
4. Packing
5. Testing
6. Style (of code and documentation)
7. Tox (Orchestration)
8. Software Design (Good Design, SOLID, and Design Patterns)

The main file for the seminar is the notebook `main.ipynb`. That file indicates that the reader should follow the instructions below for the examples on debugging.

For running the examples, you'll need some dependencies that you can install as needed, or you can simply install everything in my requirement files:
```bash
pip install -r usual_requirements.txt
pip install -r dev-requirements.txt
```

Disclaimer: `main.ipynb` points to examples including code in other repos not presented here. Should you really need to see those parts, you can contact me via [email](mailto:jerofotinos@gmail.com).

## Debbugging
### Example 1
We introduce `ipdb` with `debugging_example_1.py`. The idea is to show that one can use `ipdb` instead of adding prints everywhere, allowing us to decide dynamically what to “print”.

```Bash
> python debugging_example_1.py
None
```
We add the breakpoint `import ipdb; ipdb.set_trace()` inside `filter_and_sort`. We explore a little to introduce the commands `l`, `n`, and the posibility of calculating things interactively. Then we show that `sorted_temps` is `None` cause `.sort()` sorts in place.
```Python
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
In `debugging_example_2.py` we introduce the idea of having a function that checks part of our code, not yet set up as a proper unit test. The idea here is to illustrate that we can step into fuctions, and also to prepare the ground for testing. Again, we begin by running the example's script.
```Bash
└─> python debugging_example_2.py
There's some type of error :(
```
After that we uncomment the checkpoint and run again the script. We show that `p` and `q` have been properly defined and get to the step were we're just about to excecute the line that calls the `check_distance` function. We can do a demonstration of not stepping first.

```Python
ipdb> l
     15
     16 if __name__ == "__main__":
     17     p = (0.0, 0.0)
     18     q = (1.0, 1.0)
     19     import ipdb; ipdb.set_trace()
---> 20     correct_distance = Decimal(2).sqrt()
     21     check_distance(vector_1=p, vector_2=q, target=correct_distance)

ipdb> print(p)
(0.0, 0.0)
ipdb> print(q)
(1.0, 1.0)
ipdb> print(correct_distance)
*** NameError: name 'correct_distance' is not defined
ipdb> n
> /home/nate/Devel/sft_dev_seminar/debugging/debugging_example_2.py(21)<module>()
     19     import ipdb; ipdb.set_trace()
     20     correct_distance = Decimal(2).sqrt()
---> 21     check_distance(vector_1=p, vector_2=q, target=correct_distance)

ipdb> print(correct_distance)
1.414213562373095048801688724
ipdb> n
There's some type of error :(
--Return--
```
This wasn't very helpful. What we should do instead is to step into the `check_distance` function.

```Python
└─> python debugging_example_2.py
> /home/nate/Devel/sft_dev_seminar/debugging/debugging_example_2.py(20)<module>()
     19     import ipdb; ipdb.set_trace()
---> 20     correct_distance = Decimal(2).sqrt()
     21     check_distance(vector_1=p, vector_2=q, target=correct_distance)

ipdb> n
> /home/nate/Devel/sft_dev_seminar/debugging/debugging_example_2.py(21)<module>()
     19     import ipdb; ipdb.set_trace()
     20     correct_distance = Decimal(2).sqrt()
---> 21     check_distance(vector_1=p, vector_2=q, target=correct_distance)

ipdb> s
--Call--
> /home/nate/Devel/sft_dev_seminar/debugging/debugging_example_2.py(8)check_distance()
      7
----> 8 def check_distance(vector_1, vector_2, target):
      9     d = distance(vector_1, vector_2)

ipdb> n
> /home/nate/Devel/sft_dev_seminar/debugging/debugging_example_2.py(9)check_distance()
      8 def check_distance(vector_1, vector_2, target):
----> 9     d = distance(vector_1, vector_2)
     10     # we compare the distances

ipdb> n
> /home/nate/Devel/sft_dev_seminar/debugging/debugging_example_2.py(11)check_distance()
     10     # we compare the distances
---> 11     if d == target:
     12         print("Correct distance calculation :)")

ipdb> print(d)
1.4142135623730951
ipdb> print(target)
1.414213562373095048801688724
```
And now it is cristal clear that the error stems from the precision difference.

### Example 3
This las example is just to show a bit less trivial example. Same as before, we run the script `debugging_example_3.py`, then debug (when calculating B, A got modified), and then show the solution in `sol_debugging_example_3.py` and copy the correct code in ipython just to check.

## Testing
### Unit and Integration Testing
I'll show a simple example of automated testing with `pytest` in a small repo, explaining the concepts of unit test and integration test. I'll leave here the command to run just in case.
```Bash
pytest -v <carpeta con los tests>  --cov <carpeta con el código> --cov-fail-under 90 --cov-report term-missing
```

### Property-Based Testing
To illustrate what's the interest of PBT, we show how we can test for a general property like symmetry of a distance:
```bash
pytest -v test_distance_symmetry.py
```
To show that `hypothesis` finds the *minimal* counterexample to the property.
```Bash
pytest test_capped_sum.py --hypothesis-verbosity=debug --hypothesis-show-statistics
```
