test = {
  'name': 'Extra',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> 8 // 2 * 3 % 5
          f7d3cdb0402b42e52c954901449d93cb
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> 2 ** 4 // 3 + 2 ** (4 // 3)
          d17308edd69158ccc9b5c658c0aad9e5
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> price_2015 = 400000
          >>> price_2016 = 500000
          >>> price_pct_change = (price_2016 - price_2015) / price_2015 * 100
          >>> print(price_pct_change)
          40e8c2f7cea9515d5ae5ee9aaebc7363
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print('I have \n one \n two \n three \n books')
          4f8be665a42f480f008623f8ab76fa1a
          c7566f59a634bb71fa60b85273e0467e
          f95ee9d2d317c425c105107c38eabe97
          43588f637bda882c01eaec04c1acef9c
          5222e5a183eec7faeaf81e302a9f33b7
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> a = '9.95'
          >>> b = float(a)
          >>> type(b)
          c4dd4083edb8816bfbae995a787593d4
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> str(int(float(str(1.5))) + 2.5)
          c89247abb4db0fc78b2ce130dcb918e6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> float(str(4.2)) + float(int(float(str(4.2))))
          ec1ff91e4fd57977626001633584d54a
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print(1 and not 0 == 5)
          1ac56596133f2112dab3e3ff26ecc44f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print(0>=0 or 0 and True)
          1ac56596133f2112dab3e3ff26ecc44f
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print(0>=0 and 0 and True)
          40ff8b60a7b29f23ce960dc442025d66
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> print(5 * 4 == 20, 5 >= 5, not 5 != 4)
          be84bf2ea028e8d69c554699285a12e6
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> first_name = 'Franz'
          >>> print(first_name == 'Franz', type(first_name) == str)
          3d974d367a4992692827efde4d43d742
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
