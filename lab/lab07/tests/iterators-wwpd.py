test = {
  'name': 'Iterators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Enter StopIteration if StopIteration exception occurs, Error for other errors
          >>> # Enter Iterator if the output is an iterator object.
          >>> s = [1, 2, 3, 4]
          >>> t = iter(s)
          >>> next(s) 
          795bceccbca635277a3bbfa64bc9dba0
          # locked
          >>> next(t)
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> next(t)
          c9aea858aa12d15d170a9fd7596d70b1
          # locked
          >>> iter(s)
          8b4ce7a6f0d1eeeb34ff90fb7c678f24
          # locked
          >>> next(iter(s))
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> next(iter(t))
          9a023de211dac9bf8558350f5fa3bdca
          # locked
          >>> next(iter(s))
          030bca9dd0d55198e3fa5a2ab185b285
          # locked
          >>> next(iter(t))
          f2991d685f624ad59b79213e20800653
          # locked
          >>> next(t)
          05a15eb5f98182075ce2901cad69fc3a
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> r = range(6)
          >>> r_iter = iter(r)
          >>> next(r_iter)
          67a37433345d12b97afe4885b1fa6019
          # locked
          >>> [x + 1 for x in r]
          9e03e882809e6614b7d41f56d988605f
          # locked
          >>> [x + 1 for x in r_iter]
          8e5519d9a54fe07f53b8a6e00df7c476
          # locked
          >>> next(r_iter)
          05a15eb5f98182075ce2901cad69fc3a
          # locked
          >>> list(range(-2, 4))   # Converts an iterable into a list
          64867940d30d6d33657d35a59c852d98
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> map_iter = map(lambda x : x + 10, range(5))
          >>> next(map_iter)
          700368183fe24919898aaeca9b976fbd
          # locked
          >>> next(map_iter)
          44567d7ece823e5a44bf86d110909d16
          # locked
          >>> list(map_iter)
          6accc321f5175879b1eeac30e99f77d4
          # locked
          >>> for e in filter(lambda x : x % 2 == 0, range(1000, 1008)):
          ...     print(e)
          edb6f8e1ec6e1bc0b2deae8f8cd333bf
          099c150bda72a24b73dc2cb8f5f49db1
          bb8d5e84aaf2e424fcfad3fa0ea6b7cb
          d90474a8ceed1879bae876a479f97354
          # locked
          >>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
          367c80da127d9e6e87c2b0e6263d3abe
          # locked
          >>> for e in zip([10, 9, 8], range(3)):
          ...   print(tuple(map(lambda x: x + 2, e)))
          f0829be0ca890c83a3353a8ec565df3e
          4efa8abe373c21808fc6d504dc42995a
          f077d61d615e84899e87f9eda9200ef8
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
