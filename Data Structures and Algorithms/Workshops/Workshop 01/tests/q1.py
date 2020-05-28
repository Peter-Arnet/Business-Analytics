test = {
  'name': 'Recap',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> print(4 * 3)
          95c5e5b96c76b9df93db9a21430267e2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x = 2
          >>> y = 3
          >>> x = (y + 1)*x
          >>> print(x)
          17f312cdf3916843f719e96fdb50d116
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> temp = 30
          >>> print('Temp: ' + temp)
          4377ff50ab0714057a6bdfd461595c5b
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> x = 8
          >>> x < 5
          551e34ef337160a1c82519aae36e677e
          # locked
          >>> x > 0 and x < 7
          551e34ef337160a1c82519aae36e677e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> name = 'Franz'
          >>> if name == 'Franz':
          ...     print('Hello ' + name)
          25a18f38a155a4f4d3ae276eab0087ab
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}
