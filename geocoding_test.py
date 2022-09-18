import geocoding as gc
import os

def test_read_file():
    org_line_one=['bangalore\n','mumbai\n','pune']
    org_line_two=['bhopal\n','agra\n','dewas']
    org_line_three=['hyderabad\n','mumbai\n','delhi']
    assert gc.read_file('input_test/input_test_one.txt')==org_line_one
    assert gc.read_file('input_test/input_test_two.txt')==org_line_two
    assert gc.read_file('input_test/input_test_three.txt')==org_line_three

def test_clean_data():
    org_line_one=['bangalore','mumbai','pune']
    org_line_two=['bhopal','agra','dewas']
    org_line_three=['hyderabad','mumbai','delhi']
    assert gc.clean_data(['bangalore\n','mumbai\n','\n','pune'])==org_line_one
    assert gc.clean_data(['bhopal\n','agra\n','dewas'])==org_line_two
    assert gc.clean_data(['hyderabad\n','mumbai\n','delhi'])==org_line_three

def test_compute_geocode():
    assert False==gc.compute_geocode([])
    assert True==gc.compute_geocode(['bangalore','mumbai','pune'])
    if os.path.exists('output.txt'):
        os.remove('output.txt')
    assert True==gc.compute_geocode(['bangalore','mum','pune'])
    if os.path.exists('output.txt'):
        os.remove('output.txt')

