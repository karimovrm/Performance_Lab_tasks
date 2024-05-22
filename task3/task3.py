import json


with open('tests.json', 'r') as file_tests:
    tests = json.load(file_tests)


with open('values.json', 'r') as file_values:
    values = json.load(file_values)


def input_value(test_id, test):
    for value in values['values']:
        if test_id == value['id']:
            test['value'] = value['value']


for test1 in tests['tests']:
    test_id = test1['id']
    input_value(test_id, test1)
    if 'values' in test1:
        for test2 in test1['values']:
            test_id = test2['id']
            input_value(test_id, test2)
            if 'values' in test2:
                for test3 in test2['values']:
                    test_id = test3['id']
                    input_value(test_id, test3)
                    if 'values' in test3:
                        for test4 in test3['values']:
                            test_id = test4['id']
                            input_value(test_id, test4)


with open('report.json', 'w') as file_report:
    json.dump(tests, file_report)



