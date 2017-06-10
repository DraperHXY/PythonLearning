rec = {
    'name': {
        'first': 'Bob', 'last': 'Smith'
    },
    'job': ['dev', 'mgr'],
    'age':40.5
}
print(rec['name'])
print(rec['name']['last'])
print(rec['job'])
rec['job'].append('janitor')
print(rec)

