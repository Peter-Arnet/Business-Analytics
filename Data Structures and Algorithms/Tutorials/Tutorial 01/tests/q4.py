test = {
  'name': 'Objects',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type('23')
          8675ec7c479e01a86801e44b5c3040bb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> type(42)
          be8bc8785e021285ac146ee280503e28
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> number = '3' # If there is an error, type Error
          >>> number = int(number)
          >>> number + 2
          379a92d554955ef9651d0899c9f66740
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> number = '3' # If there is an error, type Error
          >>> type(number * 4)
          8675ec7c479e01a86801e44b5c3040bb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> number = '3' # If there is an error, type Error
          >>> print(number + 2)
          01a8ea71318920ea344bc6dce6de30e2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> c = 5.1 # If there is an error, type Error
          >>> s = str(c)
          >>> print('The number is ' + s)
          5d4bdb0276b8f3ee8f5fe81adb11e965
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> number = '3' # If there is an error, type Error
          >>> number = float(number * 4)
          >>> number
          eabf476ee4b717d01881ed64aaa901a4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> number = '3'
          >>> number = float(number  + '5')
          >>> number
          9f2ce7ce2d4893d5e0dcf594ed83f163
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> int(2.5) + 2.5
          c6e1ac59c28187d66c978756d1859ac3
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> max(3, 5.0)
          47fe3624ada7fc8fd94efd60b0d5609f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> type(max(3, 1.0))
          be8bc8785e021285ac146ee280503e28
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> type(max(3, 10.0))
          c4dd4083edb8816bfbae995a787593d4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> round(3.8)
          7d7e6a0a27e3ca1a9e6a8111701a8359
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> type(round(4.53))
          be8bc8785e021285ac146ee280503e28
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> type(round(4.53, 1))
          c4dd4083edb8816bfbae995a787593d4
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
