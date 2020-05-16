test = {
  'name': 'Dictionaries',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> d1 = dict() # If there's an error, type Error
          >>> d1['Penny'] = 'penny[at]hotmail.com'
          >>> print(d1['Penny'])
          efb26292a3ff2d84a6d4996f199b32e5
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # If there's an error, type Error
          >>> d1 = dict(Mateo='mateo[at]imperial.ac.uk')
          >>> d1['Dave'] = 'dave93[at]gmail.com'
          >>> print(d1['Mateo'])
          944ec4d3e6bdbb3378ecfd333425123e
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> # If there's an error, type Error
          >>> songs = {'Kraftwerk': 'Trans-Europe Express', 'Talking Heads': 'I Zimbra'}
          >>> songs['Steve Reich'] = 'Electric Counterpoint'
          >>> songs['Talking Heads'] 
          d0d7c541134228a12a71f1b8bdff9976
          # locked
          >>> 'Electric Counterpoint' in list(songs)
          bc7c4866f6593cc5a61914e675ee18c7
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> d = {'Joe':123, 'Jane':234}
          >>> sorted(list(d.keys()))
          e9db1538b178239cd48451401ee77699
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
