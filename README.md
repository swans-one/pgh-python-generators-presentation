# Generators: Advanced Iteration and More

This repository contains code and notes for the presentation given to
the Pittsburgh Python Users Group on September 27th, 2017.

## Lessons & Examples

This talk was divided into two sections, in the first section we
covered the basics of iterators, generators, and coroutines. This was
further divided into four lessons, `01-Iterators.ipynb` to
`04-Coroutines.ipynb`. These were developed live in the talk, but
ipython notebooks with some explanation of the code and the concepts
are here in this repository.

The second section covered some use cases that approached real world
use of generators, including using their suspended execution to
implement context managers, architecting a data-pipeline that follows
a live updating file, and a very very simple use of asyncio's event
loop. These were done in five example lessons `Ex01-Context.ipynb`
through `Ex05-EventLoop.ipynb`. These examples do not have any
explanation in them, but you're encouraged to experiment with them.

## Slides

Slides are included in PDF form in the file slides.pdf.

## Other source files

There is additionally a python source file `fake_logger.py` which
periodically writes fake log entries to a file. In order for the
follower examples to work, this should be running with a command line
specifying the file. The following usage should work:

```
$ python fake_logger.py fake_log.txt
```

# License

All code is licensed under the MIT license. See LICENSE.txt for
details.
