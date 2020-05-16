test = {
  'name': 'Strings',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> x = 'Franz'
          >>> y = 'Kafka'
          >>> z = x + y
          >>> print(z)
          99ab7508b535354ea308aae00481d6c4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> x = 'Franz'
          >>> y = 'Kafka'
          >>> c = ' '
          >>> z = x + c + y
          >>> print(z)
          e5c23d2401d0b7fc0da61c856fa63334
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print('Two'*1 + 'Three'*2)
          23f2202004bf225a7381659cd5fe79d3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> phrase = 'It wasn\'t me' # If the code results in an error, type Error
          >>> print(phrase)
          0532529923ac64549287b8ba23e2d212
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> phrase = 'It wasn't me' # If the code results in an error, type Error
          01a8ea71318920ea344bc6dce6de30e2
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
